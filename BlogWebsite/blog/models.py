from django.db import models
from tkinter import CASCADE
from django.contrib.auth.models import User

class Category(models.Model):
    category_name = models.CharField(max_length=270)

class Post(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date_published = models.DateField()

class Comment(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateField()
    

    

