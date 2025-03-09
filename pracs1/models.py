from django.db import models

# recipe table
class Recipe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    ingredients = models.TextField()
    directions = models.TextField()

    def __str__(self):
        return self.name