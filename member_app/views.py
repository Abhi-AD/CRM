from django.shortcuts import render, redirect
from member_app.forms import ContactForm
from django.contrib import messages
from django.views.generic import View
# Create your views here.


class ContactView(View):
    template_name = "member/contact/contact.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Successfully submitted your query. We will contact you soon "
            )
            return redirect("contact")
        else:
            messages.error(request, "Cannot submit your data. ")
            return render(
                request,
                self.template_name,
                {"form": form},
            )

