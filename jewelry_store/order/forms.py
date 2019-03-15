from django import forms


class CheckoutClientForm(forms.Form):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone = forms.CharField(required=True)
    address = forms.CharField(required=True)
    comments = forms.CharField(widget=forms.widgets.Textarea(
        attrs={'class': "form-control", 'rows': 7, 'data-form-field': "Comments"}))
