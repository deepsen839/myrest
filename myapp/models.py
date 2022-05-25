from statistics import mode
from django.db import models

# Create your models here.
class Breed(models.Model):
    SIZE_OF_CHOICES = [
        ('Tiny', 'Tiny'),
        ('Small', 'Small'),
        ('Medium', 'Medium'),
        ('Large', 'Large'),
    ]
    STATUS_CHOICES = (
            (0,0),
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5),
        )
    name = models.CharField(max_length=200)
    size = models.CharField(
        max_length=10,
        choices=SIZE_OF_CHOICES,
        default='Tiny',
    )
    friendliness = models.IntegerField(default=0,choices=STATUS_CHOICES)
    trainability = models.IntegerField(default=0,choices=STATUS_CHOICES)
    sheddingamount = models.IntegerField(default=0,choices=STATUS_CHOICES)
    exerciseneeds = models.IntegerField(default=0,choices=STATUS_CHOICES)
    
    def __str__(self):
        return self.name

class Dog(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(null=True)    
    gender = models.CharField(max_length=10)
    color = models.CharField(max_length=10)
    favoritefood = models.CharField(max_length=10)
    favoritetoy = models.CharField(max_length=10)
    breed = models.ForeignKey(Breed,related_name='breed',on_delete=models.CASCADE)

    