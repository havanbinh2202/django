# Generated by Django 4.2.6 on 2023-10-22 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_dt_projects', '0005_shippingaddress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingaddress',
            name='mobile',
            field=models.IntegerField(max_length=200, null=True),
        ),
    ]
