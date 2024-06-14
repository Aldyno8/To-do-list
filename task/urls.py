from django.urls import path
from . import views

urlpatterns = [
    path('Tuned/', views.home, name='home'),
    path('', views.task_listing, name='list'),
    path('add/', views.add_task, name='add'),
    path('edit/<int:task_id>/', views.edit_task, name='edit'),
    path('delete/<int:task_id>/', views.delete_task, name='delete')
    
]
