from django.urls import path
from . import views

urlpatterns = [
    # Create new url pattern
    path('', views.index, name="index"),  # views.index means look for a function named index in views.py
    path('progress', views.progress, name="progress"),
    path('post/<int:id>', views.post_id, name='post_id'),
    path('delete/<int:id>', views.delete_post, name="delete_post"),
    path('edit/<int:id>', views.edit_post, name="edit_post"),
]
