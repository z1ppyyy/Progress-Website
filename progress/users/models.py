from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.png", upload_to="profile_pics")
    streak = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} Profile"

    def inc_streak(self, value=1):
        """
        Increment streak.

        :param int value(default=1): Value wanted to increment the streak by.

        :return: None.
        """
        self.streak += value
        self.save()

    def kill_streak(self):
        """
        Kill streak.

        :return: None.
        """
        self.streak = 0
        self.save()
