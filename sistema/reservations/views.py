from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


# Create your views here.
def calendar_manager(request):
    return render(request, 'reservations/calendar_ges.html')

def calendar_teacher(request):
    return render(request, 'reservations/calendar.html')

def all_requests(request):
    return render(request, 'reservations/total_request.html')

def pending_requests(request):
    return render(request, 'reservations/request_pending.html')

def requests(request):
    return render(request, 'reservations/requests.html')

def hours(request):
    return render(request, 'reservations/hours.html')



