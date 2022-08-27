from django.db import models

from django.utils import timezone


class Product(models.Model):
    category = models.CharField(max_length=30)
    name = models.CharField(max_length=50)
    date_purchased = models.DateTimeField(default=timezone.now)
    expiration = models.CharField(max_length=50)
    

    def get_absolute_url(self):
        return f"/product/{self.expiration}"

    class Meta: ordering = ["-name"]

    def __str__(self):
        return self.name
 
        


