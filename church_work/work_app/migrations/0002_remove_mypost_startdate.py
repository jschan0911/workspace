# Generated by Django 4.0.6 on 2022-07-14 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('work_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mypost',
            name='startdate',
        ),
    ]
