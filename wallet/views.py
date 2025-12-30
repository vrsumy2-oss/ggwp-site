import stripe
from django.conf import settings
from django.shortcuts import redirect, render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from market.models import Item
from .models import Transaction

stripe.api_key = settings.STRIPE_SECRET_KEY


def create_checkout_session(request):
    # Hardcoded $10.00 for testing
    amount = 1000  # Cents

    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[
            {
                "price_data": {
                    "currency": "usd",
                    "product_data": {"name": "Top-up Balance ($10)"},
                    "unit_amount": amount,
                },
                "quantity": 1,
            }
        ],
        mode="payment",
        success_url="http://localhost:8000/wallet/success/",
        cancel_url="http://localhost:8000/wallet/cancel/",
    )
    return redirect(session.url, code=303)


def create_item_checkout_session(request, item_id):
    item = Item.objects.get(id=item_id)
    amount = int(item.price * 100)  # Cents

    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[
            {
                "price_data": {
                    "currency": "usd",
                    "product_data": {"name": item.title},
                    "unit_amount": amount,
                },
                "quantity": 1,
            }
        ],
        mode="payment",
        success_url=f"http://localhost:8000/wallet/success/?item_id={item_id}",
        cancel_url="http://localhost:8000/wallet/cancel/",
    )
    return redirect(session.url, code=303)


def payment_success(request):
    item_id = request.GET.get("item_id")
    item = None
    if item_id:
        item = Item.objects.get(id=item_id)

    return render(request, "success.html", {"item": item})


@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META["HTTP_STRIPE_SIGNATURE"]
    event = None
    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        return HttpResponse(status=400)
    # Handle the checkout.session.completed event
    if event["type"] == "checkout.session.completed":
        # TODO: Update user balance here (We will implement this next)
        print("Payment successful!")
    return HttpResponse(status=200)
