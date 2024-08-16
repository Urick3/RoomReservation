from django.urls import path
from .views import *

urlpatterns = [
    path('calendario/', CalendarReservation.as_view(), name='calendar'),#ok
    path('docentes/', ListReservation.as_view(), name='requests'),#ok
    path('pendentes/', ListReservationPending.as_view(), name='requests_pending'),#ok
    path('solicitacao/<int:id>/', ManageSolicitationView.as_view(), name='manage_solicitation'),
    path('calendar/manager/', calendar_manager, name='calendar_manager'),
    
    path('total/request/', all_requests, name='total_request'),
    
    path('horas/', hours, name='hours'),

]