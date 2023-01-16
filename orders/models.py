from django.db import models


class PayMethod(models.TextChoices):
    CR = "credit"
    DB = "debit"
    CH = "cash"
    PX = "pix"


class StatusOrder(models.TextChoices):
    OPEN = "open"
    DOING = "doing"
    DELIVERED = "delivered"
    CANCELED = "canceled"


class Order(models.Model):
    table = models.CharField(null=True, max_length=50)
    total = models.FloatField()
    dishes_info = models.CharField(max_length=3000, null=True)
    pay_method = models.CharField(
        max_length=50,
        choices=PayMethod.choices,
    )
    delivery = models.BooleanField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    order_status = models.CharField(
        max_length=50, choices=StatusOrder.choices, default=StatusOrder.OPEN
    )

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="orders",
    )

    client = models.ForeignKey(
        "clients.Client",
        on_delete=models.CASCADE,
        related_name="orders",
        null=True,
    )

    dishes = models.ManyToManyField("dishes.Dish", related_name="orders")
