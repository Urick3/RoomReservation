document.addEventListener("DOMContentLoaded", function() {
    "use strict";

    var date = new Date();
    var today = date.getDate();
    
    document.getElementById("prev").addEventListener("click", function() {
        prev_year({ date: date });
    });
    document.getElementById("next").addEventListener("click", function() {
        next_year({ date: date });
    });

    var months = document.getElementsByClassName("month");
    for (var i = 0; i < months.length; i++) {
        months[i].addEventListener("click", function() {
            month_click({ date: date });
        });
    }

    document.getElementById("add-button").addEventListener("click", function() {
        new_event({ date: date });
    });

    var activeMonth = document.getElementsByClassName("months-row")[0].children[date.getMonth()];
    activeMonth.classList.add("active-month");

    init_calendar(date);

    var events = check_events(today, date.getMonth() + 1, date.getFullYear());
    show_events(events, months[date.getMonth()].textContent, today);
});

function init_calendar(date) {
    var tbody = document.getElementsByClassName("tbody")[0];
    var eventsContainer = document.getElementsByClassName("events-container")[0];
    tbody.innerHTML = "";
    eventsContainer.innerHTML = "";
    
    var calendar_days = tbody;
    var month = date.getMonth();
    var year = date.getFullYear();
    var day_count = days_in_month(month, year);
    var row = document.createElement("tr");
    row.className = "table-row";
    var today = date.getDate();

    date.setDate(1);
    var first_day = date.getDay();

    for (var i = 0; i < 35 + first_day; i++) {
        var day = i - first_day + 1;
        if (i % 7 === 0) {
            calendar_days.appendChild(row);
            row = document.createElement("tr");
            row.className = "table-row";
        }
        var curr_date;
        if (i < first_day || day > day_count) {
            curr_date = document.createElement("td");
            curr_date.className = "table-date nil";
        } else {
            curr_date = document.createElement("td");
            curr_date.className = "table-date";
            curr_date.textContent = day;
            var events = check_events(day, month + 1, year);
            if (today === day && document.getElementsByClassName("active-date").length === 0) {
                curr_date.classList.add("active-date");
                show_events(events, months[month], day);
            }
            if (events.length !== 0) {
                curr_date.classList.add("event-date");
            }
            curr_date.addEventListener("click", function() {
                date_click({ date: date });
            });
        }
        row.appendChild(curr_date);
    }
    calendar_days.appendChild(row);
    document.getElementsByClassName("year")[0].textContent = year;
}

function days_in_month(month, year) {
    return new Date(year, month + 1, 0).getDate();
}

function date_click(event) {
    var eventsContainer = document.getElementsByClassName("events-container")[0];
    eventsContainer.style.display = "block";
    document.getElementById("dialog").style.display = "none";
    var activeDate = document.getElementsByClassName("active-date")[0];
    if (activeDate) {
        activeDate.classList.remove("active-date");
    }
    event.target.classList.add("active-date");

    var day = parseInt(event.target.textContent);
    var month = document.getElementsByClassName("active-month")[0].textContent;
    var year = parseInt(document.getElementsByClassName("year")[0].textContent);

    var events = check_events(day, month_to_num(month), year);
    show_events(events, month, day);
}

function month_click(event) {
    var eventsContainer = document.getElementsByClassName("events-container")[0];
    eventsContainer.style.display = "block";
    document.getElementById("dialog").style.display = "none";

    var date = event.date;
    var activeMonth = document.getElementsByClassName("active-month")[0];
    if (activeMonth) {
        activeMonth.classList.remove("active-month");
    }
    event.target.classList.add("active-month");

    var new_month = Array.prototype.indexOf.call(event.target.parentNode.children, event.target);
    date.setMonth(new_month);
    init_calendar(date);
}

function next_year(event) {
    document.getElementById("dialog").style.display = "none";
    var date = event.date;
    var new_year = date.getFullYear() + 1;
    document.getElementsByClassName("year")[0].textContent = new_year;
    date.setFullYear(new_year);
    init_calendar(date);
}

function prev_year(event) {
    document.getElementById("dialog").style.display = "none";
    var date = event.date;
    var new_year = date.getFullYear() - 1;
    document.getElementsByClassName("year")[0].textContent = new_year;
    date.setFullYear(new_year);
    init_calendar(date);
}

function new_event(event) {
    if (document.getElementsByClassName("active-date").length === 0) return;

    document.getElementById("name").value = '';
    document.getElementById("count").value = '';
    var eventsContainer = document.getElementsByClassName("events-container")[0];
    eventsContainer.style.display = "none";
    document.getElementById("dialog").style.display = "block";

    document.getElementById("cancel-button").onclick = function() {
        document.getElementById("name").classList.remove("error-input");
        document.getElementById("count").classList.remove("error-input");
        document.getElementById("dialog").style.display = "none";
        eventsContainer.style.display = "block";
    };

    document.getElementById("ok-button").onclick = function() {
        var date = event.date;
        var name = document.getElementById("name").value.trim();
        var count = parseInt(document.getElementById("count").value.trim());
        var day = parseInt(document.getElementsByClassName("active-date")[0].textContent);
        if (name.length === 0) {
            document.getElementById("name").classList.add("error-input");
        } else if (isNaN(count)) {
            document.getElementById("count").classList.add("error-input");
        } else {
            document.getElementById("dialog").style.display = "none";
            new_event_json(name, count, date, day);
            date.setDate(day);
            init_calendar(date);
        }
    };
}

function new_event_json(name, count, date, day) {
    var event = {
        "occasion": name,
        "invited_count": count,
        "year": date.getFullYear(),
        "month": date.getMonth() + 1,
        "day": day
    };
    event_data["events"].push(event);
}

function show_events(events, month, day) {
    var eventsContainer = document.getElementsByClassName("events-container")[0];
    eventsContainer.innerHTML = "";
    eventsContainer.style.display = "block";
    if (events.length === 0) {
        var event_card = document.createElement("div");
        event_card.className = "event-card";
        var event_name = document.createElement("div");
        event_name.className = "event-name";
        event_name.textContent = "There are no events planned for " + month + " " + day + ".";
        event_card.style.borderLeft = "10px solid #FF1744";
        event_card.appendChild(event_name);
        eventsContainer.appendChild(event_card);
    } else {
        for (var i = 0; i < events.length; i++) {
            var event_card = document.createElement("div");
            event_card.className = "event-card";
            var event_name = document.createElement("div");
            event_name.className = "event-name";
            event_name.textContent = events[i]["occasion"] + ":";
            var event_count = document.createElement("div");
            event_count.className = "event-count";
            event_count.textContent = events[i]["invited_count"] + " Invited";
            if (events[i]["cancelled"] === true) {
                event_card.style.borderLeft = "10px solid #FF1744";
                event_count = document.createElement("div");
                event_count.className = "event-cancelled";
                event_count.textContent = "Cancelled";
            }
            event_card.appendChild(event_name);
            event_card.appendChild(event_count);
            eventsContainer.appendChild(event_card);
        }
    }
}

function check_events(day, month, year) {
    var events = [];
    for (var i = 0; i < event_data["events"].length; i++) {
        var event = event_data["events"][i];
        if (event["day"] === day && event["month"] === month && event["year"] === year) {
            events.push(event);
        }
    }
    return events;
}

var event_data = {
    "events": [
        {
            "occasion": " Repeated Test Event ",
            "invited_count": 120,
            "year": 2020,
            "month": 5,
            "day": 10,
            "cancelled": true
        },
        {
            "occasion": " Repeated Test Event ",
            "invited_count": 120,
            "year": 2020,
            "month": 5,
            "day": 10,
            "cancelled": true
        },
        {
            "occasion": " Repeated Test Event ",
            "invited_count": 120,
            "year": 2020,
            "month": 5,
            "day": 10,
            "cancelled": true
        },
        {
            "occasion": " Repeated Test Event ",
            "invited_count": 120,
            "year": 2020,
            "month": 5,
            "day": 10
        },
        {
            "occasion": " Repeated Test Event ",
            "invited_count": 120,
            "year": 2020,
            "month": 5,
            "day": 10,
            "cancelled": true
        },
        {
            "occasion": " Repeated Test Event ",
            "invited_count": 120,
            "year": 2020,
            "month": 5,
            "day": 10
        },
        {
            "occasion": " Repeated Test Event ",
            "invited_count": 120,
            "year": 2020,
            "month": 5,
            "day": 10,
            "cancelled": true
        },
        {
            "occasion": " Repeated Test Event ",
            "invited_count": 120,
            "year": 2020,
            "month": 5,
            "day": 10
        },
        {
            "occasion": " Repeated Test Event ",
            "invited_count": 120,
            "year": 2020,
            "month": 5,
            "day": 10,
            "cancelled": true
        },
        {
            "occasion": " Repeated Test Event ",
            "invited_count": 120,
            "year": 2020,
            "month": 5,
            "day": 10
        },
        {
            "occasion": " Test Event",
            "invited_count": 120,
            "year": 2020,
            "month": 5,
            "day": 11
        }
    ]
};

const months = [
    "January", 
    "February", 
    "March", 
    "April", 
    "May", 
    "June", 
    "July", 
    "August", 
    "September", 
    "October", 
    "November", 
    "December"
];
