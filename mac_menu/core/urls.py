from django.contrib import admin
from django.urls import path

from api_menu.views import ProductListAPIView, ProductDetailAPIView, ProductDetailFieldDetailAPIView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("all_products/", ProductListAPIView.as_view()),
    path("products/<str:product_name>/", ProductDetailAPIView.as_view()),
    path("products/<str:product_name>/<str:product_field>/", ProductDetailFieldDetailAPIView.as_view()),
]
