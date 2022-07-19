from django.db import models

# Create your models here.
class Tequila(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.name