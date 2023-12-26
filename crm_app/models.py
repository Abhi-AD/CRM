from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import ValidationError
from datetime import date
# Create your models here.


class Staff(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    images = models.ImageField(upload_to="Staff/%Y/%m/%d", blank=False)
    position = models.CharField(max_length=20,choices=[("staff", "staff"),("manager", "Manager"),("Boss", "Boss"),])
    gender = models.CharField(max_length=20, choices=[("male", "Male"),("female", "Female"),("other", "Other"),])
    email = models.EmailField(unique = True)
    contact = models.CharField(max_length=10)
    date_of_birth = models.DateField(default=timezone.now)
    address = models.CharField(max_length=255, blank=True)
    hire_date = models.DateField(auto_now_add = True)

    def clean(self):
        # Check if the person is less than 17 years old
        age_limit = 17
        if self.date_of_birth:
            age = (date.today() - self.date_of_birth).days // 365
            if age < age_limit:
                raise ValidationError({'date_of_birth': 'Must be at least 17 years old.'})
            
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Stock(models.Model):
    selling_price = models.PositiveIntegerField()
    cost_price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    name = models.CharField(max_length=100)
    using_date = models.IntegerField()
    images = models.ImageField(upload_to="Stock/%Y/%m/%d", blank=False)
    
    
    
    def __str__(self):
        return self.name