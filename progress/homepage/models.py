from django.db import models
from datetime import date

current_date = date.today().strftime('%B %d')

# Create your models here.
class Post(models.Model):
    """Table of posts"""
    title = current_date
    progress = models.CharField(max_length=900)
    spent = models.IntegerField(max_length=2)