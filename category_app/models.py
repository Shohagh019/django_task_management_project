from django.db import models
from task_app.models import Task
# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=20)
    task_name = models.ManyToManyField(Task, related_name="categories", blank=True)

    def __str__(self):
        return self.category_name