from django.shortcuts import render,redirect
from .forms import TaskForm
from . import models
# Create your views here.
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm()    
    return render(request,'task.html',{'form':form})

def edit_task(request, id):
    task = models.Task.objects.get(pk=id)
    task_form = TaskForm(instance=task)
    if request.method == 'POST':
        task_form = TaskForm(request.POST, instance=task)
        if task_form.is_valid():
            task_form.save()
            return redirect('home')   
    return render(request,'task.html',{'form':task_form})

def delete_task(request, id):
    task = models.Task.objects.get(pk=id)
    task.delete()
    return redirect('home')