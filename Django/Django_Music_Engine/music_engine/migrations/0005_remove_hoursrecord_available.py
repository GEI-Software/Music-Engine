# Generated by Django 4.0.3 on 2023-05-09 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music_engine', '0004_hoursrecord_available'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hoursrecord',
            name='available',
        ),
    ]