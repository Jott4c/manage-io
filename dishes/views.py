from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.permissions import IsActiveTrue
from .models import Dish
from .serializers import DishSerializer


class DishView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsActiveTrue]

    queryset = Dish.objects.all()
    serializer_class = DishSerializer


class DishDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsActiveTrue]

    serializer_class = DishSerializer
    queryset = Dish.objects.all()
