from django import forms
from django.contrib.auth.forms import AuthenticationForm,UsernameField


class Loginform(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'autofocus': True,'class':'form-input','id':'email','placeholder':"Username"}))
    password=forms.CharField(
        #label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password','id':'password','class':'form-input','placeholder':'Password'}),
    )