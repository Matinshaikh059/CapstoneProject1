from django.shortcuts import render,redirect
from .models import Accounts, Customer, Customer_Request
from django.http import HttpResponse, JsonResponse
import time
import json
from datetime import date

def send_account(request):
    custid = request.GET['custid']
    accounts = Accounts.objects.filter(Customer = custid)
    l = ""
    for i in accounts:
        l = l + str(i.Ac_no) + ","

    return HttpResponse(l)


def new_account(request):
    acc_no = request.GET['account_no']
    custid = request.GET['custid']

    cust = Customer.objects.get(id = custid)
    accounts_info = Accounts.objects.get(Ac_no = acc_no)
    return render(request, 'customer.html', {'Customer_Info': cust, 'account': accounts_info})


def applypassbook(request):
    obj = Customer_Request()
    custid = request.POST['custid']
    cust = Customer.objects.get(id = custid)
    obj.custid = cust
    obj.date = date.today()
    obj.description = "passbook"

    obj.save()

    
    return HttpResponse('SUCCSEEFULLY APPLIED PASSBOOK')

def applychequebook(request):
    obj = Customer_Request()
    custid = request.POST['custid']
    cust = Customer.objects.get(id = custid)
    obj.custid = cust
    obj.date = date.today()
    obj.description = "chequebook"

    obj.save()
    return HttpResponse('SUCCESSFULLY APPLIED PASSBOOK')
    



# Create your views here.
