from django.db import models

class Admin(models.Model):
    Admin_id = models.CharField(primary_key=True, max_length=10)
    Phone_no = models.CharField(max_length=10)
    Admin_name = models.CharField(max_length=20)
    Street_add = models.CharField(max_length=50)
    City = models.CharField(max_length=15)
    State = models.CharField(max_length=30)
    Zipcode = models.CharField(max_length=6)

    class Meta:
        db_table = "Admin"



    

# Create your models here.
