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
    
    path('add_member/', views.add_member, name='add_member'),
    path('member_details/', views.member_details, name='member_details'),
    path('member/<int:pk>/', views.member, name='member'),
    path('update_member/<int:pk>', views.update_member, name='update_member'),
    path('delete_member/<int:pk>/', views.delete_member, name='delete_member'),
    
    # view user
    path('stock_details_view/', views.stock_details_view, name='stock_details_view'),
    path('stock_view/<int:pk>/', views.stock_view, name='stock_view'),
    
    
    path('add_product/', views.add_product, name='add_product'),
    path('product_details/', views.product_details, name='product_details'),
    path('product/<int:pk>/', views.product, name='product'),
    path('update_product/<int:pk>', views.update_product, name='update_product'),
    path('delete_product/<int:pk>/', views.delete_product, name='delete_product'),
    
    path('cash_transaction_create/', views.cash_transaction_create, name="cash_transaction_create"),
    path('cash_transaction_list/', views.cash_transaction_list, name="cash_transaction_list"),
    
    
    path('add_sport/', views.add_sport, name='add_sport'),
    path('sport_details/', views.sport_details, name='sport_details'),
    path('sport/<int:pk>/', views.sport, name='sport'),
    path('update_sport/<int:pk>', views.update_sport, name='update_sport'),
    path('delete_sport/<int:pk>/', views.delete_sport, name='delete_sport'),
    
    path('add_voice/', views.add_voice, name='add_voice'),
    path('voice_details/', views.voice_details, name='voice_details'),
    path('voice/<int:pk>/', views.voice, name='voice'),
    path('update_voice/<int:pk>', views.update_voice, name='update_voice'),
    path('delete_voice/<int:pk>/', views.delete_voice, name='delete_voice'),
    
    path('add_sport_player/', views.add_sport_player, name='add_sport_player'),
    path('sport_player_details/', views.sport_player_details, name='sport_player_details'),
    path('sport_player/<int:pk>/', views.sport_player, name='sport_player'),
    path('update_sport_player/<int:pk>', views.update_sport_player, name='update_sport_player'),
    path('delete_sport_player/<int:pk>/', views.delete_sport_player, name='delete_sport_player'),
    
]

