from pyexpat import model
from django import forms
from .models import User


class SignUpForm(forms.Form):
    username = forms.CharField(max_length=254)
    email = forms.EmailField()
    first_name = forms.CharField(max_length=254)
    last_name = forms.CharField(max_length=254)
    password = forms.CharField(max_length=8)
