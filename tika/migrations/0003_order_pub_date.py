# Generated by Django 2.2.4 on 2019-08-08 12:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tika', '0002_auto_20190807_2227'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published'),
            preserve_default=False,
        ),
    ]
