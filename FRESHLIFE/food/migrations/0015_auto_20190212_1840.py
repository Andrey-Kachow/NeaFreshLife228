# Generated by Django 2.1.1 on 2019-02-12 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0014_auto_20190212_1140'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='cholesterol',
            field=models.DecimalField(decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='food',
            name='monounsaturated',
            field=models.DecimalField(decimal_places=1, max_digits=3, null=True),
        ),
        migrations.AddField(
            model_name='food',
            name='polyunsaturated',
            field=models.DecimalField(decimal_places=1, max_digits=3, null=True),
        ),
        migrations.AddField(
            model_name='food',
            name='protein_quality',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='food',
            name='saturated_fat',
            field=models.DecimalField(decimal_places=1, max_digits=3, null=True),
        ),
    ]