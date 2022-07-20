from django.db import models
from django.urls import reverse
from datetime import date
RIMS = (
    ('S', 'Salt'),
    ('SG', 'Sugar'),
    ('NO', 'No Rim'),
)
# Create your models here.

class Tequila(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'tequila_id': self.id})

class Taste(models.Model):
    date = models.DateField('drinking time')
    rims = models.CharField(
        max_length=2,
        choices=RIMS,
        default=RIMS[0][0],
    )

    tequila = models.ForeignKey(Tequila, on_delete=models.CASCADE)

    def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
     return f"{self.get_rims_display()} on {self.date}"
    