from django.db import models
from django.conf import settings
from django.utils import timezone


class Board(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(default=timezone.now)

