# Generated by Django 4.1.7 on 2023-04-10 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('redeem', '0010_riderequests'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rider',
            name='bike_details',
        ),
        migrations.AddField(
            model_name='rider',
            name='bike_color',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='rider',
            name='bike_model',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='rider',
            name='bike_number',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.DeleteModel(
            name='BikeDetails',
        ),
    ]
