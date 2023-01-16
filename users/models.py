from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class UserFunction(models.TextChoices):
    COZI = "Cozinheiro"
    CAIXA = "Caixa"
    ENTRE = "Entregador"
    SERV_GER = "Serviços Gerais"
    GER = "Gerente"
    ADM = "Administrador"


class User(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=127, unique=True)
    function = models.CharField(max_length=50, choices=UserFunction.choices)
    cpf = models.CharField(max_length=11, unique=True)
    isActive = models.BooleanField(default=True)
    orders_attended = models.IntegerField(null=True, default=0)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    business = models.ForeignKey(
        "business.Business", on_delete=models.CASCADE, related_name="users"
    )
