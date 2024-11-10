from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from .models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField()
    
    class Meta:
        model = User
        fields = ('username', 'password')
        
        
class UserRegistrationForm(UserCreationForm):
    username = forms.CharField()
    email = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
        
class ProfileForm(forms.ModelForm):
    username = forms.CharField()
    email = forms.CharField()
    class Meta:
        model = User
        fields = ('username', 'email', 'status')

