from django.db import models

# Create your models here.
class Branch(models.Model):
    city = models.CharField(max_length=32)
    postcode = models.CharField(max_length=9)
    capacity = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ['city']

class Car(models.Model):
    WITH_OPTIONS = [('BR','Branch'),('DR','Driver')]

    registration = models.CharField(unique=True,max_length=7)
    make = models.CharField(max_length=32)
    model = models.CharField(max_length=32)
    year = models.DateField()
    currently_with = models.CharField(choices=WITH_OPTIONS,default='Branch',max_length=2)
    assigned_to = models.IntegerField(default=0)
    in_service = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['registration']

class Driver(models.Model):
    name = models.CharField(max_length=128)
    date_of_birth = models.DateField()

    class Meta:
        ordering = ['name']