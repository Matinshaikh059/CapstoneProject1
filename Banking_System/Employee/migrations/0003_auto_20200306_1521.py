# Generated by Django 3.0.2 on 2020-03-06 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0002_employee_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='Image',
            field=models.ImageField(upload_to='Emp_Images'),
        ),
    ]