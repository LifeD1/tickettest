from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User, Agency
from django.forms import ModelForm


class AddAgencyForm(ModelForm):
    class Meta:
        model = Agency
        fields = '__all__'

class AddAgencyAdminForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField(required=True)
    gender = forms.ChoiceField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE')])
    phone = forms.CharField
    agency =  forms.ModelChoiceField(queryset=Agency.objects.all(), to_field_name='id')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'gender',  'phone', 'agency', 'password1', 'password2']