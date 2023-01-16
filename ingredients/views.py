from rest_framework import generics
from .models import Ingredients
from .serializers import IngredientsSerializer
from users.permissions import IsActiveTrue
from rest_framework_simplejwt.authentication import JWTAuthentication


class IngredientView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsActiveTrue]

    queryset = Ingredients.objects.all()
    serializer_class = IngredientsSerializer


class IngredientDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsActiveTrue]

    serializer_class = IngredientsSerializer
    queryset = Ingredients.objects.all()
