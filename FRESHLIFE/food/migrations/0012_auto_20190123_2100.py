# Generated by Django 2.1.1 on 2019-01-23 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0011_food_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/food/'),
        ),
    ]