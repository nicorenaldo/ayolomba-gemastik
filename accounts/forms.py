from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username' : forms.TextInput(attrs={'class': 'input', 'placeholder' : 'Your Username'}),
            'email' : forms.EmailInput(attrs={'class': 'input', 'placeholder' : 'you@email.com'}),
            'password1': forms.Textarea(attrs={'class': 'textarea', 'rows': 10, 'placeholder' : 'Your message...'}),
            'password2': forms.Textarea(attrs={'class': 'textarea', 'rows': 10, 'placeholder' : 'Your message...'}),
        }

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user','favorite']
        widgets = {
            'image': forms.FileInput(),
        }