from django.contrib import admin
from task.models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_date')


# Register your models here.
admin.site.register(Task, TaskAdmin)