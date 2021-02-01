from django.db import models

# Create your models here.

class Task(models.Model):

    title = models.CharField('naming', max_length=50)
    text = models.TextField('description')

    def __str__(self):
        return self.title

    class Meta:

        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
