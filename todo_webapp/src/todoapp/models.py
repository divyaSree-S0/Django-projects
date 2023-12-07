from django.db import models
# Create your models here.
class ToDoListItems(models.Model):
    content=models.TextField()

