# Generated by Django 2.1.1 on 2018-11-25 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0009_auto_20181121_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='unit',
            field=models.CharField(default='g', max_length=45),
        ),
    ]
