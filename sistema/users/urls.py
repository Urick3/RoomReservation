from django.urls import path
from .views import *

urlpatterns = [
    path('index', , name='index'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('manager', manager_page, name="dash_manager"),
    path('teacher', teacher_page, name="dash_teacher"),
    path('request', , name="request"),
    path('total/request', , name="total_request"),
    path('users/list', , name='user_list'),
    path('profile', , name='profile'),
]