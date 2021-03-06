from django.db import models

class Employee(models.Model):
    id = models.CharField(primary_key=True,max_length= 8)
    name = models.CharField(max_length=20)
    Phone_no = models.CharField(max_length=10)
    Street_add = models.CharField(max_length=50)
    City = models.CharField(max_length=15)
    State = models.CharField(max_length=30)
    Zipcode = models.CharField(max_length=6)
    Department = models.CharField(choices = (("Teller","Teller"),("Customer Service","Customer Service"),("Loan Servicing","Loan Servicing"),("Cash Management","Cash Management"),("Electronic Banking","Electronic Banking"),("Mortage Banking","Mortage Banking")), max_length=20)
    Salary = models.BigIntegerField()
    Image = models.ImageField(upload_to="Emp_Images")

    class Meta:
        db_table = "Employee"


# Create your models here.
