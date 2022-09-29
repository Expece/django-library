from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms


class SignUpUserForm(UserCreationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Username"}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "Password"}))
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "Repeat password"}))
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

class SignInUserForm(AuthenticationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Username"}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "Password"}))
    class Meta:
        model = User
        fields = ('username', 'password')

class UserEditForm(forms.ModelForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Username"}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "Password"}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "First name"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Last name"}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': "name@example.com",'id': "exampleFormControlInput1"}))
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')