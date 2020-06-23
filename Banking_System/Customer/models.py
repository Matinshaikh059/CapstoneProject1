from django.db import models

class Customer(models.Model):
    id = models.CharField(primary_key=True ,max_length=9)
    name = models.CharField(max_length=20)
    Phone_no = models.CharField(max_length=10)
    Street_add = models.CharField(max_length=50)
    City = models.CharField(max_length=15)
    State = models.CharField(max_length=30)
    Zipcode = models.CharField(max_length=6)
    Image = models.ImageField(upload_to="Cust_Images")

    class Meta:
        db_table = "Customer"

class Accounts(models.Model):
    Ac_no = models.BigIntegerField(primary_key=True)
    Ac_type = models.CharField(choices=(('Savings','Savings'),('Current','Current')), max_length=7)
    Start_date = models.DateField()
    Ac_balance = models.BigIntegerField()
    Trans_limit = models.BigIntegerField()
    Customer = models.ForeignKey(Customer, on_delete = models.CASCADE)

    class Meta:
        db_table = "Accounts"


class Customer_Request(models.Model):
    custid = models.ForeignKey(Customer, on_delete = models.CASCADE)
    description = models.CharField(choices=(('passbook','passbook'),('chequebook','chequebook')), max_length=11)
    date = models.DateField()

    class Meta:
        db_table = "Customer_Request"

class DepositsWithdrawals(models.Model):
    date = models.DateField()
    Account_no = models.ForeignKey(Accounts, on_delete = models.CASCADE) 
    amount = models.IntegerField()

    class Meta:
        db_table = "Depositswithdrawals"

class Transfers(models.Model):
    date = models.DateField()
    from_account = models.ForeignKey(Accounts, on_delete = models.CASCADE, related_name = "from_account") 
    to_account = models.ForeignKey(Accounts, on_delete = models.CASCADE, related_name = "to_account")
    amount = models.IntegerField()

    class Meta:
        db_table = "Transfers"

# Create your models here.
