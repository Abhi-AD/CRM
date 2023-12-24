from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


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
    date_of_birth = models.DateField()
    membership_types = models.CharField(max_length=20, choices= [("basic", "Basic"),("gold", "Gold"),], default="basic")
    date_of_signature = models.DateTimeField(default=timezone.now)
    contact = models.CharField(max_length=10)
    emergency_contact = models.CharField(max_length=10,blank=True, null=True)
    emergency_contact2 = models.CharField(max_length=10,blank=True, null=True)
    registration_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
          