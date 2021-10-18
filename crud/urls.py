from django.urls import path
from crud import views
from .views import TaskList,TaskDetail,TaskCreate,TaskUpdate,TaskDelete,LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
from .forms import LoginForm

urlpatterns = [
    path('login/', LoginView.as_view(),name='login'),
    path('login/',auth_views.LoginView.as_view(template_name='crud/login.html',authentication_form=LoginForm), name='login'),
    path('registration/',views.CustomerRegistrationView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page='login'),name='logout'),
    path('', TaskList.as_view(),name='tasklist'),
    path('taskcreate/', TaskCreate.as_view(),name='taskcreate'),
    path('taskupdate/<int:pk>/', TaskUpdate.as_view(),name='taskupdate'),
    path('taskdetail/<int:pk>/', TaskDetail.as_view(),name='detail'),
    path('taskdelete/<int:pk>/', TaskDelete.as_view(),name='taskdelete')

]  