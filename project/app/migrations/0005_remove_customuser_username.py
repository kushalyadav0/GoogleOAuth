# Generated by Django 5.2.2 on 2025-06-12 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_name_customuser_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='username',
        ),
    ]
