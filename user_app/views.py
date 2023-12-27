from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from user_app.forms import (
    AddBillRecordFrom,
    AddYogaMemberFrom,
    AddMemberFrom,
    AddProductFrom,
    CashTransactionForm,
)
from user_app.models import BillRecord, YogaMember, Member,Product,CashTransaction
from crm_app.models import Stock
import datetime


def home(request):
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
        return render(request, "user/home.html")


def login_user(request):
    pass


def logout_user(request):
    logout(request)
    messages.success(request, "User logout Sucessfully...")
    return redirect("home")


# bill record view


def add_record(request):
    form = AddBillRecordFrom(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            form = AddBillRecordFrom(request.POST, request.FILES)
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "New Record ADD...")
                return redirect("record_details")
        else:
            form = AddBillRecordFrom()
        return render(request, "user/bill/add_record.html", {"form": form})
    else:
        messages.success(request, "Must Be logged...")
        return redirect("home")


def record_details(request):
    if request.user.is_authenticated:
        records = BillRecord.objects.all()
        return render(request, "user/bill/record_details.html", {"records": records})
    else:
        messages.success(request, "YOu Must Be")
        return redirect("home")


def bill_record(request, pk):
    if request.user.is_authenticated:
        customer_record = BillRecord.objects.get(id=pk)
        return render(
            request, "user/bill/record.html", {"customer_record": customer_record}
        )
    else:
        messages.success(request, "YOu Must Be")
        return redirect("home")


def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = BillRecord.objects.get(id=pk)
        form = AddBillRecordFrom(
            request.POST or None, request.FILES or None, instance=current_record
        )

        if form.is_valid():
            form.save()
            messages.success(request, "Record has been updated!")
            return redirect("record_details")

        return render(request, "user/bill/update_record.html", {"form": form})
    else:
        messages.success(request, "Must be logged in...")
        return redirect("home")


def delete_record(request, pk):
    delete_record = BillRecord.objects.get(id=pk)
    delete_record.delete()
    messages.success(request, f"Account delete for! Successfully.")
    return redirect("record_details")


# yoga member record view


def add_yoga(request):
    form = AddYogaMemberFrom(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            form = AddYogaMemberFrom(request.POST, request.FILES)
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "New Record ADD...")
                return redirect("yoga_details")
        else:
            form = AddYogaMemberFrom()
        return render(request, "user/yoga/add_yoga.html", {"form": form})
    else:
        messages.success(request, "Must Be logged...")
        return redirect("home")


def yoga_details(request):
    if request.user.is_authenticated:
        yoga_member = YogaMember.objects.all()
        return render(
            request, "user/yoga/yoga_details.html", {"yoga_member": yoga_member}
        )
    else:
        messages.success(request, "YOu Must Be")
        return redirect("home")


def yoga_member(request, pk):
    if request.user.is_authenticated:
        customer_record = YogaMember.objects.get(id=pk)
        return render(
            request, "user/yoga/yoga_member.html", {"customer_record": customer_record}
        )
    else:
        messages.success(request, "YOu Must Be")
        return redirect("home")


def update_yoga(request, pk):
    if request.user.is_authenticated:
        current_record = YogaMember.objects.get(id=pk)
        form = AddYogaMemberFrom(
            request.POST or None, request.FILES or None, instance=current_record
        )
        if form.is_valid():
            form.save()
            messages.success(request, "Record has been updated!")
            return redirect("yoga_details")

        return render(request, "user/yoga/update_yoga.html", {"form": form})
    else:
        messages.success(request, "Must be logged in...")
        return redirect("home")


def delete_yoga(request, pk):
    delete_record = YogaMember.objects.get(id=pk)
    delete_record.delete()
    messages.success(request, f"Account delete for! Successfully.")
    return redirect("yoga_details")


#  member record view


def add_member(request):
    form = AddMemberFrom(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            form = AddMemberFrom(request.POST, request.FILES)
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "New Record ADD...")
                return redirect("member_details")
        else:
            form = AddMemberFrom()
        return render(request, "user/member/add_member.html", {"form": form})
    else:
        messages.success(request, "Must Be logged...")
        return redirect("home")


def member_details(request):
    if request.user.is_authenticated:
        member = Member.objects.all()
        return render(request, "user/member/member_details.html", {"member": member})
    else:
        messages.success(request, "YOu Must Be")
        return redirect("home")


def member(request, pk):
    if request.user.is_authenticated:
        customer_record = Member.objects.get(id=pk)
        return render(
            request, "user/member/member.html", {"customer_record": customer_record}
        )
    else:
        messages.success(request, "YOu Must Be")
        return redirect("home")


def update_member(request, pk):
    if request.user.is_authenticated:
        current_record = Member.objects.get(id=pk)
        form = AddMemberFrom(
            request.POST or None, request.FILES or None, instance=current_record
        )

        if form.is_valid():
            form.save()
            messages.success(request, "Record has been updated!")
            return redirect("member_details")

        return render(request, "user/member/update_member.html", {"form": form})
    else:
        messages.success(request, "Must be logged in...")
        return redirect("home")


def delete_member(request, pk):
    delete_record = Member.objects.get(id=pk)
    delete_record.delete()
    messages.success(request, f"Account delete for! Successfully.")
    return redirect("member_details")


# stock details view
def stock_details_view(request):
    if request.user.is_authenticated:
        stock_view = Stock.objects.all()
        return render(
            request, "user/stock/stock_details.html", {"stock_view": stock_view}
        )
    else:
        messages.success(request, "YOu Must Be")
        return redirect("main")


def stock_view(request, pk):
    if request.user.is_authenticated:
        customer_record = Stock.objects.get(id=pk)
        return render(
            request, "user/stock/stock.html", {"customer_record": customer_record}
        )
    else:
        messages.success(request, "YOu Must Be")
        return redirect("main")


#  product record view


def add_product(request):
    form = AddProductFrom(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            form = AddProductFrom(request.POST, request.FILES)
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "New Record ADD...")
                return redirect("product_details")
        else:
            form = AddProductFrom()
        return render(request, "user/product/add_product.html", {"form": form})
    else:
        messages.success(request, "Must Be logged...")
        return redirect("home")


def product_details(request):
    if request.user.is_authenticated:
        product = Product.objects.all()
        return render(request, "user/product/product_details.html", {"product": product})
    else:
        messages.success(request, "YOu Must Be")
        return redirect("home")


def product(request, pk):
    if request.user.is_authenticated:
        customer_record = Product.objects.get(id=pk)
        return render(
            request, "user/product/product.html", {"customer_record": customer_record}
        )
    else:
        messages.success(request, "YOu Must Be")
        return redirect("home")


def update_product(request, pk):
    if request.user.is_authenticated:
        current_record = Product.objects.get(id=pk)
        form = AddProductFrom(
            request.POST or None, request.FILES or None, instance=current_record
        )

        if form.is_valid():
            form.save()
            messages.success(request, "Record has been updated!")
            return redirect("product_details")

        return render(request, "user/product/update_product.html", {"form": form})
    else:
        messages.success(request, "Must be logged in...")
        return redirect("home")


def delete_product(request, pk):
    delete_record = Product.objects.get(id=pk)
    delete_record.delete()
    messages.success(request, f"Account delete for! Successfully.")
    return redirect("product_details")



def cash_transaction_create(request):
    form = CashTransactionForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            form = CashTransactionForm(request.POST, request.FILES)
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Payment Sucessfully!....")
                return redirect("cash_transaction_list")
        else:
            form = CashTransactionForm()
        return render(request, "user/bill/cashtransaction_form.html", {"form": form})
    else:
        messages.success(request, "Must Be logged...")
        return redirect("home")


from django.db.models import Sum

def cash_transaction_list(request):
    queryset = CashTransaction.objects.all()
    payments = queryset.filter(transaction_type='Payment')
    pending = queryset.filter(transaction_type='Pending')

    # Calculate the sums
    total_payment = payments.aggregate(Sum('amount'))['amount__sum'] or 0
    total_pending = pending.aggregate(Sum('amount'))['amount__sum'] or 0

    # Calculate the difference
    difference = total_payment - total_pending
    
    context = {
        'object_list': queryset,
        'payments': payments,
        'pending': pending,
        'total_payment': total_payment,
        'total_pending': total_pending,
        'difference': difference,
    }

    template_name = "user/bill/cashtransaction_list.html"
    return render(request, template_name, context)