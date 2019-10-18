from django.forms import ModelForm
from .models import Predict
from django import forms

class predict_form(ModelForm):
    class Meta:
        model = Predict
        fields = '__all__'



class UserRegistrationForm(forms.Form):
    username = forms.CharField(
        required = True,
        label = 'Username',
        max_length = 32
    )
    email = forms.CharField(
        required = True,
        label = 'Email',
        max_length = 32,
    )
    password = forms.CharField(
        required = True,
        label = 'Password',
        max_length = 32,
        widget = forms.PasswordInput()
    )

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Predict
        fields = ('full_name','address','phone_no')#,'tenure','internet_service','phone_service','multiple_lines','online_security',
                  #'online_backup','stream_tv','stream_mov','tech_support']