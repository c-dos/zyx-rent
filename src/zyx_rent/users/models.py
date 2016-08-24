from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Property(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    description = models.TextField()
    day_payment = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(31), MinValueValidator(1)]
    )
    price = models.DecimalField(default=None, max_digits=6, decimal_places=2)
    owner = models.ForeignKey(User)
    tenant = models.ForeignKey('Tenant', default=None)


class Tenant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    user = models.ForeignKey(User, default=None)
