from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class UserSerializer(serializers.ModelSerializer):
    orders_attended = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            "id",
            "name",
            "password",
            "function",
            "cpf",
            "username",
            "email",
            "created_at",
            "updated_at",
            "business",
            "orders_attended",
            "isActive",
        ]
        extra_kwargs = {"password": {"write_only": True}}
        read_only_fields = ["orders_attended"]

    def get_orders_attended(self, obj):
        return obj.orders.count()

    def create(self, validated_data: dict) -> User:
        if (
            validated_data["function"] == "Administrador"
            or validated_data["function"] == "Gerente"
        ):
            return User.objects.create_superuser(**validated_data)

        return User.objects.create_user(**validated_data)

    def update(self, instance: User, validated_data: dict) -> User:
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance
