# Generated by Django 3.0.2 on 2020-03-07 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='Image',
            field=models.ImageField(default=0, upload_to='Cust_Images'),
            preserve_default=False,
        ),
    ]