# Generated by Django 4.0.3 on 2022-04-07 06:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('books', '0002_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='booksmodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bookreview',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review', to='books.booksmodel'),
        ),
        migrations.AddField(
            model_name='bookreview',
            name='writer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bookrentbyuser',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rent', to='books.booksmodel'),
        ),
        migrations.AddField(
            model_name='bookrentbyuser',
            name='user_rented',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rent', to=settings.AUTH_USER_MODEL),
        ),
    ]
