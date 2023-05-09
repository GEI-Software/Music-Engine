# Generated by Django 4.0.3 on 2023-05-09 09:49

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('music_engine', '0005_remove_hoursrecord_available'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disponibility',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('date', models.DateField(default=datetime.date.today)),
                ('available', models.BooleanField(default=True)),
                ('technician', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
