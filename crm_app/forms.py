from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from crm_app.models import Staff, Stock,Salary


class UserSignUpForm(UserCreationForm):
    email = (forms.EmailField(),)
    first_name = (forms.CharField(),)
    last_name = (forms.CharField(),)

    class Meta:
        model = User
        fields = {
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        }

class StaffRegisterForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = "__all__"

    

class StockAddForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = "__all__"

class PaymentSalaryForm(forms.ModelForm):
    class Meta:
        model = Salary
        fields = "__all__"

      
        