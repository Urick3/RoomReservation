from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views import View
from reservations.service import ReservationService, HourService
from users.decorators import *
from rooms.service import RoomService
from datetime import datetime

@method_decorator(user_is_teacher, name='dispatch')
class CalendarReservation(View):
    
    def get(self, request, *args, **kwargs):
        rooms = RoomService.get_all_rooms()
        
        return render(request, 'reservations/calendar.html', {'rooms': rooms})
    
    def post(self, request, *args, **kwargs):
        room = request.POST.get('room')
        hours = request.POST.getlist('hours')  
        date = request.POST.get('date')
        date_american = datetime.strptime(date, "%d/%m/%Y")

        if room  != None:
            room = RoomService.get_room_details(room)

        for hour in hours:
            hour = HourService.get_hour_id_by_range(hour)
            ReservationService.create_new_reservation(room, request.user, hour, date_american)
        
        return redirect('calendar')
    

@method_decorator(user_is_teacher, name='dispatch')
class ListReservation(View):
    
    def get(self, request, *args, **kwargs):
        reservas = ReservationService.get_user_reservations(request.user,request.GET.get('page', 1),20)
        
        return render(request, 'reservations/requests.html', {'reservas': reservas})
    
    def post(self, request, *args, **kwargs):
        pass



def calendar_manager(request):
    return render(request, 'reservations/calendar_ges.html')


def all_requests(request):
    return render(request, 'reservations/total_request.html')

def pending_requests(request):
    return render(request, 'reservations/request_pending.html')

def requests(request):
    return render(request, 'reservations/requests.html')

def hours(request):
    return render(request, 'reservations/hours.html')



