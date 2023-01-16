from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "api/",
        include("users.urls"),
    ),
    path(
        "api/",
        include("clients.urls"),
    ),
    path(
        "api/",
        include("ingredients.urls"),
    ),
    path(
        "api/",
        include("dishes.urls"),
    ),
    path(
        "api/",
        include("orders.urls"),
    ),
    path(
        "api/",
        include("business.urls"),
    ),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="docs",
    ),
]
