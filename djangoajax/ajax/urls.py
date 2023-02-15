from django.urls import path
from . import views

urlpatterns = [
    path('', views.task, name="task"),
    path('<str:id>/completed/', views.taskComplete, name='task_completed' ),
    path('<str:id>/delete/', views.taskDelete, name='task_delete' ),
]
