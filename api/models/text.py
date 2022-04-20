from email.quoprimime import body_check
from django.db import models
from django.contrib.auth import get_user_model

class Text(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=5000)
    attribution = models.CharField(max_length=100)
    tags = models.JSONField()
    owner = models.ForeignKey(
        get_user_model(),
        # if user is deleted, text items get deleted
        on_delete=models.CASCADE
    )