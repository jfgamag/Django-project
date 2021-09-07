#Django
from django import forms
from django.forms.forms import Form
#models
from django.contrib.auth.models import User

class SignupForm(forms.Form):
    username = forms.CharField(min_length=4, max_length=50)

    password = forms.CharField(max_length=70, widget=forms.PasswordInput)
    password_confirmation = forms.CharField(max_length=70, widget=forms.PasswordInput)

    first_name = forms.CharField(min_length=2, max_length=20)
    last_name = forms.CharField(min_length=2, max_length=40)

    email = forms.CharField(min_length=6, max_length=70, widget= forms.EmailInput)
    
    def clean_username(self):
        """Username ust be unique
        """
        username = self.cleaned_data['username']
        taken_username = User.objects.filter(username=username).exist()
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



class ProfileForm(forms.Form):
    website = forms.URLField(max_length=200, required=True)
    biography = forms.CharField(max_length=500, required=False)
    phone_number = forms.CharField(max_length=20, required=False)
    picture = forms.ImageField(required=False) 