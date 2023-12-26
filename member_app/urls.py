from django.urls import path
from member_app import views
from member_app.views import ConatcView

urlpatterns = [
    path('contact/', ConatcView.as_view(), name='contact'),
]
