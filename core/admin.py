from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # Add 'balance' to the list view
    list_display = UserAdmin.list_display + ("balance", "is_seller")
    # Add 'balance' to the edit form
    fieldsets = UserAdmin.fieldsets + (
        ("Extra Fields", {"fields": ("balance", "is_seller")}),
    )
