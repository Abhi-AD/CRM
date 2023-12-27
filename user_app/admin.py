from django.contrib import admin
from user_app.models import BillRecord, YogaMember, Member,Product,CashTransaction

# Register your models here.
admin.site.register(BillRecord)
admin.site.register(YogaMember)
admin.site.register(Member)
admin.site.register(Product)
admin.site.register(CashTransaction)
