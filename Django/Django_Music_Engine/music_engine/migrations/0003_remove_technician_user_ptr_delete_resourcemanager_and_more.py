# Generated by Django 4.0.3 on 2023-04-06 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music_engine', '0002_remove_musicalstudio_incorporated_material_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='technician',
            name='user_ptr',
        ),
        migrations.DeleteModel(
            name='ResourceManager',
        ),
        migrations.DeleteModel(
            name='Technician',
        ),
    ]