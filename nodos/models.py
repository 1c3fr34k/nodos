from django.db import models


class Note(models.Model):
    title = models.TextField(max_length=150)
    description = models.CharField(max_length=2000, blank=True, null=True)
    done = models.BooleanField(default=False, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    last_edited = models.DateTimeField(auto_now=True)
