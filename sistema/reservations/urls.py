from django.urls import path
from .views import *

urlpatterns = [
    path('calendario/', CalendarReservation.as_view(), name='calendar'),#ok
    path('docentes/', ListReservation.as_view(), name='requests'),#ok
    path('pendentes/', ListReservationPending.as_view(), name='requests_pending'),#ok
    path('solicitacao/<int:id>/', ManageSolicitationView.as_view(), name='manage_solicitation'),#ok
    path('calendario/gestor/', CalendarManagerReservation.as_view(), name='calendar_manager'),#ok
    path('dashboard/', DashboardRequestPageView.as_view(), name="request_dashboard"),#ok
    path('total/request/', all_requests, name='total_request'),
    
    path('horas/', hours, name='hours'),

]