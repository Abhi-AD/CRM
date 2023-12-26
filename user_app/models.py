from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import ValidationError
from datetime import date


class BillRecord(models.Model):
    date = models.DateField(auto_now_add = True)
    description = models.TextField()

    # Details about the items in the bill
    item_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    # Additional fields (you can customize these based on your needs)
    customer_name = models.CharField(max_length=100)
    payment_status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('paid', 'Paid')])

    def __str__(self):
        return f"{self.id} - {self.customer_name}"





class YogaMember(models.Model):
    first_name = models.CharField(max_length=100)
    middel_name = models.CharField(max_length=10,blank=True)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=20, choices=[("male", "Male"),("female", "Female"),("other", "Other"),])
    images = models.ImageField(upload_to="YogaMember/%Y/%m/%d", blank=False)
    street_address = models.CharField(max_length=255, blank=True)
    street_address2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state_province = models.CharField(max_length=100, blank=True, null=True)
    zip_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(default=timezone.now)
    membership_types = models.CharField(max_length=20, choices= [("basic", "Basic"),("gold", "Gold"),], default="basic")
    date_of_signature = models.DateTimeField(default=timezone.now)
    contact = models.CharField(max_length=10)
    emergency_contact = models.CharField(max_length=10,blank=True, null=True)
    emergency_contact2 = models.CharField(max_length=10,blank=True, null=True)
    registration_date = models.DateField(auto_now_add=True)
    
    def clean(self):
        # Check if the person is less than 5 years old
        age_limit = 5
        if self.date_of_birth:
            age = (date.today() - self.date_of_birth).days // 365
            if age < age_limit:
                raise ValidationError({'date_of_birth': 'Must be at least 5 years old.'})



    def __str__(self):
        return f"{self.first_name} {self.last_name}"
  
  
class Member(models.Model):
    first_name = models.CharField(max_length=100)
    middel_name = models.CharField(max_length=10,blank=True)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=20, choices=[("Male", "Male"),("Female", "Female"),("Other", "Other"),])
    images = models.ImageField(upload_to="Member/%Y/%m/%d", blank=False)
    street_address = models.CharField(max_length=255, blank=True)
    street_address2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state_province = models.CharField(max_length=100, blank=True, null=True)
    zip_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(default=timezone.now)
    membership_types = models.CharField(max_length=20, choices= [("basic", "Basic"),("gold", "Gold"),], default="basic")
    date_of_signature = models.DateTimeField(default=timezone.now)
    contact = models.CharField(max_length=10)
    emergency_contact = models.CharField(max_length=10,blank=True, null=True)
    emergency_contact2 = models.CharField(max_length=10,blank=True, null=True)
    registration_date = models.DateField(auto_now_add=True)

    def clean(self):
        # Check if the person is less than 17 years old
        age_limit = 17
        if self.date_of_birth:
            age = (date.today() - self.date_of_birth).days // 365
            if age < age_limit:
                raise ValidationError({'date_of_birth': 'Must be at least 17 years old.'})

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
