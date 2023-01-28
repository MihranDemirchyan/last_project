from django.db import models

from django.contrib.auth.models import User
from rest_framework import request


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    cuisine = models.ForeignKey("Cuisine", on_delete=models.CASCADE, null=True)
    product_elements = models.ManyToManyField("Elements")
    # comments = models.ForeignKey("Comments",on_delete=models.PROTECT, null=True)

    def __str__(self):
        return f"{self.user}"


class Elements(models.Model):
    name = models.CharField(max_length=50, null=True)
    # product = models.ManyToManyField("Product")


class Cuisine(models.Model):
    cuisine_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.cuisine_name}"


class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey("Product", on_delete=models.CASCADE)


class Comments(models.Model):
    comment = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product = models.ManyToManyField("Product")

    def __str__(self):
        return f"{self.comment}"


class Favourite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product = models.ManyToManyField("Product")

    def __str__(self):
        return f"{self.user}"
