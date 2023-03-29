from django.db import models

class Hero(models.Model):
    name = models.CharField(max_length=50)
    bio = models.CharField(max_length=200)

class Ability(models.Model):
    main_ability = models.ForeignKey(Hero, on_delete=models.CASCADE)

# Create your models here.
