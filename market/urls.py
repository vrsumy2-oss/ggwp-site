from django.urls import path
from . import views

urlpatterns = [
    path("api/items/", views.ItemListAPIView.as_view(), name="item-list"),
    path("api/items/<int:pk>/", views.ItemDetailAPIView.as_view(), name="item-detail"),
]
