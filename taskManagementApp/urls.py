from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<list_id>/', views.delete, name='delete'),
    path('tasks/<str:pk_test>/', views.tasks, name='tasks')
]
