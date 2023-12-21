from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include('crm_app.urls')),
    path('user/', include('user_app.urls')),
]
