from django import forms
from .models import Elon
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class ElonForm(forms.ModelForm):
    class Meta:
        model = Elon
        fields = '__all__'

class CustomAdminLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full py-2 outline-none',
        'placeholder': 'Login kiriting'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full py-2 outline-none',
        'placeholder': 'Parol kiriting'
    }))