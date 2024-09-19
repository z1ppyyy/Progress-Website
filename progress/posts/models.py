from django.db import models
from datetime import date, datetime, timedelta
from django.contrib.auth.models import User
from users.models import Profile


class Post(models.Model):
    """Table of posts"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True)
    progress = models.CharField(max_length=900)
    hours = models.IntegerField()
    minutes = models.IntegerField()
    date = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Automatically set title to "current date progress" before saving
        current_date = date.today().strftime('%B %d')
        self.title = f"{current_date} progress"
        super(Post, self).save(*args, **kwargs)

        # If it's saved, update the streak
        profile_object = Profile.objects.get(user=self.user)  # Get the current user

        post_objects = Post.objects.filter(user=self.user)[::-1]  # Get the posts from the user

        # The logic will check if the time between posts is 1 day or less
        # if its more than 1 day then the streak is lost
        try:
            time_diff = post_objects[0].date - post_objects[1].date
            if time_diff.days > 1:
                profile_object.kill_streak()
                return None
            if time_diff.days <= 0:
                return None
            profile_object.inc_streak()

        except IndexError:
            return None

    def __str__(self):
        return f"{self.user.username} - {self.progress[:20]}"

    class Meta:
        ordering = ['date']  # date order so newest is first
