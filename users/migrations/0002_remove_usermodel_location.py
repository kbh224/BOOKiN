# Generated by Django 4.0.3 on 2022-04-07 06:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermodel',
            name='location',
        ),
    ]
