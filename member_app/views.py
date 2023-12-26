from django.shortcuts import render, redirect
from member_app.forms import ContactForm
from django.contrib import messages
from django.views.generic import TemplateView
# Create your views here.


class ConatcView(TemplateView):
    template_name = "member/contact/contact.html"


