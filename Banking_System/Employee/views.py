from django.shortcuts import render
from Customer.models import Customer, Accounts, DepositsWithdrawals
from django.contrib import messages
from datetime import date

def employee_home(request):
    return render(request, 'employee.html')

def add_customer(request):
    cust = Customer()
    account = Accounts()

    cust.id = request.POST['id']
    cust.name = request.POST["Name"]
    cust.Phone_no = request.POST["Phone_Number"]
    cust.Street_add = request.POST["Street_address"]
    cust.City = request.POST["City"]
    cust.State = request.POST["State"]
    cust.Zipcode = request.POST["Zip_Code"]
    cust.Image = request.FILES["Image"]
    cust.save()

    account.Ac_no = request.POST["Account_Number"]
    account.Ac_balance = request.POST["Balance"]
    account.Ac_type = request.POST["Account_Type"]
    account.Trans_limit = request.POST["Transaction_Limit"]
    account.Start_date = date.today()
    account.Customer = cust
    account.save()

    
    messages.success(request, "Customer Added Successfully")
    return render(request, 'employee.html')

def remove_account(request):
    try:
        id = request.POST["Account_Number"]
        account = Accounts.objects.get(Ac_no = id)
    except Exception as e:
        return render(request, 'Error.html', {'message':'Account Number'})
    
    account.delete()
    return render(request, 'employee.html')

def add_account(request):
    try:
        cust_id = request.POST["id"]
        cust = Customer.objects.get(id = cust_id)
    except Exception as e:
        return render(request, 'Error.html', {'message':'Customer'})
    
    account = Accounts()
    account.Ac_no = request.POST["Account_Number"]
    account.Ac_balance = request.POST["Balance"]
    account.Ac_type = request.POST["Account_Type"]
    account.Trans_limit = request.POST["Transaction_Limit"]
    account.Start_date = date.today()
    account.Customer = cust
    account.save()
    return render(request, 'employee.html')

def emp_search_customer(request):
    try:
        cust_id = request.POST["cust_search"]
        cust = Customer.objects.get(id = cust_id)
    except Exception as e:
        return render(request, 'Error.html', {'message':'Customer'})
    
    accounts = Accounts.objects.filter(Customer = cust_id)
    return render(request, 'employee.html', {'Customer_select': 0, 'Customer_Info':cust,'accounts_Info':accounts})

def update_cust_details(request):
    try:
        cust_id = request.POST["id"]
        cust = Customer.objects.get(id = cust_id)
    except Exception as e:
        return render(request, 'Error.html', {'message':'Customer'})
    

    cust.name = request.POST["name"]
    cust.Phone_no = request.POST["Phone_no"]
    cust.Street_add = request.POST["Street_add"]
    cust.City = request.POST["City"]
    cust.State = request.POST["State"]
    cust.Zipcode = request.POST["Zipcode"]

    cust.save()
    return render(request, 'employee.html')




def withdraw_cash(request):
    acc = int(request.POST['Account_no'])
    amount = int(request.POST['amount'])

    account = Accounts.objects.get(Ac_no = acc)
    account.Ac_balance = account.Ac_balance - amount
    account.save()

    withdraw = DepositsWithdrawals()
    withdraw.Account_no = account
    withdraw.date = date.today()
    withdraw.amount = 0 - amount

    withdraw.save()
    return render(request, 'employee.html')

def deposit_cash(request):
    acc = int(request.POST['Account_no'])
    amount = int(request.POST['amount'])

    account = Accounts.objects.get(Ac_no = acc)
    account.Ac_balance = account.Ac_balance + amount
    account.save()

    deposit = DepositsWithdrawals()
    deposit.Account_no = account
    deposit.date = date.today()
    deposit.amount = amount

    deposit.save()
    return render(request, 'employee.html')



# Create your views here.
