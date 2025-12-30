from django.contrib import admin
from .models import Item, Game, Category


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "game", "slug")
    list_filter = ("game",)


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "status", "seller")
    search_fields = ("title", "description")
    list_filter = ("status",)
