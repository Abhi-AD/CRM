from django.urls import path
from member_app import views
from member_app.views import ContactView

urlpatterns = [
    path('contact/', ContactView.as_view(), name='contact'),
]
