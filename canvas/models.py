from django.db import models
from django.utils import timezone


class CanvasData(models.Model):
    id = models.AutoField(primary_key=True)
    data = models.TextField(blank=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Check(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.TextField(blank=False, unique=True)
    end_time = models.DateTimeField(default=timezone.now() + timezone.timedelta(minutes=3))
