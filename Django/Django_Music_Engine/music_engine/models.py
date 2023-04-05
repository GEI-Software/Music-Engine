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

    incorporated_material = models.ForeignKey(MusicalMaterial, on_delete=models.CASCADE, blank=True)
    #incorporated_material2 = models.ForeignKey(MusicalMaterial, on_delete=models.CASCADE, blank=True)
    #incorporated_material3 = models.ForeignKey(MusicalMaterial, on_delete=models.CASCADE, blank=True)
    #incorporated_material4 = models.ForeignKey(MusicalMaterial, on_delete=models.CASCADE, blank=True)
    #compatible_material = models.ForeignKey(MusicalMaterial, on_delete=models.CASCADE, blank=True)
    #compatible_material2 = models.ForeignKey(MusicalMaterial, on_delete=models.CASCADE, blank=True)
    #compatible_material3 = models.ForeignKey(MusicalMaterial, on_delete=models.CASCADE, blank=True)
    #compatible_material4 = models.ForeignKey(MusicalMaterial, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.name

    #def inc_mat(self):
    #    return [self.incorporated_material, self.incorporated_material2,
    #            self.incorporated_material3, self.incorporated_material4]

    #def comp_mat(self):
    #    return [self.compatible_material, self.compatible_material2,
    #            self.compatible_material3, self.compatible_material4]


class ResourceManager(User):
    username = 'Gestor de Recursos'
    email = 'gestor@musicengine.com'
    password = 'gestor.musicengine'


class Technician(User):
    SPECIALITY_COICES = (('gravar', 'GRAVAR'),
                         ('assessorar', 'assessorar'),
                         ('gravar i assessorar', 'GRAVAR I ASSESSORAR'))
    speciality = models.CharField(choices=SPECIALITY_COICES, max_length=100)
