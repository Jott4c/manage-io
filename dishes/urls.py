from django.urls import path
from . import views

urlpatterns = [
    path("dishes/", views.DishView.as_view()),
    path("dishes/<str:pk>/", views.DishDetailView.as_view()),
]
