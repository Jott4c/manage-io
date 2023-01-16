from django.urls import path
from . import views


urlpatterns = [
    path("ingredients/", views.IngredientView.as_view()),
    path("ingredients/<str:pk>/", views.IngredientDetailView.as_view()),
]
