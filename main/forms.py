from .models import Task
from django.forms import ModelForm, TextInput, Textarea


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task"]
        widgets = {
            "title": TextInput(attrs={
                'placeholder': "Введите название",
            #  'class': "class name",
            }),
            "task": Textarea(attrs={
                'placeholder': "Введите Описание",
            })
        }