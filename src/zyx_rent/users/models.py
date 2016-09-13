from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.urlresolvers import reverse
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
    tenant = models.ForeignKey('Tenant', null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('property', args=[self.id])

    def to_csv(self):
        return ','.join([
            self.name,
            self.address,
            self.description,
            str(self.day_payment),
            str(self.price)
        ])


class Tenant(CreatedUpdatedModel):
    name = models.CharField(max_length=100, default=None)
    email = models.EmailField()
    user = models.ForeignKey(User, blank=True)
    phone = models.CharField(max_length=100, blank=True)
    bank = models.CharField(max_length=100, blank=True)
    account = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

    def to_csv(self):
        return ','.join([
            self.name,
            self.email,
            self.phone,
            self.bank,
            self.account
        ])

    def get_absolute_url(self):
        return reverse('tenant', args=[self.id])
