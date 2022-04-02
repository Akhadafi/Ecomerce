from django.urls import path

import store

from . import views

apps_name = store
urlpatterns = [
    # Leave as empty string for base url
    path("", views.store, name="store"),
    path("cart/", views.cart, name="cart"),
    path("checkout/", views.checkout, name="checkout"),
    #
    path("update_item/", views.updateItem, name="update_item"),
    path("process_order/", views.processOrder, name="process_order"),
]
