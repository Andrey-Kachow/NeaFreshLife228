# Generated by Django 2.1.1 on 2018-11-23 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meal',
            name='time',
        ),
        migrations.AddField(
            model_name='meal',
            name='index',
            field=models.IntegerField(null=True),
        ),
    ]