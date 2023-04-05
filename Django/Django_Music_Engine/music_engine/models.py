from django.db import models
from django.contrib.auth.models import User


class MusicalMaterial(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    type = models.CharField(choices=('ENSAIG', 'ENREGISTRAR'))

    # incorporated_material = models.ForeignKey(MusicalMaterial, on_delete=CASCADE)
    # compatible_material = models.ForeignKey(MusicalMaterial, on_delete=CASCADE)

    def __str__(self):
        return self.name


class MusicalStudio(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    type = models.CharField(choices=('ENSAIG', 'ENREGISTRAR'))
    
    incorporated_material = models.ForeignKey(MusicalMaterial, on_delete=models.CASCADE)

    # compatible_material = models.ForeignKey(MusicalMaterial, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
