from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import ImageUpload
from .models import UserProfile


class AddStudentForm(forms.Form):
    username = forms.CharField(label="Kasutajanimi")
    first_name = forms.CharField(label="Eesnimi", required=False)
    email = forms.EmailField(label="E-post")
    password = forms.CharField(label="Parool", widget=forms.PasswordInput)

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    status = forms.ChoiceField(choices=UserProfile.STATUS_CHOICES, label="Staatus")

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "status", "password1", "password2")


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label="Kasutajanimi")
    password = forms.CharField(label="Parool", widget=forms.PasswordInput)


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageUpload
        fields = ['image']
        labels = {'image': 'Vali pilt'}
