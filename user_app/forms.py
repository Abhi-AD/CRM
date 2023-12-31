from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from user_app.models import (
    BillRecord,
    YogaMember,
    Member,
    Product,
    CashTransaction,
    Sport,
    VocalRecording,
    SportPlayer,
)


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


class AddProductFrom(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"


class CashTransactionForm(forms.ModelForm):
    class Meta:
        model = CashTransaction
        fields = "__all__"


class SportForm(forms.ModelForm):
    class Meta:
        model = Sport
        fields = "__all__"


class VocalRecordingForm(forms.ModelForm):
    class Meta:
        model = VocalRecording
        fields = "__all__"


class SportPlayerForm(forms.ModelForm):
    class Meta:
        model = SportPlayer
        fields = "__all__"
