from django.contrib import admin
from user_app.models import BillRecord, YogaMember, Member

# Register your models here.
admin.site.register(BillRecord)
admin.site.register(YogaMember)
admin.site.register(Member)
