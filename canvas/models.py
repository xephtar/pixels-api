from django.db import models


class CanvasData(models.Model):
    id = models.AutoField(primary_key=True)
    data = models.TextField(blank=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
