from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from crm_app.forms import UserSignUpForm, StaffRegisterForm
from django.contrib.auth.models import User
from crm_app.models import Staff


def main(request):
    # check to see if logging
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        # authenticate
        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_superuser:
            # Only allow superusers to log in
            login(request, user)
            messages.success(request, "You have been logged in!")
            return redirect("main")
        else:
            messages.error(request, "Username or Password is incorrect.")
            return redirect("main")
    else:
        return render(request, "crm/main.html")


def user(request):
    if request.user.is_authenticated:    
        records = User.objects.all()
        return render(request, "crm/user/user.html", {"records": records})
    else:
        messages.success(request, "Must Be logged...")
        return redirect("main")
        


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
        return render(request, "crm/user/register.html", {"form": form})


# bill record view


def add_staff(request):
    form = StaffRegisterForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            form = StaffRegisterForm(request.POST, request.FILES)
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "New Record ADD...")
                return redirect("staff_details")
            else:
                form = StaffRegisterForm()
        return render(request, "crm/staff/add_staff.html", {"form": form})
    else:
        messages.success(request, "Must Be logged...")
        return redirect("main")


def staff_details(request):
    if request.user.is_authenticated:
        staff = Staff.objects.all()
        return render(request, "crm/staff/staff_details.html", {"staff": staff})
    else:
        messages.success(request, "YOu Must Be")
        return redirect("main")


def staff(request, pk):
    if request.user.is_authenticated:
        customer_record = Staff.objects.get(id=pk)
        return render(
            request, "crm/staff/staff.html", {"customer_record": customer_record}
        )
    else:
        messages.success(request, "YOu Must Be")
        return redirect("main")


def update_staff(request, pk):
    if request.user.is_authenticated:
        current_record = Staff.objects.get(id=pk)
        form = StaffRegisterForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record Has been Updated!")
            return redirect("staff_details")
        
        return render(request, "crm/staff/update_staff.html", {"form": form})
    else:
        messages.success(request, "Must Be logged...")
        return redirect("main")


def delete_staff(request, pk):
    delete_record = Staff.objects.get(id=pk)
    delete_record.delete()
    messages.success(request, f"Account delete for! Successfully.")
    return redirect("staff_details")
