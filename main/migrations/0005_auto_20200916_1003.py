# Generated by Django 3.1.1 on 2020-09-16 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20200808_2038'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tool',
            name='mail',
        ),
        migrations.AddField(
            model_name='tool',
            name='name',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
