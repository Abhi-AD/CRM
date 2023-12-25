from django.urls import path
from crm_app import views

urlpatterns = [
    path('', views.main, name='main'),
    path('login_admin/', views.login_admin, name='login_admin'),
    path('logout_admin/', views.logout_admin, name='logout_admin'),
    path('user/', views.user, name='user'),
    path('register_user/', views.register_user, name='register_user'),

    # staff
    path('add_staff/', views.add_staff, name='add_staff'),
    path('staff_details/', views.staff_details, name='staff_details'),
    path('staff/<int:pk>/', views.staff, name='staff'),
    path('update_staff/<int:pk>', views.update_staff, name='update_staff'),
    path('delete_staff/<int:pk>/', views.delete_staff, name='delete_staff'),
]
