from django import forms
from django.forms import ModelForm
from agencies.models import Bus, Bus_layout, Driver, Trip
from sub_admins.models import Agency, Branche, User
from django.contrib.auth.forms import UserCreationForm

class AddBrandForm(ModelForm):
    class Meta:
        model = Branche
        fields = ['name', 'town']


class AddBrandAdminForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField(required=True)
    gender = forms.ChoiceField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE')])
    phone = forms.CharField()
    # agency =  forms.CharField(initial= {'agency' =request.user.agency})
    branch =  forms.ModelChoiceField(queryset=Branche.objects.all(), to_field_name='id')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'gender',  'phone', 'branch' , 'password1', 'password2']


class AddTellerForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField(required=True)
    gender = forms.ChoiceField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE')])
    phone = forms.CharField()
    # agency =  forms.CharField(initial= {'agency' =request.user.agency})
    branch =  forms.ModelChoiceField(queryset=Branche.objects.all(), to_field_name='id')
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'gender',  'phone', 'branch' , 'password1', 'password2']


class AddBusLayoutForm(ModelForm):
    class Meta:
        model = Bus_layout
        fields = '__all__'

class AddBusForm(ModelForm):
    class Meta:
        model = Bus
        fields = '__all__'


class AddDriverForm(ModelForm):
    class Meta:
        model = Driver
        fields = '__all__'
        exclude = ('agency',)

class AddTripForm(ModelForm):
    class Meta:
        model = Trip
        fields = '__all__'