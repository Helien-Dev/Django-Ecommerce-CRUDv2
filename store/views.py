from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
import json
from .models import *


# Create your views here.

def landingPage(request):
    context = {}
    return render(request, 'store/landingPage.html', context)

def about_us(request):
    context = {}
    return render(request, 'store/about-us.html', context)


def client_support(request):
    context = {}
    return render(request, 'store/client_support.html', context)


def store(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {"get_cart_total": 0, "get_cart_items": 0, 'shipping': False}
        cartItems = order["get_cart_items"]

    products = Product.objects.all()
    context = {"products": products, "cartItems": cartItems}
    return render(request, "store/store.html", context)


def product_detail(request, slug):
    product_slug = get_object_or_404(Product, slug=slug)
    return render(request, 'store/product_detail.html', {'product_slug': product_slug})

def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {"get_cart_total": 0, "get_cart_items": 0, 'shipping': False}
        cartItems = order["get_cart_items"]

    context = {"items": items, "order": order, 'cart_items': cartItems}
    return render(request, "store/cart.html", context)


def checkout(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {"get_cart_total": 0, "get_cart_items": 0, 'shipping': False}
        cartItems = order["get_cart_items"]

    context = {"items": items, "order": order, 'cart_items': cartItems}
    return render(request, "store/checkout.html", context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data["productId"]
    action = data["action"]

    print("Action", action)
    print("productId", productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == "add":
        orderItem.quantity = orderItem.quantity + 1
    elif action == "remove":
        orderItem.quantity = orderItem.quantity - 1

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse("Item was added", safe=False)
