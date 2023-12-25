from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

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

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

