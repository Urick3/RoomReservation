from django.shortcuts import render

# Create your views here.
def index(request):
    pass

def login_view(request):
    return render(request, 'users/login.html')

def profile(request):
    return render(request, 'users/profile.html')

def teacher_page(request):
    return render(request, 'users/teacher/dashboard.html')

def manager_page(request):
    return render(request, 'users/manager/dashboard.html')

def register_user(request):
    return render(request, 'users/manager/register_user.html')

def users_list(request):
    return render(request, 'users/manager/users_list.html')

def logout_view(request):
    pass

def register_view(request):
    pass