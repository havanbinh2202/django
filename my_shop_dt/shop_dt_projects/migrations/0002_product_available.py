# Generated by Django 4.2.6 on 2023-10-20 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_dt_projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='available',
            field=models.BooleanField(default=True),
        ),
    ]