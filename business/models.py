from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class Business(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    business_name = models.CharField(max_length=50)
    cpnj = models.CharField(max_length=14, unique=True)
    email = models.EmailField(max_length=127, unique=True)
    created_at = models.DateField(auto_now_add=True)
    isActive = models.BooleanField(default=True)
