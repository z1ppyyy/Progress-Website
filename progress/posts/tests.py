from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from users.models import Profile
from .models import Post
from datetime import datetime


class PostTest(TestCase):
    """
    Test creating posts
    """

    def setUp(self):
        self.user = User.objects.create_user(username="Dummy",
                                             email="dummy@gmail.com",
                                             password="password1234")
        self.user.save()
        self.client.login(username="Dummy", password="password1234")

    def test_create(self):
        response = self.client.post(reverse("progress"), {
            'progress': 'This is progress!',
            'hours': '1',
            'minutes': '0'
        })
        self.assertEqual(response.status_code, 302)

    def test_streak_calc(self):
        """
        Test if a streak is maintained, incremented or destroyed when
        a post is created.
        """
        self.client.post(reverse("progress"), {
            'progress': 'This is another post!',
            'hours': '1',
            'minutes': '0'
        })
        self.client.post(reverse("progress"), {
            'progress': 'Please dont work',
            'hours': '1',
            'minutes': '0'
        })
        self.client.post(reverse("progress"), {
            'progress': 'OMG its working :''(',
            'hours': '1',
            'minutes': '0'
        })
        # response = self.client.post(reverse("progress"), {
        #     'progress': 'This is progress!',
        #     'hours': '1',
        #     'minutes': '0'
        # })
        # self.assertEqual(response.status_code, 302)
        # print(Profile.objects.get(id=self.client))
