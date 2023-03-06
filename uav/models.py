from django.db import models

# UAV class with necessary fields.
class UAV(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    weight = models.FloatField(max_length=50)
    category = models.CharField(max_length=50)
    rented = models.BooleanField()

    def __str__(self):
        return self.brand + ' ' + self.model
