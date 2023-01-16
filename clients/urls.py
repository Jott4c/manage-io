from django.urls import path

from . import views


urlpatterns = [
    path("clients/", views.ClientView.as_view()),
    path("clients/all/", views.ClientAllView.as_view()),
    path("clients/<str:pk>/", views.ClientDetailView.as_view()),
]
