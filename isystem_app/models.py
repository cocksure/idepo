from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator


class Position(models.Model):
    name = models.CharField(max_length=100)


class User(AbstractUser):
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=13, null=True, blank=True, unique=True)
    photo = models.ImageField(upload_to='user_photos/', null=True, blank=True,
                              validators=[FileExtensionValidator
                                          (allowed_extensions=['jpg', 'jpeg', 'png', 'heic', 'heif'])])


class MaterialGroup(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)


class MaterialType(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)


class Warehouse(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    firm = models.CharField(max_length=100)


class Material(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    group = models.ForeignKey(MaterialGroup, on_delete=models.CASCADE)
    type = models.ForeignKey(MaterialType, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='material_photos')
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_materials')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='updated_materials')


class Device(models.Model):
    agent = models.CharField(max_length=100)
    imei = models.CharField(max_length=100)
    comment = models.TextField()


class Client(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    agent = models.CharField(max_length=100)


class Unit(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)


class Currency(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)


class Dealer(models.Model):
    name = models.CharField(max_length=100)


class Brand(models.Model):
    name = models.CharField(max_length=100)
