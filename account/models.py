from django.db import models
from django.db.models.fields import CharField

class TodoList(models.Model):
    work = CharField(max_length=100)

    def __str__(self):
        return f"{self.work} in ToDo"
