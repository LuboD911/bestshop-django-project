import os
from os.path import join

from django.conf import settings
from django import forms
from django.forms import FileInput

from bestshop.core.mixins import BootstrapFormMixin
from bestshop.products.models import Product, Comment
from bestshop.validators.validators import validate_dot



class ProductForm(BootstrapFormMixin, forms.ModelForm):
    title = forms.CharField(validators=[validate_dot])
    class Meta:
        model = Product
        exclude = ('user',)
        widgets = {
            'image': FileInput(),
        }



class EditProductForm(ProductForm):

    class Meta:
        model = Product
        fields = '__all__'



    def save(self, commit=True):
        db_product = Product.objects.get(pk=self.instance.id)
        if commit:
            if str(db_product.image) != 'image.png':
                image_path = join(settings.MEDIA_ROOT, str(db_product.image))
                os.remove(image_path)

        return super().save(commit)






class CommentForm(forms.ModelForm):
    product_pk = forms.IntegerField(
        widget=forms.HiddenInput()
    )

    class Meta:
        model = Comment
        fields = ('text','product_pk')

    def save(self, commit=True):
        product_pk = self.cleaned_data['product_pk']
        product = Product.objects.get(pk=product_pk)
        comment = Comment(
            text=self.cleaned_data['text'],
            product=product,
        )

        if commit:
            comment.save()

        return comment