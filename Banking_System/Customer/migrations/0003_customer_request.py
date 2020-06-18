# Generated by Django 3.0.2 on 2020-06-17 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0002_customer_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer_Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(choices=[('passbook', 'passbook'), ('chequebook', 'chequebook')], max_length=11)),
                ('date', models.DateField()),
                ('custid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Customer.Customer')),
            ],
            options={
                'db_table': 'Customer_Request',
            },
        ),
    ]
