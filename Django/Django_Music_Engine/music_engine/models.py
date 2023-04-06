from django.db import models
from django.contrib.auth.models import User


class MusicalMaterial(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    TYPE_CHOICES = (('altaveu', 'ALTAVEU'),
                    ('micròfon', 'MICRÒFON'),
                    ('percussió', 'PERCUSSIÓ'),
                    ('corda', 'CORDA'),
                    ('vent', 'VENT'),
                    ('amplificador', 'AMPLIFICADOR'))
    type = models.CharField(choices=TYPE_CHOICES, max_length=100)

    def __str__(self):
        return self.name


class MusicalStudio(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    capacity = models.IntegerField()
    TYPE_CHOICES = (
        ('ensaig', 'ENSAIG'),
        ('enregistrar', 'ENREGISTRAR')
    )
    type = models.CharField(choices=TYPE_CHOICES, max_length=100)

    incorporated_material = models.ManyToManyField(MusicalMaterial, blank=True)

    def __str__(self):
        return self.name


class ResourceManager(User):
    username = 'Gestor de Recursos'
    email = 'gestor@musicengine.com'
    password = 'gestor.musicengine'


class Technician(User):
    SPECIALITY_COICES = (('gravar', 'GRAVAR'),
                         ('assessorar', 'assessorar'),
                         ('gravar i assessorar', 'GRAVAR I ASSESSORAR'))
    speciality = models.CharField(choices=SPECIALITY_COICES, max_length=100)
