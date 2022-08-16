from django.db import models

class Product(models.Model):
    category = models.CharField(max_length=30)
    name = models.CharField(max_length=50)
    expiration = models.CharField(max_length=50)

    class Meta: ordering = ["-name"]

    def __str__(self):
        return self.name
 
        


