# Generated by Django 2.1.1 on 2018-11-18 21:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0007_auto_20181118_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='ignored_by',
            field=models.ManyToManyField(blank=True, related_name='ignored_food', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='food',
            name='loved_by',
            field=models.ManyToManyField(blank=True, related_name='favourite_food', to=settings.AUTH_USER_MODEL),
        ),
    ]
