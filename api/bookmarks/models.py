from django.db import models
from django.contrib.auth.models import User

class Bookmark(models.Model):
    name = models.CharField(max_length=75)
    URL = models.URLField()
    date_created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE) 

    def __str__(self):
        return self.name