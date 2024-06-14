from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from task.models import Task
from django.template import Template, Context
from task.form import TaskForm


# Create your views here.
def home(request):
    return HttpResponse("Hacking is a passion, not a crime. PiR@T£S")

# Affiche la liste des taches 
def task_listing(request):
    tasks = Task.objects.all().order_by('due_date')
    return render(request, 'list_task.html', {'tasks': tasks})

# Redirige vers une formulaire d'ajout de tache et ajoute la tache dans une base de donées si le formulaire est soumis via la methode post
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list') 

    else:
        form = TaskForm()
    return render(request, 'new_task.html', {'form': form})

# récupère l'id d'une tache pour pouvoir la modifier ensuite
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance = task)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'edit_task.html', {'form':form})

# Supprimer une tache
def delete_task(request, task_id):
   task = get_object_or_404(Task, id=task_id)
   task.delete()
   return redirect('list')
    

