from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from crm_app.forms import UserSignUpForm, AddRecordFrom
from crm_app.models import Record


def home(request):
    records = Record.objects.all()

    # check to see if logging
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        # authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been login !")
            return redirect("home")
        else:
            messages.error(request, "Username or Password is incorrect.")
            return redirect("home")
    else:
        return render(request, "crm/home.html", {"records": records})


def login_user(request):
    pass


def logout_user(request):
    logout(request)
    messages.success(request, "You have been log Out ...")
    return redirect("home")


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
            return redirect("home")
    else:
        form = UserSignUpForm()
        return render(request, "crm/register.html", {"form": form})


def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        return render(request, "crm/record.html", {"customer_record": customer_record})
    else:
        messages.success(request, "YOu Must Be")
        return redirect("home")


def delete_record(request, pk):
    delete_record = Record.objects.get(id=pk)
    delete_record.delete()
    messages.success(request, f"Account delete for! Successfully.")
    return redirect("home")


def add_record(request):
    form = AddRecordFrom(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "New Record ADD...")
                return redirect("home")
        return render(request, "crm/add_record.html", {"form": form})
    else:
        messages.success(request, "Must Be logged...")
        return redirect("home")


def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordFrom(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record Has been Updated!')
            return redirect('home')
        return render(request, "crm/update_record.html", {"form": form})
    else:
        messages.success(request, "Must Be logged...")
        return redirect("home")
        
        
        