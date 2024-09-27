# registration/forms.py
from django import forms
from .models import UserProfile

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    consent = forms.BooleanField(label='I agree to the terms and conditions', required=True)

    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password', 'confirm_password', 'address', 'phone_number', 'country', 'profile_picture', 'signature', 'consent']
