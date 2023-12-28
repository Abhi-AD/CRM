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
    registration_date = models.DateField(auto_now_add=True)

    

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



class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    images = models.ImageField(upload_to="product/%Y/%m/%d", blank=False)
    
    
    def __str__(self):
        return f"{self.name} price:{self.price}"




class CashTransaction(models.Model):
    name = models.CharField(max_length = 255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=8, choices=[("Payment", "Payment"),
        ("Pending", "Pending"),])
    date = models.DateField(default=timezone.now)
    description = models.TextField()

    def __str__(self):
        return f"{self.transaction_type} - {self.amount} {self.name}"



class Sport(models.Model):
    name = models.CharField(max_length=100)
    players = models.PositiveIntegerField()
    equipment = models.CharField(max_length=100)
    images = models.ImageField(upload_to="Sport/Sport/%Y/%m/%d", blank=False)
    

    def __str__(self):
        return self.name


class VocalRecording(models.Model):
    title = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    artist_profile = models.ImageField(upload_to="artist/artist_profile/%Y/%m/%d", blank=False)
    recording_date = models.DateField(default = timezone.now())
    audio_file = models.FileField(upload_to='artist/vocal_recordings/%Y/%m/%d')

    def __str__(self):
        return self.title


class SportPlayer(models.Model):
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    player_name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    images = models.ImageField(upload_to="Sport/Sportplayer/%Y/%m/%d", blank=False)
    

    def __str__(self):
        return f"{self.player_name} - {self.sport.name}"