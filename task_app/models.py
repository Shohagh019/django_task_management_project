from django.db import models

# Create your models here.
class Task(models.Model):
    task_title = models.CharField(max_length=20)
    task_description = models.TextField()
    is_complete = models.BooleanField(default=False)
    task_assign_date = models.DateField()
    def __str__(self):
        return f'{self.task_title}'