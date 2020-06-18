from django.shortcuts import render
from Customer.models import Customer, Accounts


def home(request):
    return render(request,'Home.html')

def direct(request):
    return render(request, 'admin.html')

def direct2(request):
    return render(request, 'employee.html')

def direct3(request):
    cust = Customer.objects.get(id = 'cust10001')

    accounts = Accounts.objects.filter(Customer = 'cust10001')
    
    return render(request, 'customer.html', {'Customer_Info': cust, 'account': accounts[0]})

# Create your views here.
