from django.urls import path
from .views import *

urlpatterns = [
    path('check-availability/<int:room_id>/<str:date>/', check_available_hours, name='check-availability'),

]