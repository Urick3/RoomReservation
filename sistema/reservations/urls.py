from django.urls import path
from .views import *

urlpatterns = [
    path('calendar/', calendar_teacher, name='calender'),
    path('calendar/manager/', calendar_manager, name='calendar_manager'),
    path('pending/requests/', pending_requests, name='requests_pending'),
    path('total/request/', all_requests, name='total_request'),
    path('requests/', requests, name='requests'),
    path('horas/', hours, name='hours')

]