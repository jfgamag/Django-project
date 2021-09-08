#Django
from django import forms
<<<<<<< HEAD
from django.contrib.auth.models import User
=======
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


>>>>>>> c34caaed19f6ec92a20d0bc0bf68932beabbdb54

class ProfileForm(forms.Form):
    website = forms.URLField(max_length=200, required=True)
    biography = forms.CharField(max_length=500, required=False)
    phone_number = forms.CharField(max_length=20, required=False)
<<<<<<< HEAD
    picture = forms.ImageField(required=False)

class SignupForm(forms.Form):
    """Sign up form"""
    username = forms.CharField(min_length=4, max_length=50)

    password = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput()
    )
    password_confirmation = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput()
    )

    first_name = forms.CharField(min_length=2, max_length=50)
    last_name = forms.CharField(min_length=2, max_length=50)

    email = forms.CharField(
        min_length=6,
        max_length=70,
        widget=forms.EmailInput()
    )

    def clean_username(self):
        """Username must be unique."""
        username = self.cleaned_data['username']
        username_taken = User.objects.filter(username=username).exists()
        if username_taken:
            raise forms.ValidationError('Username is already in use.')
        return username

    def clean(self):
        """Verify password confirmation match."""
        data = super().clean()

        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Passwords do not match.')

        return data
=======
    picture = forms.ImageField(required=False) 
>>>>>>> c34caaed19f6ec92a20d0bc0bf68932beabbdb54
