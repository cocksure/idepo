from django.db import models
from isystem_app.models import Material, Warehouse, Unit, User


class Incoming(models.Model):
    data = models.DateField()
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()


class Outgoing(models.Model):
    code = models.CharField(max_length=10)
    data = models.DateField()
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    type = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()