from django import forms

from .models import Order


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = (
            'first_name', 'last_name', 'address', 'phone', 'email',
            'buying_type', 'order_date', 'comment',
        )
        to_email = forms.EmailField()
