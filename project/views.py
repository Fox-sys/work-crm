from django.urls import reverse
from django.shortcuts import redirect


def home_redirect_view(request):
    return redirect(reverse('orders.order_list'))

