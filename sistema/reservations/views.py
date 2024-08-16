from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
from .service import ReservationService
from .models import Room

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

# @login_required(login_url='/login/')
# @api_view(['GET'])
# def check_available_hours(request, room_id, date):
#     try:
#         room = Room.objects.get(id=room_id)
#         available_hours = ReservationService.list_available_hours_for_date(room, date)
#         return Response({
#             'available_hours': list(available_hours.values('id', 'range_hour'))
#         })
#     except Room.DoesNotExist:
#         return Response({'error': 'Room not found'}, status=404)

