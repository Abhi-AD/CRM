from django.urls import path
from crm_app import views

urlpatterns = [
    path('', views.main, name='main'),
    path('login_admin/', views.login_admin, name='login_admin'),
    path('logout_admin/', views.logout_admin, name='logout_admin'),
    path('register_user/', views.register_user, name='register_user'),
]
