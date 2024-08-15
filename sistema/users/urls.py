from django.urls import path
from .views import *

urlpatterns = [
    path('index', index, name='index'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('manager', manager_page, name="dash_manager"),
    path('teacher', teacher_page, name="dash_teacher"),
    path('users/list', users_list, name='user_list'),
    path('profile', profile, name='profile'),
]