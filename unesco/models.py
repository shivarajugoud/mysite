from django.db import models

# Create your models here.
class State(models.Model):
    name = models.CharField(max_length = 128)
    def __str__(self):
        return self.state
class Region(models.Model):
    name = models.CharField(max_length=128)
    def __str__(self):
        return self.region
class Iso(models.Model):
    name = models.CharField(max_length=2)
    def __str__(self):
        return self.iso
class Category(models.Model):
    name = models.CharField(max_length=128)
    def __str__(self):
        return self.name
class Site(models.Model):
    name =models.CharField(max_length=128)
    year = models.IntegerField(null = True)
    longitude = models.DecimalField(max_digits=19, decimal_places=10,null=True)
    latitude = models.DecimalField(max_digits=19, decimal_places=10,null=True)
    area_hectares = models.DecimalField(max_digits=19,decimal_places=10,null = True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True)
    states = models.ForeignKey(State, on_delete=models.CASCADE,null=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE,null=True)
    iso = models.ForeignKey(Iso, on_delete=models.CASCADE,null=True)
    description = models.TextField(null=True)
    justification = models.TextField(null=True)

    def __str__(self):
        return self.name
