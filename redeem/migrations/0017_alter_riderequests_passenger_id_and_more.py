# Generated by Django 4.1.7 on 2023-05-26 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('redeem', '0016_alter_product_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='riderequests',
            name='passenger_id',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='riderequests',
            name='rider_id',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
