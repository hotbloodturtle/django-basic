from django.db import models
from django.conf import settings


class Board(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    photo = models.ImageField(blank=True, upload_to="boards/%Y/%m/%d", null=True)
    created_at = models.DateTimeField(auto_now_add=True)
