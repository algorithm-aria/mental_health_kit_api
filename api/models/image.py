from django.db import models
from django.contrib.auth import get_user_model

class Image(models.Model):
    title = models.CharField(max_length=100)
    image_url = models.CharField(max_length=500)
    tags = models.JSONField()
    owner = models.ForeignKey(
        get_user_model(),
        # if user is deleted, text items get deleted
        on_delete=models.CASCADE
    )