# Generated by Django 3.0.8 on 2020-08-08 20:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200808_1825'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tool',
            name='income',
        ),
        migrations.RemoveField(
            model_name='tool',
            name='urls',
        ),
    ]
