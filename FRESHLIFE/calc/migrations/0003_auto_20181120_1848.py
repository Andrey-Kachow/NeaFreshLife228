# Generated by Django 2.1.1 on 2018-11-20 18:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0002_latest_inputs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='latest_inputs',
            name='id',
        ),
        migrations.AlterField(
            model_name='latest_inputs',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
