# Generated by Django 4.0.3 on 2022-04-07 06:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('like', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='likemodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddConstraint(
            model_name='likemodel',
            constraint=models.UniqueConstraint(fields=('user', 'book'), name='unique_user_book'),
        ),
    ]
