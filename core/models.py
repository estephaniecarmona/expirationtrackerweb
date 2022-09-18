from django.db import models

from django.utils import timezone

CATEGORY_CHOICES = (
    
    ('beauty', 'Beauty'),
    ('health', 'Health'),
    ('auto', 'Auto'),
    ('food', 'Food'),
    ('other','Other')
)


class Product(models.Model):
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    name = models.CharField(max_length=50)
    date_purchased = models.DateTimeField(default=timezone.now)
    expiration = models.DateTimeField(default=timezone.now)
    

    def get_absolute_url(self):
        return f"/product/{self.expiration}"

    class Meta: ordering = ["-name"]

    def __str__(self):
        return self.name
 
        


