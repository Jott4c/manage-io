from django.urls import path

from . import views


urlpatterns = [
    path("business/", views.BusinessView.as_view()),
    path("business/<str:pk>/", views.BusinessDetailView.as_view()),
]
