# Generated by Django 3.0.2 on 2020-03-05 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='Phone_no',
            field=models.CharField(default=9876543210, max_length=10),
            preserve_default=False,
        ),
    ]
