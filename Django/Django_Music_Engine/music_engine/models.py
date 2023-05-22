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
    price = models.IntegerField()

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


class technical_personnel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dni = models.CharField(max_length=30)
    #name = user.first_name
    #last_name = user.last_name
    specialty = models.CharField(max_length=50, default='none')
    experience = models.IntegerField(default=0, blank=True, null=True)

    #def __str__(self):
    #    return f"{self.name} {self.last_name}"


class Reserva(models.Model):
    usuari = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    sala = models.ForeignKey(MusicalStudio, on_delete=models.CASCADE, blank=False)
    material = models.ManyToManyField(MusicalMaterial, blank=True)
    tecnic = models.ForeignKey(technical_personnel, on_delete=models.CASCADE, blank=True, null=True)
    data = models.DateField(blank=False)
    hora_inici = models.TimeField(blank=False)
    hora_fi = models.TimeField(blank=False)
    reservat = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.usuari_id:
            self.usuari = self._default_user()
        super().save(*args, **kwargs)

    def _default_user(self):
        # Access the current user using the request object
        # You need to pass the request object to the save() method
        # For example, if you're calling save() from a view, pass the request object like this:
        # reserva.save(request=request)
        return self.request.user


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
    # name = models.ForeignKey(Assignment,on_delete=models.CASCADE)
    data = models.DateField(_("Date"), default=date.today)
    subject = models.ForeignKey(Reserva, on_delete=models.CASCADE)
    cost = models.DecimalField(max_digits=7, decimal_places=2)
    valid = models.BooleanField(default=True)

    def __str__(self):
        return f"Receip:{self.name} {self.data} {self.subject} {self.cost}"

    def url_route(self):
        return reverse('financial_data', args=[str(self.name)])


#class Receip2(models.Model):
 #   pass


class Client(models.Model):
    nom = models.CharField(max_length=100)
    cognom = models.CharField(max_length=100)
    correo_electronico = models.EmailField()

    def __str__(self):
        return f"{self.nom} {self.cognom}"


class Comercial(models.Model):
    name = models.CharField(max_length=50)
    cognom = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f"{self.name} {self.cognom}"


class Disponibility(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    date = models.DateField(default=date.today)
    # hours = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(8)], default=0)
    technician = models.ForeignKey(User, on_delete=models.CASCADE)
    available = models.BooleanField(default=True)

class Assesorament(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(default=date.today)
    telephone = models.CharField(max_length=9)
    client_name = models.CharField(max_length=255)
    motive = models.TextField(max_length=250)

