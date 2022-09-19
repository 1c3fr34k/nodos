from django.db import models

class Note(models.Model):
    title = models.TextField(max_length=150)
    description = models.CharField(max_length=2000, blank=True, null=True)
    done = models.BooleanField(default=False, blank=True)