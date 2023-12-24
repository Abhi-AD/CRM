from django.urls import path
from user_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    
    path('add_record/', views.add_record, name='add_record'),
    path('record_details/', views.record_details, name='record_details'),
    path('record/<int:pk>/', views.bill_record, name='record'),
    path('update_record/<int:pk>', views.update_record, name='update_record'),
    path('delete_record/<int:pk>/', views.delete_record, name='delete_record'),
    
    path('add_yoga/', views.add_yoga, name='add_yoga'),
    path('yoga_details/', views.yoga_details, name='yoga_details'),
    path('yoga_member/<int:pk>/', views.yoga_member, name='yoga_member'),
    path('update_yoga/<int:pk>', views.update_yoga, name='update_yoga'),
    path('delete_yoga/<int:pk>/', views.delete_yoga, name='delete_yoga'),
]

