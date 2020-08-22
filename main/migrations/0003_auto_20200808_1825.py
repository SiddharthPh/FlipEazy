# Generated by Django 3.0.8 on 2020-08-08 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200806_0311'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tool',
            old_name='url',
            new_name='urls',
        ),
        migrations.RemoveField(
            model_name='tool',
            name='date_posted',
        ),
        migrations.RemoveField(
            model_name='tool',
            name='traffic',
        ),
        migrations.RemoveField(
            model_name='tool',
            name='user',
        ),
        migrations.AlterField(
            model_name='tool',
            name='mail',
            field=models.CharField(max_length=300),
        ),
    ]