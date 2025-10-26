
from django.urls import path,include
from . import views

urlpatterns = [
  path("addTask/",views.addTask, name="addTask"),
  path("markComplete/<int:pk>/",views.markComplete, name="markComplete"),
  path("markNotComplete/<int:pk>/",views.markNotComplete, name="markNotComplete"),
  path("deleteTask/<int:pk>/",views.deleteTask, name="deleteTask"),
  
]