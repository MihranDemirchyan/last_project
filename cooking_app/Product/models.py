from django.db import models

from django.contrib.auth.models import User
from rest_framework import request


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    users = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    cuisine = models.ForeignKey("Cuisine", on_delete=models.CASCADE)
    product_elements = models.ForeignKey("Elements", on_delete=models.CASCADE)
    comments = models.ForeignKey("Comments",on_delete=models.PROTECT, null=True)

    def __str__(self):
        return f"{self.users}"


class Elements(models.Model):
    meat = models.TextField(null=True, blank=True)
    sauces = models.TextField(null=True, blank=True)
    spices = models.TextField(null=True, blank=True)
    vegetables = models.TextField(null=True, blank=True)
    fruits = models.TextField(null=True, blank=True)
    grocery = models.TextField(null=True, blank=True)
    dairy_prods = models.TextField(null=True, blank=True)
    greens = models.TextField(null=True, blank=True)


class Cuisine(models.Model):
    cuisine_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.cuisine_name}"


class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey("Product", on_delete=models.CASCADE)


class Comments(models.Model):
    comment = models.TextField(null=True, blank=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}"


class Favourite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey("Product", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}"
