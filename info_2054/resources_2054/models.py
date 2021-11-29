from django.db import models

class Department(models.Model):
    number = models.CharField(max_length=1)
    adress = models.CharField(max_length=30)
    admin = models.CharField(max_length=30)

    def __str__(self):
        return self.adress

class Computer(models.Model):
    TYPE_CHOICES = (
        ("PC", "PC"),
        ("Laptop", "Laptop"),
    )
    comp_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    brand = models.CharField(max_length=20)
    serial_number = models.CharField(max_length=20)
    owner = models.CharField(max_length=30)
    status = models.CharField(max_length=10, default="OK")
    dp = models.ForeignKey('Department', on_delete=models.CASCADE)

    def __str__(self):
        brand = self.brand 
        owner = self.owner
        return f"{brand} {owner}"

class InteractiveBoard(models.Model):
    brand = models.CharField(max_length=20)
    room = models.CharField(max_length=20)
    status = models.CharField(max_length=10, default="OK")
    dp = models.ForeignKey('Department', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.brand} | Room: {self.room}"

