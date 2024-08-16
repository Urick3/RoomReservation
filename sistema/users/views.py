from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from .decorators import *
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .service import UserService
from .forms import *



class CustomLoginView(View):
    form_class = EmailLoginForm
    template_name = 'users/login.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                if user.user_type == 'teacher':
                    return redirect('teacher_dashboard') 
                elif user.user_type == 'manager':
                    return redirect('manager_dashboard')  
            else:
                form.add_error(None, "Email ou senha incorretos")
        return render(request, self.template_name, {'form': form})

@method_decorator(user_is_manager, name='dispatch')
class UserListView(ListView):
    template_name = 'users/manager/user_list.html'
    context_object_name = 'users'
    paginate_by = 10

    def get_queryset(self):
        page = self.request.GET.get('page', 1)
        users = UserService.list_all_users(page=page, per_page=self.paginate_by)
        return users


@method_decorator(user_is_manager, name='dispatch')
class UserCreateView(CreateView):
    template_name = 'users/manager/user_register.html'
    form_class = UserForm
    success_url = reverse_lazy('user_list')

    def form_valid(self, form):
        return super().form_valid(form)

@method_decorator(user_is_manager, name='dispatch')
class UserUpdateView(UpdateView):
    template_name = 'users/manager/user_register.html'
    form_class = UserForm
    success_url = reverse_lazy('user_list')

    def get_object(self):
        user_id = self.kwargs['pk']
        return UserService.get_user_details(user_id)

    def form_valid(self, form):
        UserService.update_existing_user(self.object.id, **form.cleaned_data)
        return super().form_valid(form)

@method_decorator(user_is_manager, name='dispatch')    
class UserDeleteView(DeleteView):
    success_url = reverse_lazy('user_list')  # Redirecionar após exclusão

    def get_object(self):
        user_id = self.kwargs['pk']
        return UserService.get_user_details(user_id)

    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        UserService.delete_user(user.id)
        return super().delete(request, *args, **kwargs)


def profile(request):
    return render(request, 'users/profile.html')

@user_is_teacher
def teacher_page(request):
    return render(request, 'users/teacher/dashboard.html')

@user_is_manager
def manager_page(request):
    return render(request, 'users/manager/dashboard.html')



