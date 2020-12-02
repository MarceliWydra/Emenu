from django.contrib import admin
from django.db import models

class BaseModel(models.Model):
    """
    Base model having functionality common across different models
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Menu(BaseModel):
    """
    Represents single menu card
    """
    name = models.CharField(db_index=True, max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Course(BaseModel):
    """
    Represents single course in menu
    """
    name = models.CharField(db_index=True, max_length=255, unique=False)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField(null=False)
    is_vege = models.BooleanField(default=False)
    preparation_time = models.DurationField(null=False)
    cards = models.ManyToManyField(Menu)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name

