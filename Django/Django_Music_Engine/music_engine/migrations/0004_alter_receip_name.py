# Generated by Django 4.0.3 on 2023-05-02 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_engine', '0003_receip2_receip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receip',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]