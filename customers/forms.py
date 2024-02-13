from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms.widgets import TextInput, PasswordInput
from customers.models import Reservation
from sub_admins.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, Div, Row, Column, Field

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


# class Row(Div):
#     css_class = 'row g-3'

class ReservationForm(ModelForm):
    
    # first_name = forms.CharField()
    # last_name = forms.CharField()
    # id_card = forms.CharField()
    # def __init__(self, *args, **kwargs):
    #     super(ReservationForm, self).__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.layout = Layout(
    #         Row(
    #             Column('first_name', css_class='form-group col-md-4 mb-0'),
    #             Column('last_name', css_class='form-group col-md-4 mb-0'),
    #             Column('id_card', css_class='form-group col-md-4 mb-0'),
    #             css_class='form-row'
    #         ),
    #         # 'phone',
    #         # 'number_of_persons',
    #         Row(
    #             Column('phone', css_class='form-group col-md-4 mb-0'),
    #             Column('bus', css_class='form-group col-md-4 mb-0'),
    #             Column('agency', css_class='form-group col-md-4 mb-0'),
    #             css_class='form-row'
    #         ),
    #         Row(
    #             Column('branch', css_class='form-group col-md-4 mb-0'),
    #             Column('origin', css_class='form-group col-md-4 mb-0'),
    #             Column('destination', css_class='form-group col-md-4 mb-0'),
    #             css_class='form-row'
    #         ),
    #         Row(
    #             Column('departure_time', css_class='form-group col-md-4 mb-0'),
    #             Column('trip_type', css_class='form-group col-md-4 mb-0'),
    #             Column('bus_type', css_class='form-group col-md-4 mb-0'),
    #             css_class='form-row'
    #         ),
    #         Row(
    #             Column('number_of_persons', css_class='form-group col-md-4 mb-0'),
    #             Column('seat_number', css_class='form-group col-md-4 mb-0'),
    #             Column('trip_cost', css_class='form-group col-md-4 mb-0'),
    #             css_class='form-row'
    #         ),
            
    #         Submit('submit', 'Sign in')
    #     )
    
    
    class Meta:
        model = Reservation
        fields = '__all__'
        # fields = ['first_name', 'last_name', 'id_card', 'customer','origin']