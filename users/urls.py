from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("users/", views.UserView.as_view()),
    path("users/login/", jwt_views.TokenObtainPairView.as_view()),
    path("users/all/", views.UserAllView.as_view()),
    path("users/<str:pk>/", views.UserDetailView.as_view()),
    path("users/me", views.UserMeView.as_view()),
]
