from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from utilities.models import CreatedUpdatedModel


class Property(CreatedUpdatedModel):
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


class Tenant(CreatedUpdatedModel):
    name = models.CharField(max_length=100, default=None)
    email = models.EmailField()
    user = models.ForeignKey(User, blank=True)
    phone = models.CharField(max_length=100, blank=True)
    bank = models.CharField(max_length=100, blank=True)
    account = models.CharField(max_length=100, blank=True)


    def __unicode__(self):
        return self.name


