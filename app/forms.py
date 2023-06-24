from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class BootstrapAuthenticationForm(AuthenticationForm):
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))


#class SignupForm(forms.Form):
class SignupForm(UserCreationForm):
    username = forms.CharField(label="User Name", max_length=254, required=True,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User Name'}))

    #password = forms.CharField(label="Password", max_length=254, required=True,
    #                           widget=forms.PasswordInput({
    #                               'class': 'form-control',
    #                               'placeholder':'Password'}))

    first_name = forms.CharField(label="First Name", max_length=254, required=True,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'First Name'}))

    
    last_name = forms.CharField(label="Last Name", max_length=254, required=True,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Last Name'}))

    email = forms.CharField(label="Email", max_length=254, required=True,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Email'}))
    
    #class Meta:
    #    model = User
    #    fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

    
class LoginForm(forms.Form):
    username = forms.CharField(label="username", max_length=254, required=True,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label="Password", max_length=254, required=True,
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

