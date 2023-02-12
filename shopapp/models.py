from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=255, unique=True)
    picture = models.ImageField(upload_to="image/%Y/%m/%d", unique=True)
    description = models.TextField(max_length=2000, unique=True)

class Comment(models.Model):
    author = models.CharField(max_length=255, unique=True)
    text = models.TextField(max_length=2000, unique=True)