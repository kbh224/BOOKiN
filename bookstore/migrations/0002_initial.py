# Generated by Django 4.0.3 on 2022-04-10 10:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bookstore', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookstoremodel',
            name='user',
            field=models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, related_name='bookstore', to=settings.AUTH_USER_MODEL),
        ),
    ]
