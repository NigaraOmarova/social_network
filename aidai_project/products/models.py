from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Movie(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='movie')
    rating = models.IntegerField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

