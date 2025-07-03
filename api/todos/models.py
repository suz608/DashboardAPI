from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    text = models.CharField(max_length=254)
    date_created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE) 

    def __str__(self):
        return self.text