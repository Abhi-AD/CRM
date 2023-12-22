# models.py

from django.db import models

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
        return f"{self.bill_number} - {self.customer_name}"
