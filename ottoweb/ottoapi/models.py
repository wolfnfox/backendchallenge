from django.db import models

WITH_OPTIONS = [('BR','Branch'),('DR','Driver')]

# Create your models here.
class Car(models.Model):
    registration = models.CharField(unique=True,max_length=7)
    make = models.CharField(max_length=32)
    model = models.CharField(max_length=32)
    year = models.DateField()
    currently_with = models.CharField(choices=WITH_OPTIONS,default='Branch',max_length=2)
    in_service = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['registration']