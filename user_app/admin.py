from django.contrib import admin
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

# Register your models here.
admin.site.register(BillRecord)
admin.site.register(YogaMember)
admin.site.register(Member)
admin.site.register(Product)
admin.site.register(CashTransaction)
admin.site.register(Sport)
admin.site.register(VocalRecording)
admin.site.register(SportPlayer)