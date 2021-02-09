from django.db import models
from django.forms import ModelForm, TextInput, Textarea

# Create your models here.

class Task(models.Model):

    title = models.CharField('naming', max_length=50)
    text = models.TextField('description')

    def __str__(self):
        return self.title

    class Meta:

        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'text']
        widgets = {
            'title' : TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'name of hueta'
            }
            ),
            'text' : Textarea(attrs={
                'class' : 'form-control',
                'placeholder' : 'content of hueta'
            }
            )

        }
