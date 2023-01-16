from rest_framework import generics
from .models import Client
from .serializers import ClientSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.permissions import IsActiveTrue


class ClientView(generics.CreateAPIView):
    serializer_class = ClientSerializer


class ClientAllView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsActiveTrue]

    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsActiveTrue]

    serializer_class = ClientSerializer
    queryset = Client.objects.all()
