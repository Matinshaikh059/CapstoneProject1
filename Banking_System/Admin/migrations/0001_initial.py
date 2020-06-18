# Generated by Django 3.0.2 on 2020-03-05 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('Admin_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('Admin_name', models.CharField(max_length=20)),
                ('Street_add', models.CharField(max_length=50)),
                ('City', models.CharField(max_length=15)),
                ('State', models.CharField(max_length=30)),
                ('Zipcode', models.CharField(max_length=6)),
            ],
            options={
                'db_table': 'Admin',
            },
        ),
    ]
