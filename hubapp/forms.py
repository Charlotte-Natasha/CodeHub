from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *

class PostForm(forms.ModelForm):
    class Meta:  
        model = Post
        fields = '__all__'

class CommentForm(forms.ModelForm):
    body = forms.CharField(label='',widget=forms.Textarea(attrs={'class': 'textarea'}), required=True)

    class Meta:
        model = Comment
        fields = ('body',)        