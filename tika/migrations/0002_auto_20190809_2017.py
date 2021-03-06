# Generated by Django 2.2.4 on 2019-08-09 11:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tika', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='condition',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='customer_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer_phone',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='location',
            field=models.CharField(max_length=100),
        ),
    ]
