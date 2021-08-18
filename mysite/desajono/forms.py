from .models import Comment
from django import forms
from django.forms import TextInput, EmailInput, Textarea

from .models import User


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
        widgets = {
        'name': TextInput(attrs={'class': "form-control"}),
        'email': EmailInput(attrs={'class': "form-control"}),
        'body' : Textarea(attrs={'class':'form-control'})
        }