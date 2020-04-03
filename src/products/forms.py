from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    # 可附加widget
    title = forms.CharField(widget=forms.Textarea(
        attrs={"placeholder": "Your Title"}))

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
        ]

    # 自己寫validate條件
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        if "jim" not in title:
            return title
        else:
            raise forms.ValidationError('This is not a valid title.')


class RawProductForm(forms.Form):
    title = forms.CharField(widget=forms.Textarea(
        attrs={"placeholder": "Your Title"}))
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(

            attrs={
                "placeholder": "Your description",
                "class": "new_class_for_text",
                "id": "id_for_textarea",
                "rows": 10,
                "cols": 80
            }))
    price = forms.DecimalField(initial=199.99)
