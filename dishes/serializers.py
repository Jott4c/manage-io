from rest_framework import serializers
from .models import Dish, IngredientsToDish


class IngredientsToDishSerializer(serializers.ModelSerializer):
    class Meta:
        model = IngredientsToDish
        fields = [
            "id",
            "name",
            "quantity",
            "measurement",
        ]


class DishSerializer(serializers.ModelSerializer):
    ingredients = IngredientsToDishSerializer(many=True)

    class Meta:
        model = Dish
        fields = [
            "id",
            "name",
            "price",
            "image",
            "description",
            "ingredients",
            "orders_num",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["orders_num"]

    def create(self, validated_data):
        ingredients_list = validated_data.pop("ingredients")

        dish_dict = Dish.objects.create(**validated_data)

        for ingredient in ingredients_list:
            ingredient_dict = IngredientsToDish.objects.create(**ingredient)

            ingredient_dict.dishes.add(dish_dict)

        return dish_dict
