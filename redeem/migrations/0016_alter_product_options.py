# Generated by Django 4.1.7 on 2023-04-11 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('redeem', '0015_alter_product_options_alter_sos_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['id']},
        ),
    ]
