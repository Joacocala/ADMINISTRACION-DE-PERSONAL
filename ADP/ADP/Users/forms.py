from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserChangeForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(
        label="Correo Electrónico",
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    password1 = forms.CharField(
        label="Contraseña",
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label="Confirmar Contraseña",
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
        }


class Meta:
    model = User
    fields = ["username","email","password1","password2"]
    help_texts ={k:" " for k in fields}


class UserEditForm(UserChangeForm):
    password = None
    email = forms.EmailField(label="Ingesa tu email")
    last_name = forms.CharField(label="Ingresa tu apellido")
    first_name = forms.CharField(label="Ingresa tu nombre")
    imagen = forms.ImageField(label="avatar",required=False)

    class Meta:
        model = User
        fields = ["email","last_name","first_name"]