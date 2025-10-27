from django.shortcuts import redirect, get_object_or_404,render
from .models import Tasks

# Create your views here.
def addTask(request):
    task=request.POST.get("task")
    Tasks.objects.create(task=task)
    return redirect("home")


def markComplete(request, pk):
    task = get_object_or_404(Tasks, pk=pk)
    task.is_completed = True
    task.save()
    return redirect("home")

def markNotComplete(request, pk):
    task = get_object_or_404(Tasks, pk=pk)
    task.is_completed = False
    task.save()
    return redirect("home")

def deleteTask(request, pk):
    task = get_object_or_404(Tasks, pk=pk)
    task.delete()
    return redirect("home")

def editTask(request, pk):
    task = get_object_or_404(Tasks, pk=pk)
    if request.method == "POST":
        new_task = request.POST.get("task")
        task.task = new_task
        task.save()
        return redirect("home")
    return render(request, "edit.html", {"task": task})