from django.db import models
import uuid
from ingredients.models import MeasurementChoices
from orders.models import Order


class DishIngredient(models.Model):
    dish = models.ForeignKey("dishes.Dish", on_delete=models.CASCADE)
    ingredient = models.ForeignKey("dishes.IngredientsToDish", on_delete=models.CASCADE)


class IngredientsToDish(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    measurement = models.CharField(
        max_length=100,
        choices=MeasurementChoices.choices,
    )


class Dish(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=250)
    price = models.FloatField()
    image = models.CharField(max_length=250, null=True)
    orders_num = models.IntegerField(null=True, default=0)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    ingredients = models.ManyToManyField(
        IngredientsToDish,
        related_name="dishes",
        through=DishIngredient,
    )
