from django.db import models

class MenuItem(models.Model):
    restaurant_id = models.IntegerField()
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(blank=True)

    def __str__(self):
        return f"{self.name} (Restaurant ID: {self.restaurant_id})"
