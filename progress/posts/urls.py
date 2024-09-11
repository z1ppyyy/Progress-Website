from django.urls import path
from . import views

urlpatterns = [
	# Create new url pattern
	path('', views.index, name="index"), #views.index means look for a function named index in views.py
    path('progress', views.progress, name="progress"),
]