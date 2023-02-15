from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.http import JsonResponse
from django.forms.models import model_to_dict
# Create your views here.
def task(request):
    tasks = Task.objects.all()
    form = TaskForm(request.POST)
    if form.is_valid():
       new_task = form.save()
       return JsonResponse({'task': model_to_dict(new_task)}, status=200)
    
    return render(request, 'task_list.html', {'form': form, 'tasks': tasks})


def taskComplete(request, id):
    tasks = Task.objects.get(id=id)
    tasks.completed = True
    tasks.save()
    return JsonResponse({'task': model_to_dict(tasks)}, status=200)


def taskDelete(request, id):
    tasks = Task.objects.get(id=id)
    tasks.delete()
    return JsonResponse({'result': 'ok'}, status=200)
