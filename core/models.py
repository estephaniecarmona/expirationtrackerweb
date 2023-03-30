from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User
from  datetime import datetime, date


CATEGORY_CHOICES = (
    
    ('beauty', 'Beauty'),
    ('health', 'Health'),
    ('auto', 'Auto'),
    ('food', 'Food'),
    ('other','Other')
)


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    name = models.CharField(max_length=25)
    date_purchased = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    expiration = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    

    def get_absolute_url(self):
        return f"/product/{self.expiration}"

    class Meta: ordering = ["-name"]

    def __str__(self):
        return self.name
 
        


