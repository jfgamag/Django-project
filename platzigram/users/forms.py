#Django
from django import forms
from django.forms.forms import Form
#models
from django.contrib.auth.models import User
from users.models import Profile

class SignupForm(forms.Form):
    username = forms.CharField(
        label=False,min_length=4,max_length=50, 
        widget = forms.TextInput(attrs={'placeholder':'Username',
        'class': 'form-control','required': True}))

    password = forms.CharField(
        label=False,max_length=70, 
        widget=forms.PasswordInput(attrs={'placeholder':'Write your password',
        'class': 'form-control','required': True}))

    password_confirmation = forms.CharField(
        label=False,max_length=70, 
        widget=forms.PasswordInput(attrs={'placeholder':'Confirm your password',
        'class': 'form-control','required': True}))

    first_name = forms.CharField(
        label=False,min_length=2,max_length=50,
        widget = forms.TextInput(attrs={'placeholder':'Name',
        'class': 'form-control','required': True}))

    last_name = forms.CharField(label=False,min_length=2,max_length=50,
    widget = forms.TextInput(attrs={'placeholder':'Last Name',
    'class': 'form-control','required': True}))

    email = forms.EmailField(label=False,min_length=6,max_length=70,
    widget=forms.EmailInput(attrs={'placeholder':'Email',
    'class': 'form-control','required': True}))
    
    def clean_username(self):
        """Username ust be unique
        """
        username = self.cleaned_data['username']
        taken_username = User.objects.filter(username=username).exists()
        if taken_username:
            raise forms.ValidationError('Username already in use, choose another one')
        else:
            return username

    def clean(self):
        """Verify password confirmation match"""
        data = super().clean()
        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            forms.ValidationError("Password doesn't match")
        else:
            return data

    def save(self):
        """Create user and profile"""
        data = self.cleaned_data
        data.pop('password_confirmation')

        user = User.objects.create_user(**data)
        profile = Profile(user=user)
        profile.save()

