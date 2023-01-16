from django.db import models
import uuid


class MeasurementChoices(models.TextChoices):
    UN = "unidade"
    GR = "gramas"


class Ingredients(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=50, unique=True)
    quantity = models.IntegerField()
    price = models.FloatField()
    measurement = models.CharField(
        max_length=100,
        choices=MeasurementChoices.choices,
    )
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
