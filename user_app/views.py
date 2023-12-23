from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from user_app.forms import AddBillRecordFrom
from user_app.models import BillRecord


def home(request):
    records = BillRecord.objects.all()

    # check to see if logging
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        # authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "User login Sucessfully")
            return redirect("home")
        else:
            messages.error(request, "Username or Password is incorrect.")
            return redirect("home")
    else:
        return render(request, "user/home.html", {"records": records})

def record_details(request):
    records = BillRecord.objects.all()

    # check to see if logging
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        # authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "User login Sucessfully")
            return redirect("home")
        else:
            messages.error(request, "Username or Password is incorrect.")
            return redirect("home")
    else:
        return render(request, "user/record_details.html", {"records": records})



def login_user(request):
    pass


def logout_user(request):
    logout(request)
    messages.success(request, "User logout Sucessfully...")
    return redirect("home")



def bill_record(request, pk):
    if request.user.is_authenticated:
        customer_record = BillRecord.objects.get(id=pk)
        return render(request, "user/record.html", {"customer_record": customer_record})
    else:
        messages.success(request, "YOu Must Be")
        return redirect("home")


def delete_record(request, pk):
    delete_record = BillRecord.objects.get(id=pk)
    delete_record.delete()
    messages.success(request, f"Account delete for! Successfully.")
    return redirect("home")


def add_record(request):
    form = AddBillRecordFrom(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "New Record ADD...")
                return redirect("home")
        return render(request, "user/add_record.html", {"form": form})
    else:
        messages.success(request, "Must Be logged...")
        return redirect("home")


def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = BillRecord.objects.get(id=pk)
        form = AddBillRecordFrom(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record Has been Updated!')
            return redirect('home')
        return render(request, "user/update_record.html", {"form": form})
    else:
        messages.success(request, "Must Be logged...")
        return redirect("home")
        
        
        