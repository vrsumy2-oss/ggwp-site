from django.urls import path
from django.http import HttpResponse
from . import views

urlpatterns = [
    path(
        "create-checkout-session/",
        views.create_checkout_session,
        name="create_checkout_session",
    ),
    path("webhook/", views.stripe_webhook, name="stripe_webhook"),
    path("buy/<int:item_id>/", views.create_item_checkout_session, name="buy_item"),
    path("success/", views.payment_success, name="success"),
    path("cancel/", lambda r: HttpResponse("Payment Cancelled."), name="cancel"),
]
