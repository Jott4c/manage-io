from rest_framework import generics
from .models import Business
from .serializers import BusinessSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.permissions import IsActiveTrue, IsAdminPermission
from rest_framework.views import Response, status


class BusinessView(generics.CreateAPIView):
    serializer_class = BusinessSerializer
    queryset = Business.objects.all()


class BusinessDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsActiveTrue, IsAdminPermission]

    serializer_class = BusinessSerializer
    queryset = Business.objects.all()

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()

        instance.isActive = False

        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
