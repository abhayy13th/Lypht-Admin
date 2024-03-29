# Generated by Django 4.1.7 on 2023-04-06 03:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('redeem', '0008_remove_product_category_remove_product_image_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='BikeDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bike_number', models.CharField(max_length=200, null=True)),
                ('bike_model', models.CharField(max_length=200, null=True)),
                ('bike_color', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usertype', models.CharField(choices=[('Rider', 'Rider'), ('Passenger', 'Passenger')], max_length=200, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(choices=[('Electronics', 'Electronics'), ('Clothing', 'Clothing'), ('Food', 'Food'), ('Beauty', 'Beauty'), ('Sports', 'Sports'), ('Books', 'Books'), ('Other', 'Other')], max_length=200, null=True),
        ),
        migrations.CreateModel(
            name='Rider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rider_id', models.CharField(max_length=200, null=True)),
                ('name', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('phone', models.CharField(max_length=200, null=True)),
                ('password', models.CharField(max_length=200, null=True)),
                ('newRideStatus', models.CharField(max_length=200, null=True)),
                ('points', models.IntegerField(null=True)),
                ('bike_details', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='redeem.bikedetails')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='redeem.usertag')),
            ],
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passenger_id', models.CharField(max_length=200, null=True)),
                ('name', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('phone', models.CharField(max_length=200, null=True)),
                ('password', models.CharField(max_length=200, null=True)),
                ('points', models.IntegerField(null=True)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='redeem.usertag')),
            ],
        ),
    ]
