from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views import View
from reservations.service import ReservationService, HourService, ReservationApprovalService
from users.service import UserService
from users.decorators import *
from rooms.service import RoomService
from datetime import datetime

@method_decorator(user_is_teacher, name='dispatch')
class CalendarReservation(View):
    
    def get(self, request, *args, **kwargs):
        rooms = RoomService.get_all_rooms()
        
        return render(request, 'reservations/calendar_teacher.html', {'rooms': rooms})
    
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
        
        return render(request, 'reservations/request_teacher.html', {'reservas': reservas})
    
    def post(self, request, *args, **kwargs):
        pass

@method_decorator(user_is_manager, name='dispatch')
class ListReservationPending(View):
    
    def get(self, request, *args, **kwargs):
        reservas = ReservationService.list_pending_reservations_all(request.GET.get('page', 1),20)
        
        return render(request, 'reservations/request_pending.html', {'reservas': reservas})
    
    def post(self, request, *args, **kwargs):
        pass

@method_decorator(user_is_manager, name='dispatch')
class ManageSolicitationView(View):
    
    def post(self, request, *args, **kwargs):
        solicitation_id = kwargs.get('id')
        action = request.POST.get('action')
 
        solicitation = ReservationService.get_reservation_details(solicitation_id)
        if solicitation is None:
            return redirect('requests_pending')

        # Verifica a ação e atualiza o status
        if action == 'approved':
            ReservationService.approved_or_rejected_reservation(solicitation.id, request.user, 'approved')
        elif action == 'rejected':
            ReservationService.approved_or_rejected_reservation(solicitation.id, request.user, 'rejected') 
        else:
            return redirect('requests_pending')  

        return redirect('requests_pending')


@method_decorator(user_is_manager, name='dispatch')
class CalendarManagerReservation(View):
    
    def get(self, request, *args, **kwargs):
        rooms = RoomService.get_all_rooms()
        users = UserService.get_all_users()
        return render(request, 'reservations/calendar_manager.html', {'rooms': rooms, 'users': users})
    
    def post(self, request, *args, **kwargs):
        room = request.POST.get('room')
        hours = request.POST.getlist('hours')  
        date = request.POST.get('date')
        teacher = UserService.get_user_details(request.POST.get('teacher'))
        date_american = datetime.strptime(date, "%d/%m/%Y")

        if room  != None:
            room = RoomService.get_room_details(room)

        for hour in hours:
            hour = HourService.get_hour_id_by_range(hour)
            reservation = ReservationService.create_new_reservation(room, teacher, hour, date_american, 'approved')
            ReservationApprovalService.create_new_approval(reservation, manager=request.user, status='approved')
        
        return redirect('calendar_manager')

@method_decorator(user_is_manager, name='dispatch')
class DashboardRequestPageView(View):
    template_name = 'reservations/dashboard_request.html'





def all_requests(request):
    return render(request, 'reservations/total_request.html')

def hours(request):
    return render(request, 'reservations/hours.html')



