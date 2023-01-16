from rest_framework import serializers
from .models import Business
from users.serializers import UserSerializer


class BusinessSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Business
        fields = [
            "id",
            "business_name",
            "cpnj",
            "email",
            "created_at",
            "isActive",
            "users",
        ]
