from django.urls import path
from . import views


urlpatterns = [
    path('', views.landingPage, name='landingPage'),
    path("store/", views.store, name="store"),
    path("cart/", views.cart, name="cart"),
    path("checkout/", views.checkout, name="checkout"),
    path("update_item/", views.updateItem, name="update_item"),
    path("about_us/", views.about_us, name="about_us"),
    path("client_support/", views.client_support, name="client_support"),
    path("product/<slug:slug>/", views.product_detail, name="product_detail"),
]