from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Customer
from django import forms 

from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

# - Register/Create a user

class CreateUserForm(UserCreationForm):
    
    class Meta:

        model = User
        fields = ['username','password1','password2']

# Login a user

class LoginForm(AuthenticationForm):

    username = forms.CharField(widget = TextInput())
    password = forms.CharField(widget = PasswordInput())


# - Add a customer

class AddCustomerForm(forms.ModelForm):

    class Meta:

        model = Customer
        fields = ['name','email','phone','due_date','address','due_amount']

# - Update a record

class UpdateCustomerForm(forms.ModelForm):

    class Meta:

        model = Customer
        fields = ['name','email','phone','due_date','address','due_amount']
