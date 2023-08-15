from django.db import models

# Create your models here.


class Vehicle(models.Model):
    vehicle_type_choices = [
        ('two wheelers', 'Two wheelers'),
        ('three wheelers', 'Three wheelers'),
        ('four wheelers', 'Four wheelers')
    ]

    vehicle_number = models.CharField(max_length=155)
    vehicle_type = models.CharField(max_length=20, choices=vehicle_type_choices, default=None)
    vehicle_model = models.CharField(max_length=155)
    vehicle_description = models.TextField()

