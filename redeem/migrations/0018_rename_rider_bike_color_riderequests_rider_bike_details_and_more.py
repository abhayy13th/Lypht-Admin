# Generated by Django 4.1.7 on 2023-05-26 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('redeem', '0017_alter_riderequests_passenger_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='riderequests',
            old_name='rider_bike_color',
            new_name='rider_bike_details',
        ),
        migrations.RemoveField(
            model_name='riderequests',
            name='rider_bike_model',
        ),
        migrations.RemoveField(
            model_name='riderequests',
            name='rider_bike_number',
        ),
    ]