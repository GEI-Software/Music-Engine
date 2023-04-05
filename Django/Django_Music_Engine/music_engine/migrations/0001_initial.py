# Generated by Django 4.0.3 on 2023-04-05 14:29

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='MusicalMaterial',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('altaveu', 'ALTAVEU'), ('micròfon', 'MICRÒFON'), ('percussió', 'PERCUSSIÓ'), ('corda', 'CORDA'), ('vent', 'VENT'), ('amplificador', 'AMPLIFICADOR')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ResourceManager',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Technician',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('speciality', models.CharField(choices=[('gravar', 'GRAVAR'), ('assessorar', 'assessorar'), ('gravar i assessorar', 'GRAVAR I ASSESSORAR')], max_length=100)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='MusicalStudio',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('capacity', models.IntegerField()),
                ('type', models.CharField(choices=[('ensaig', 'ENSAIG'), ('enregistrar', 'ENREGISTRAR')], max_length=100)),
                ('incorporated_material', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='music_engine.musicalmaterial')),
            ],
        ),
    ]