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
        
    # fonction qui va faire la validation personalisée
    # Verifie si la date d'écheance de la tache est ultérieur à la date d'éxecution
        
    def clean(self):
        cleaned_data = super().clean()
        start = cleaned_data.get('schedule_date')
        end = cleaned_data.get('due_date')
        
        if start and end and start > end :
            self.add_error('due_date', "La date d'écheance doit etre antérieur à la date d'éxécution")
        return cleaned_data
        