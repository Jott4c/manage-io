from rest_framework import serializers
from .models import Client, Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = [
            "id",
            "cep",
            "street",
            "city",
            "state",
            "number",
        ]


class ClientSerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = Client
        fields = [
            "id",
            "name",
            "phone",
            "birth_date",
            "address",
            "created_at",
            "updated_at",
        ]

    def create(self, validated_data):
        address_data = validated_data.pop("address")

        client = Client.objects.create(**validated_data)
        address = Address.objects.create(client=client, **address_data)

        return client
