from django.urls import reverse
from django.views.generic import ListView
from extra_views import CreateWithInlinesView, InlineFormSetFactory
from .models import Order, SubTask
from .forms import OrderForm, SubTaskForm


class OrderListView(ListView):
    model = Order
    template_name = 'orders/OrderList.html'


class SubTaskInline(InlineFormSetFactory):
    model = SubTask
    form_class = SubTaskForm
    factory_kwargs = {
        'extra': 0
    }


class OrderCreateView(CreateWithInlinesView):
    model = Order
    template_name = 'DetailForm.html'
    form_class = OrderForm
    inlines = [SubTaskInline]

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Создать заказ'
        context_data['model_name'] = 'Order'
        return context_data

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if not kwargs.get('initial'):
            kwargs['initial'] = {}
        return kwargs

    def get_success_url(self):
        return reverse('orders:order_list')

    def form_invalid(self, form):
        return super().form_invalid(form)
