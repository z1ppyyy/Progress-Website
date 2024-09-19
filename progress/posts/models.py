from django.db import models
from datetime import date
from django.contrib.auth.models import User


class Post(models.Model):
    """Table of posts"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True)
    progress = models.CharField(max_length=900)
    hours = models.IntegerField()
    minutes = models.IntegerField()
    date = models.DateField(default=date.today())

    def save(self, *args, **kwargs):
        # Automatically set title to "current date progress" before saving
        current_date = date.today().strftime('%B %d')
        self.title = f"{current_date} progress"
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} - {self.progress[:20]}"
