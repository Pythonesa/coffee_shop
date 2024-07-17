from django.db import models


class Product(models.Model):
    name = models.TextField(max_length=100, verbose_name="Name")
    description = models.TextField(max_length=500, verbose_name="Description")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price")
    available = models.BooleanField(default=True, verbose_name="Available")
    photo = models.ImageField(
        upload_to="photos", blank=True, null=True, verbose_name="Photo"
    )

    def __str__(self):
        return self.name
