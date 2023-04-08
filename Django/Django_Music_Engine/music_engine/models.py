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


class Reserva(models.Model):
    usuari = models.ForeignKey(User, on_delete=models.CASCADE)
    sala = models.ForeignKey(MusicalStudio, on_delete=models.CASCADE)
    data = models.DateField()
    hora_inici = models.TimeField()
    hora_fi = models.TimeField()
    reservat = models.BooleanField(default=False)


class technical_personnel(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dni = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name} {self.last_name}"
