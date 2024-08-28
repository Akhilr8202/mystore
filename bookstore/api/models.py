from django.db import models

# Create your models here.

class books(models.Model):
    name=models.CharField(unique=True,max_length=100)
    price=models.PositiveIntegerField()
    description=models.CharField(max_length=200)
    category=models.CharField(max_length=100)
    image=models.ImageField(null=True)

    def __str__(self):
        return self.name