from django.db import models


# Create your models here.
class PokeMove(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class PokeAbility(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class PokeType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Pokemon(models.Model):
    pokemon_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=255)
    types = models.ManyToManyField(PokeType)
    moves = models.ManyToManyField(PokeMove)
    image = models.CharField(max_length=255)
    abilities = models.ManyToManyField(PokeAbility)

    def __str__(self):
        return f"{self.pokemon_id}-{self.name}"
