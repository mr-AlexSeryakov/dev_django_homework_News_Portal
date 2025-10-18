from django import forms
from .models import Post

class ProductForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = [
            'author',
            'categories',
            'title',
            'text',
            'rating',
        ]

class SearchForm(forms.Form):
    title = forms.CharField(required=False)
    author = forms.CharField(required=False)
    date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type':'date'}))