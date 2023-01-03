from django import forms
import django_select2.forms as select2_forms
from . import models


class SubTaskForm(forms.ModelForm):
    class Meta:
        model = models.SubTask
        fields = ['title', 'done']
        widgets = {
            'done': forms.CheckboxInput(attrs={'class': 'checkboxinput form-check-input'})
        }


class OrderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = models.Order
        widgets = {
            'client': select2_forms.Select2Widget(),
            'status': select2_forms.Select2Widget(),
            'deadline': forms.SelectDateWidget()
        }
        fields = ('title', 'status', 'client', 'description', 'deadline', 'closed', 'payed')
