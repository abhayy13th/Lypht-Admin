# Generated by Django 4.1.3 on 2023-04-02 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('redeem', '0005_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='tags',
            field=models.ManyToManyField(to='redeem.tag'),
        ),
    ]