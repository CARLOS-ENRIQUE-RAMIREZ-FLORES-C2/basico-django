""" Users forms """

#Django
from django import forms

#Models
from django.contrib.auth.models import User
from users.models import Profile

class SignupForm(forms.Form):
    """ Sign up form """
    #https://docs.djangoproject.com/en/2.0/ref/forms/fields/
    username = forms.CharField(min_length=4, max_length=30)

    #https://docs.djangoproject.com/en/2.0/ref/forms/widgets/
    password = forms.CharField(
        min_length = 8, 
        max_length = 50, 
        widget     = forms.PasswordInput()
    )
    password_confirmation = forms.CharField(
        min_length=8, 
        max_length=50, 
        widget=forms.PasswordInput()
    )
    first_name = forms.CharField(min_length=3, max_length=30)
    last_name = forms.CharField(min_length=3, max_length=30)

    email = forms.CharField(
        min_length=6, 
        max_length=50,
        widget= forms.EmailInput()
    )
    #https://docs.djangoproject.com/en/2.0/ref/forms/validation/
    def clean_username(self):
        """Username must be unique. """
        username = self.cleaned_data['username']
        username_taken = User.objects.filter(username=username).exists()
        if username_taken:
            raise forms.ValidationError('Username is already in use.')
        return username

    def clean(self):
        """ Verify password confirmation match. """
        data = super().clean()

        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Passwords do not match.')

        return data


    def save(self):
        data = self.cleaned_data
        data.pop('password_confirmation')

        user = User.objects.create_user(**data)
        profile = Profile(user= user)
        profile.save()


class ProfileForm(forms.Form):
    """ profile form."""

    website      = forms.URLField(max_length=200, required=True)
    biography    = forms.CharField(max_length=500, required=False)
    phone_number = forms.CharField(max_length=20, required=False)
    picture      = forms.ImageField()