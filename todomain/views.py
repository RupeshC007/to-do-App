from django.shortcuts import render 
from todos.models import Tasks

def home(request):
    tasks=Tasks.objects.filter(is_completed=False).order_by('-created_at')
    completed_tasks=Tasks.objects.filter(is_completed=True).order_by('-created_at')
    context={'tasks':tasks,
             'completed_tasks':completed_tasks}
    return render(request, "./home.html",context)