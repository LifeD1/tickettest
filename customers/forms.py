from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms.widgets import TextInput, PasswordInput
from sub_admins.models import User

class CustomerRegistrationForm(UserCreationForm):
    # first_name = forms.CharField()
    # last_name = forms.CharField()
    # gender = forms.ChoiceField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE')])
    # id_card = forms.CharField()
    email = forms.EmailField(required = True)
    # phone = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'gender', 'email', 'id_card',  'phone', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())