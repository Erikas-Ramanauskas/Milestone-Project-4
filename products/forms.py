from django import forms
from .models import Product, Category, Image


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    # Change to FileField for multiple image uploads
    images = forms.FileField(label='Images', required=False,
                             widget=forms.ClearableFileInput(attrs={'multiple': True}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
