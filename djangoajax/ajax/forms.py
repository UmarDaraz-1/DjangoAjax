from django import forms 
from . models import *

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'})
        }