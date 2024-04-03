from django.contrib import admin
from django.urls import path

from api_menu.views import ProductListAPIView, ProductDetailAPIView, ProductDetailFieldDetailAPIView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("product/", ProductListAPIView.as_view()),
    path("product/<str:title>/", ProductDetailAPIView.as_view()),
    path("product/<str:title>/<str:field>/", ProductDetailFieldDetailAPIView.as_view()),
]
