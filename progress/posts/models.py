from django.db import models
from datetime import date
from django.core.validators import MaxValueValidator, MinValueValidator

current_date = date.today().strftime('%B %d')

# Create your models here.
class Post(models.Model):
    """Table of posts"""
    title = current_date
    progress = models.CharField(max_length=900)
    hours = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(24)], default=0
    )
    minutes = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(60)], default=0
    )
    