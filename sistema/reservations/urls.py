from django.urls import path
from .views import *

urlpatterns = [
    path('calendar/', calendar_teacher, name='calender'),
    path('calendar_manager', calendar_manager, name='request_pending'),
    path('requests/', pending_requests, name='requests_pending'),
    path('total_request/', all_requests, name='total_request')

]