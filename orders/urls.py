from django.contrib import admin
from django.urls import path

app_name = 'orders'

urlpatterns = [
    path('', admin.site.urls, name='order_list')  # временная заглушка, после добавления списка заказов: заменить на список заказов
]
