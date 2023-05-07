from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.urls import reverse
from django.utils.translation import gettext as _


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
    dni = models.CharField(max_length=30)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    specialty = models.CharField(max_length=50,default='none')
    experience = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return f"{self.name} {self.last_name}"
    
class Assignment(models.Model):
    studio = models.ForeignKey(MusicalStudio, on_delete=models.CASCADE)
    material = models.ForeignKey(MusicalMaterial, on_delete=models.CASCADE)
    technician = models.ForeignKey(technical_personnel, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return f"{self.studio} - {self.material} - {self.technician} - {self.date}"


class HoursRecord(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    date = models.DateField(default=date.today)
    hours = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(8)], default=0)
    technician = models.ForeignKey(User, on_delete=models.CASCADE)


class Receip(models.Model):
    name = models.CharField(max_length=100)
    #name = models.ForeignKey(Assignment,on_delete=models.CASCADE)
    data = models.DateField(_("Date"), default=date.today)
    subject = models.CharField(max_length=50)
    cost = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return  f"Receip:{self.name} {self.data} {self.subject} {self.cost}"

    def url_route(self):
        return reverse('financial_data', args=[str(self.name)])


class Receip2(models.Model):
    pass




