from django.urls import path

from orders.views import OrderListView, OrderCreateView

app_name = 'orders'

urlpatterns = [
    path('', OrderListView.as_view(), name='order_list'),
    path('create/', OrderCreateView.as_view(), name='order_create')
]
