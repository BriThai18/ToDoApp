from base.decorators import unauthenticated_user
from typing import ContextManager
from django.shortcuts import redirect, render
from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required

from .models import Task
from .forms import TaskForm
from .decorators import unauthenticated_user
# Create your views here.

@unauthenticated_user
def registerPage(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account was created successfully")
            return redirect('/login')
    context = {'form' : form}
    return render(request, 'base/register.html', context)

@unauthenticated_user
def loginPage(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request = request, data = request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
   
    context = {'form': form}
    return render(request, 'base/login.html', context)

def logoutPage(request):
    logout(request)
    messages.info(request, "Logged out sucessfully")
    return redirect('login')

@login_required(login_url='login')
def taskList(request):
    tasks = Task.objects.filter(user=request.user)
    context = {'tasks' : tasks}
    return render(request, 'base/taskList.html', context)

@login_required(login_url='login')
def task(request, id):
    task  = Task.objects.get(id=id)
    context = {'task' : task}
    return render(request, 'base/task.html', context)

@login_required(login_url='login')
def taskCreate(request):
    form = TaskForm()

    if request.method == 'POST':
        #Create value
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('/')
        else:
            form = TaskForm()

    return render(request, 'base/task_form.html', {'form': form})

@login_required(login_url='login')
def updateTask(request, id):
    task = Task.objects.get(id=id)

    #Get instance of the specific task
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form' : form}
    return render(request, 'base/update_task.html', context)

@login_required(login_url='login')
def deleteTask(request, id):
    task = Task.objects.get(id=id)

    if request.method == 'POST':
        task.delete()
        return redirect('/')

    context = {'task' : task}
    return render(request, 'base/delete.html', context)