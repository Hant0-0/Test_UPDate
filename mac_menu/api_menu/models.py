from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    calories = models.CharField(max_length=120)
    fats = models.CharField(max_length=120)
    carbs = models.CharField(max_length=120)
    proteins = models.CharField(max_length=120)
    unsaturated_fats = models.CharField(max_length=120)
    sugar = models.CharField(max_length=120)
    salt = models.CharField(max_length=120)
    portion = models.CharField(max_length=120)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']

