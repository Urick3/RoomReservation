from django.urls import path
from .views import *

urlpatterns = [
    path('calender/', , name='calender'),
    path('request_pending',, name='request_pending'),
    path('requests/', , name='requests'),
    path('total_request/', , name='total_request')

]