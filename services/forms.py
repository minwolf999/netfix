from django import forms

from users.models import Company
from services.models import Service

class CreateNewService(forms.Form):
    name = forms.CharField(max_length=40)
    description = forms.CharField(widget=forms.Textarea, label='Description')
    price_hour = forms.DecimalField(
        decimal_places=2, max_digits=5, min_value=0.00)
    field = forms.ChoiceField(required=True, choices=Service.choices)

    def __init__(self, *args, choices=None, ** kwargs):
        super(CreateNewService, self).__init__(*args, **kwargs)
        # adding choices to fields
        if choices:
            self.fields['field'].choices = choices
        # adding placeholders to form fields

        self.fields['name'].widget.attrs['placeholder'] = 'Enter Service Name'
        self.fields['description'].widget.attrs['placeholder'] = 'Enter Description'
        self.fields['price_hour'].widget.attrs['placeholder'] = 'Enter Price per Hour'

        self.fields['name'].widget.attrs['autocomplete'] = 'off'


class RequestServiceForm(forms.Form):
    address = forms.CharField(widget=forms.Textarea)
    period = forms.DecimalField(min_value=0)

    def __init__(self, *args, ** kwargs):
        super(RequestServiceForm, self).__init__(*args, **kwargs)
        self.fields['address'].widget.attrs['placeholder'] = 'Enter Address'
        self.fields['period'].widget.attrs['placeholder'] = 'Enter Service Hours'
