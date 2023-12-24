from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from user_app.models import BillRecord, YogaMember, Member


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


class AddBillRecordFrom(forms.ModelForm):
    class Meta:
        model = BillRecord
        fields = "__all__"


class AddYogaMemberFrom(forms.ModelForm):
    class Meta:
        model = YogaMember
        fields = "__all__"


class AddMemberFrom(forms.ModelForm):
    class Meta:
        model = Member
        fields = "__all__"
