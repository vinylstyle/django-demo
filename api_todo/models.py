from django.db import models

class Todo(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField()

    class Meta:
        ordering = ['created']