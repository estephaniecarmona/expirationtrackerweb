# Generated by Django 2.2.13 on 2023-03-10 20:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20230310_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_purchased',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='product',
            name='expiration',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]