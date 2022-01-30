from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Band(models.Model):
    def __str__(self) -> str:
        return f'{self.name}'

    class Gender(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'

    name = models.fields.CharField(max_length=100)
    gender = models.fields.CharField(choices=Gender.choices, max_length=5)
    bibliography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2022)]
    )
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)


class Listing(models.Model):
    class Type(models.TextChoices):
        RECORDS = "DK"
        CLOTHING = "CL"
        POSTERS = "PO"
        DIVERS = "DIV"

    title = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=500)
    sold = models.fields.BooleanField(default=False)
    year = models.fields.IntegerField(null=True)
    type = models.fields.CharField(choices=Type.choices, max_length=5)
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)
