# Generated by Django 4.1.7 on 2023-04-10 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('redeem', '0012_remove_rider_bike_color_remove_rider_bike_model_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('phone', models.CharField(max_length=200, null=True)),
                ('rider_name', models.CharField(max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
