from rest_framework import generics
from .models import Item
from .serializers import ItemSerializer


class ItemListAPIView(generics.ListAPIView):
    serializer_class = ItemSerializer

    def get_queryset(self):
        queryset = Item.objects.filter(status="active")
        # Use GET.get() for maximum compatibility
        game_slug = self.request.GET.get("game")
        if game_slug:
            # Case-insensitive exact match
            queryset = queryset.filter(category__game__slug__iexact=game_slug)
        return queryset


class ItemDetailAPIView(generics.RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
