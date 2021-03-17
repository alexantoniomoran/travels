from django import forms
from django.contrib.auth.forms import AuthenticationForm


class CustomAuthForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.widgets.TextInput(
            attrs={"class": "validate", "placeholder": "admin"}
        )
    )
    password = forms.CharField(
        widget=forms.widgets.PasswordInput(attrs={"placeholder": "password"})
    )
