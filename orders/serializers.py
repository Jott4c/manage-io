from django.forms import model_to_dict
from rest_framework import serializers
from .models import Order
from dishes.serializers import DishSerializer
from users.serializers import UserSerializer
from ingredients.models import Ingredients
import ipdb
from dishes.models import Dish
from users.models import User


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            "id",
            "table",
            "total",
            "pay_method",
            "delivery",
            "created_at",
            "order_status",
            "updated_at",
            "user",
            "client",
            "dishes",
            "dishes_info",
        ]
        read_only_fields = ["total"]
        extra_kwargs = {"dishes": {"write_only": True}}

    def create(self, validated_data):

        user_order = validated_data["user"]
        new_num_user = user_order.orders.count() + 1
        setattr(user_order, "orders_attended", new_num_user)
        User.save(user_order)

        dishes_list = validated_data.pop("dishes")
        valor = [dish.price for dish in dishes_list]
        total = sum(valor)

        dishes_info = [
            {"id": info.id, "name": info.name, "price": info.price}
            for info in dishes_list
        ]

        order_dict = Order.objects.create(
            **validated_data, total=total, dishes_info=dishes_info
        )

        unique_list = list(set(dishes_list))

        for dishes in unique_list:

            new_num = dishes.orders_num + dishes_list.count(dishes)
            setattr(dishes, "orders_num", new_num)
            Dish.save(dishes)
            order_dict.dishes.add(dishes)

            dishes = model_to_dict(dishes)
            ingredients = dishes.pop("ingredients")
            ingredients_list = [model_to_dict(ingredient) for ingredient in ingredients]

            for ingredient in ingredients_list:

                ingredient_dict = Ingredients.objects.get(name=ingredient["name"])
                valor = (
                    model_to_dict(ingredient_dict)["quantity"] - ingredient["quantity"]
                )
                setattr(ingredient_dict, "quantity", valor)
                ingredient_dict.save()

        return order_dict


class OrderGetSerializer(serializers.ModelSerializer):
    dishes = DishSerializer(many=True)
    user = UserSerializer()

    class Meta:
        model = Order
        fields = [
            "id",
            "table",
            "total",
            "pay_method",
            "delivery",
            "created_at",
            "order_status",
            "updated_at",
            "user",
            "client",
            "dishes",
        ]
