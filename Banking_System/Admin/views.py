from django.shortcuts import render
from Employee.models import Employee
from django.contrib import messages
from Customer.models import Customer, Accounts

def admin_home(request):
    return render(request, 'admin.html')

def add_employee(request):
    emp = Employee()

    emp.id = request.POST['id']
    emp.name = request.POST["Name"]
    emp.Phone_no = request.POST["Phone_Number"]
    emp.Street_add = request.POST["Street_address"]
    emp.City = request.POST["City"]
    emp.State = request.POST["State"]
    emp.Zipcode = request.POST["Zip_Code"]
    emp.Department = request.POST["Department"]
    emp.Salary = request.POST["Salary"]
    emp.Image = request.FILES["Image"]
    emp.save()
    
    return render(request, 'admin.html', {'messages':'Employee Added Successfully'})

def remove_employee(request):

    try:
        id = request.POST["Employee_Id"]
        employee = Employee.objects.get(id = id)
    except Exception as e:
        return render(request, 'Error.html',{'message': 'Employee'})
    
    
    employee.delete()
    return render(request, 'admin.html')

def search_customer(request):
    cust_id = request.POST["cust_search"]
    try:
        cust = Customer.objects.get(id = cust_id)
    except Exception as e:
        return render(request, 'Error.html',{'message': 'Customer'})
    
    
    accounts = Accounts.objects.filter(Customer = cust_id)
    return render(request, 'admin.html', {'Customer_select': 0, 'Customer_Info':cust,'accounts_Info':accounts})


def set_transaction_limit(request):
    ac_no = request.POST["account_no"]
    limit = request.POST["transaction_limit"]

    try:
        account = Accounts.objects.get(Ac_no = ac_no)
    except Exception as e:
        return render(request, 'Error.html',{'message': 'Account Number'})
    account.Trans_limit = limit
    account.save()

    return render(request, 'admin.html',{'messages':"Transaction Limit set"})


def search_employee(request):
    try:
        emp_id = request.POST["emp_search"]
        emp = Employee.objects.get(id = emp_id)
    except Exception as e:
        return render(request, 'Error.html',{'message': 'Employee'})
    
    return render(request, 'admin.html', {'Employee_select':0,'Emp_Info':emp})


def update_employee_details(request):
    try:
        emp_id = request.POST["id"]
        emp = Employee.objects.get(id = emp_id)
    except Exception as e:
        return render(request, 'Error.html',{'message': 'Employee'})
    emp_id = request.POST["id"]
    emp = Employee.objects.get(id = emp_id)
    emp.name = request.POST["name"]
    emp.Phone_no = request.POST["Phone_no"]
    emp.Street_add = request.POST["Street_add"]
    emp.City = request.POST["City"]
    emp.State = request.POST["State"]
    emp.Zipcode = request.POST["Zipcode"]
    emp.Department = request.POST["Department"]
    emp.Salary = request.POST["Salary"]
    emp.save()
    return render(request, 'admin.html')


# Create your views here.
