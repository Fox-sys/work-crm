from django.shortcuts import render
from django.views.generic import ListView
from .models import Order


class OrderListView(ListView):
    model = Order
    template_name = 'orders/OrderList.html'
