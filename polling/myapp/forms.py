from django import forms
from django.contrib.auth.models import User
from .models import UserProfile
from .models import Question


class QuestionForm(forms.ModelForm):
    choice1 = forms.CharField(max_length=100)
    choice2 = forms.CharField(max_length=100)
    choice3 = forms.CharField(max_length=100)
    choice4 = forms.CharField(max_length=100)

    class Meta:
        model = Question
        fields = ['question_text', 'choice1', 'choice2', 'choice3', 'choice4']

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class UserProfileForm(forms.ModelForm):
    ROLES_CHOICES = [
        ('ADMIN', 'Admin'),
        ('VOTER', 'Voter'),
    ]

    phone = forms.CharField(max_length=15)
    description = forms.CharField(widget=forms.Textarea)
    roles = forms.MultipleChoiceField(choices=ROLES_CHOICES, widget=forms.CheckboxSelectMultiple)
    consent = forms.BooleanField(required=True)

    class Meta:
        model = UserProfile
        fields = ['phone', 'description', 'roles', 'consent']
        
