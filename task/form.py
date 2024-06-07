from task.models import Task
from django import forms

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'schedule_date', 'due_date', 'description',] 
        widgets = {
            'name': forms.TextInput(attrs={'placeholder':'Name of the task'}),
            'description': forms.Textarea(attrs={'placeholder':'Desciption of the task'}),
            'schedule_date': forms.DateInput(attrs={'type':'date'}),
            'due_date': forms.DateInput(attrs={'type':'date'})
        }
        