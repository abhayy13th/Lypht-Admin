# Generated by Django 4.1.3 on 2023-04-02 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('redeem', '0006_order_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='tags',
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(to='redeem.tag'),
        ),
    ]
