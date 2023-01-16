from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsAdminPermission, IsActiveTrue
from rest_framework.views import Response, status

from .models import User
from .serializers import UserSerializer
import jwt
import ipdb


class UserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserAllView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsActiveTrue, IsAdminPermission]

    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsActiveTrue, IsAdminPermission]

    serializer_class = UserSerializer
    queryset = User.objects.all()

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()

        instance.isActive = False

        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserMeView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsActiveTrue]

    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        user_id = request.user.id
        queryset = User.objects.filter(id=user_id)
        serializer = UserSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
