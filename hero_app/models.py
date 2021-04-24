from django.db import models


class Hero(models.Model):
    hero_name = models.CharField(max_length=250) 
    full_name = models.CharField(max_length=250) 
    universe = models.CharField(max_length=10) 

    def __str__(self): 
        return self.hero_name
