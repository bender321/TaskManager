from django.views.generic.edit import CreateView, UpdateView, FormView
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from .models import Task


class CustomLoginView(LoginView):
    """
        Class based view that takes care of
        login an existing user.
    """
    template_name = 'taskmanager/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('users')


class RegisterView(FormView):
    """
        Class based view that takes care of
        registration of new user.
    """
    template_name = 'taskmanager/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('users')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterView, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('users')
        return super(RegisterView, self).get(*args, **kwargs)


class TaskDetail(DetailView):
    """
        Class based view that takes care of
        showing details of one specific task.
    """
    model = Task
    context_object_name = 'task-detail'


class TaskCreate(CreateView):
    """
        Class based view that takes care of
        creation of new task-record in database.
    """
    model = Task
    context_object_name = 'task-create'
    fields = '__all__'
    success_url = reverse_lazy('task-create')
    template_name = 'taskmanager/task_create_form.html'


class TaskUpdate(UpdateView):
    """
        Class based view that takes care of
        updating task-records in database.
    """
    model = Task
    context_object_name = 'update'
    fields = ['completed']
    success_url = reverse_lazy('users')


class ListUsers(ListView):
    """
        Class based view that takes care of
        listing all users registered users from database.
    """
    model = User
    template_name = 'taskmanager/myusers_list.html'
    context_object_name = 'users'


def list_tasks(request, idd):
    """
        View function that takes care of
        listing of all task from selected user.

        :param request: Any
        :param idd: int
        :return: render(request, url, context)
    """
    res = Task.objects.all().filter(user=idd)
    url = 'taskmanager/task_list.html'
    context = {'tasks': res}
    return render(request, url, context)
