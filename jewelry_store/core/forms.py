from django import forms

from store.models import Collection, Category, Product


class AddProductForm(forms.Form):
    name = forms.CharField(required=True)
    vendor_code = forms.CharField(required=True)
    description = forms.CharField(widget=forms.widgets.Textarea, required=True)
    metal = forms.CharField(required=True)
    insertion = forms.BooleanField()
    insert_type = forms.CharField()
    # size = forms.DecimalField(default=0, max_digits=4, decimal_places=1)
    # weight = forms.DecimalField(default=0, max_digits=4, decimal_places=2)
    # price = forms.DecimalField(default=0, max_digits=7, decimal_places=2)
    # collection = forms.ModelMultipleChoiceField(queryset=Collection.objects.all, required=True)
    # category = forms.ModelMultipleChoiceField(queryset=Category.objects.all, required=True)
    is_active = forms.BooleanField()

    def save(self):
        product = Product.objects.create(
            name=self.cleaned_data['name'],
            vendor_code=self.cleaned_data['vendor_code'],
            description=self.cleaned_data['description'],
        )
        return product
