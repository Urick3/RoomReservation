from django.urls import path
from .views import *

urlpatterns = [
    path('calendario/', CalendarReservation.as_view(), name='calendar'),
    path('docentes/', ListReservation.as_view(), name='requests'),
    path('calendar/manager/', calendar_manager, name='calendar_manager'),
    path('pending/requests/', pending_requests, name='requests_pending'),
    path('total/request/', all_requests, name='total_request'),
    
    path('horas/', hours, name='hours'),

]