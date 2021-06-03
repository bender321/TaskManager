from .views import list_tasks, TaskDetail, TaskCreate, \
    TaskUpdate, CustomLoginView, RegisterView, ListUsers

from django.contrib.auth.views import LogoutView
from django.urls import path


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),

    path('', ListUsers.as_view(), name='users'),
    path('/<idd>', list_tasks, name='tasks'),
    path('task-detail<int:pk>/', TaskDetail.as_view(), name='task-detail'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-edit<int:pk>/', TaskUpdate.as_view(), name='task-edit'),
]
