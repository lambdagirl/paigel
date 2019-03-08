from django import forms
from .models import Article, Images
from django.forms.models import modelformset_factory

class ArticleForm(forms.ModelForm):
    title = forms.CharField(max_length=128, label='title')

    class Meta:
        model = Article
        fields = ('title', 'body', )


class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')
    class Meta:
        model = Images
        fields = ('image', )


ImageFormSet = modelformset_factory(Images,form=ImageForm, extra=3)
