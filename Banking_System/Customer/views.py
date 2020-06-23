from django.shortcuts import render,redirect
from .models import Accounts, Customer, Customer_Request, Transfers, DepositsWithdrawals
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
    

def transfer_fund(request):
    cust = request.POST["Customer"]
    sender = int(request.POST["sender_acc_no"])
    reciever = int(request.POST["reciever_acc_no"])
    amount = int(request.POST["Amount"])

    s_account = Accounts.objects.get(Ac_no = sender)
    try:
        r_account = Accounts.objects.get(Ac_no = reciever)
    except Exception as e:
        return HttpResponse("Wrong Account Number")
    
    if((s_account.Ac_balance - amount)< 0):
        return HttpResponse("Balance is low")
    else:
        s_account.Ac_balance = s_account.Ac_balance - amount
        r_account.Ac_balance = r_account.Ac_balance + amount

        s_account.save()
        r_account.save()

        t = Transfers()
        t.date = date.today()
        t.from_account = s_account
        t.to_account = r_account
        t.amount = amount
        t.save()

        return render(request, 'customer.html', {'Customer_Info': cust, 'account': s_account})


def statements(request):
    custid = request.GET["custid"]
    acc_no = int(request.GET["account_no"])

    customer = Customer.objects.get(id = custid)
    account = Accounts.objects.get(Ac_no = acc_no)

    desposits = DepositsWithdrawals.objects.filter(Account_no = acc_no)
    l = []
    for d in desposits:
        x = []
        x.append(str(d.date))
        x.append(str(d.Account_no.Ac_no))
        if(d.amount < 0):
            x.append("withdrawal")
        else:
            x.append("deposit")
        x.append(str(d.amount))
        l.append(x)

    send = Transfers.objects.filter(from_account = acc_no)
    receive = Transfers.objects.filter(to_account = acc_no)

    for s in send:
        x = []
        x.append(str(s.date))
        x.append(str(s.from_account.Ac_no))
        x.append("transfered to {0}".format(s.to_account.Ac_no))
        x.append(str(0 - s.amount))
        l.append(x)

    for r in receive:
        x = []
        x.append(str(r.date))
        x.append(str(r.to_account.Ac_no))
        x.append("transfered to {0}".format(s.from_account.Ac_no))
        x.append(str(r.amount))
        l.append(x)

    l.sort()

   


    return JsonResponse(l, safe = False)








# Create your views here.
