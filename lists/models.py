from django.db import models
from item.models import Item

class List(models.Model):
    name = models.CharField(max_length=100)
    items = models.ManyToManyField(Item)
    price = models.DecimalField(max_digits = 5, decimal_places=2)
    def __str__(self):
        return self.name
