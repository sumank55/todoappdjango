from django.shortcuts import render,redirect
from .models import Task
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, FormView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import CustomerRegistrationsForms
from django.contrib import messages
from django.views import View






class CustomerRegistrationView(View):
    def get(self,request):
        form = CustomerRegistrationsForms()
        return render(request,'crud/register.html',{'form':form})

    def post(self,request):
        form=CustomerRegistrationsForms(request.POST,request.FILES) 
        form.profile_image = request.FILES['profile_image']  
        if form.is_valid():
            form.save()
            # messages.success(request,'Registration successfully')
            return redirect('tasklist')
        return render(request,'crud/register.html',{'form':form})     


class LoginView(LoginView):
    template_name='crud/login.html'
    fields='__all__'
    redirect_authenticated_user=True

    def get_success_url(self):
        return reverse_lazy('tasklist')

   
class TaskList(LoginRequiredMixin,ListView):
    model = Task
    context_object_name = 'tasks'
    def get_context_data(self, **kwargs,):
        context = super().get_context_data(**kwargs)
        context['tasks']=Task.objects.filter(user=self.request.user).exists()
        context['count']=Task.objects.filter(complete=False).count()
        search_input=self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks']=context['tasks'].filter(title__startswith = search_input)
        context['search_input'] = search_input
        return context

 
class TaskDetail(LoginRequiredMixin,DetailView):
    model = Task
    context_object_name = 'task'
    template_name='crud/task.html'
    
class TaskCreate(LoginRequiredMixin,CreateView):
    model=Task
    fields= ['title','description','complete']
    success_url=reverse_lazy('tasklist')

    def form_valid(self,form):
        form.instance.user=self.request.user
        return super(TaskCreate,self).form_valid(form)

class TaskUpdate(LoginRequiredMixin,UpdateView):
    model =Task
    fields= ['title','description','complete']
    success_url=reverse_lazy('tasklist')

class TaskDelete(LoginRequiredMixin,DeleteView):
    model =Task
    context_object_name = 'task'
    success_url=reverse_lazy('tasklist')

