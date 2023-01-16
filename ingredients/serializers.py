from rest_framework import serializers
from .models import Ingredients


class IngredientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients
        fields = [
            "id",
            "name",
            "price",
            "quantity",
            "measurement",
            "created_at",
            "updated_at",
        ]
