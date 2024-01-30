from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Order

# Create your views here.

def home(request):
    return render(request, "index.html", context = {})

def mark_order_completed(request, order_id=1):
    order = Order.objects.get(pk=order_id)
    if not order.is_completed:
        order.is_completed = True
        order.save()
        # Message
        messages.success(request, f"Order {order.pk} marked as completed!")
        # Email (Optional)
        send_mail(
        "Your WonderShop Order is Complete!",
        f"Hi {order.customer_name}, your order \
        {order.pk} has been marked as completed.",
        "alimohammadlou@gmail.com",
        [order.email],
        )
    else:
        messages.info(request, \
        f"Order {order.pk} is already marked as completed.")
        # Redirect or return to detail view
    return redirect("home")
