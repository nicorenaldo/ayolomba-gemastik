from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from competitions.models import Lomba , Kategori

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

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label = 'Username'
        self.fields['password1'].label = 'Password'
        self.fields['password2'].label = 'Re-Enter Password'
        self.fields['email'].label = 'Alamat Email'

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email']
        
        labels = {
        "username": "Username",
        "email" : "Alamat Email",
        }


class ProfileUpdateForm(forms.ModelForm):
    # subscribe2 = forms.ModelChoiceField(queryset=Kategori.objects.all())

    class Meta:
        model = Profile
        exclude = ['user','favorite','subscribe']
        widgets = {
            'image': forms.FileInput(),
        }

        labels = {
        "firstname": "Nama Depan",
        "lastname" : "Nama Akhir",
        "image" : "Gambar",
        "participant_level" : "Tingkat Peserta",
        }