from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('List/', views.task_listing, name='list'),
    path('add/', views.add_task, name='add'),
    path('edit/<int:task_id>/', views.edit_task, name='edit')
]
