from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', CustomLoginView.as_view(), name='index'),#ok
    path('login/', CustomLoginView.as_view(), name='login'),#ok
    path('logout/', LogoutView.as_view(), name='logout'),#ok
    path('dashboard/gerente/', DashboardManagerPage.as_view(), name="manager_dashboard"),#ok
    path('dashboard/docente/', DashboardTeacherPage.as_view(), name="teacher_dashboard"),#ok
    path('listar/usuarios/', UserListView.as_view(), name='user_list'),#ok
    path('adicionar/usuarios/', UserCreateView.as_view(), name='user_add'),#ok
    path('editar/usuario/<int:pk>/', UserUpdateView.as_view(), name='user_edit'),#ok
    path('deletar/ususario/<int:pk>/', UserDeleteView.as_view(), name='user_delete'),#ok
    path('profile', profile, name='profile'),

    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]