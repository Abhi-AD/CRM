from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from crm_app.forms import UserSignUpForm
from user_app.models import BillRecord


def main(request):
    records = BillRecord.objects.all()

    # check to see if logging
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        # authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been login !")
            return redirect("main")
        else:
            messages.error(request, "Username or Password is incorrect.")
            return redirect("main")
    else:
        return render(request, "crm/home.html", {"records": records})


def login_admin(request):
    pass


def logout_admin(request):
    logout(request)
    messages.success(request, "Admin logout Sucessfully")
    return redirect("main")


def register_user(request):
    if request.method == "POST":
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f"Account created for {username}! Successfully.")
            return redirect("main")
    else:
        form = UserSignUpForm()
        return render(request, "crm/register.html", {"form": form})







      
        
        