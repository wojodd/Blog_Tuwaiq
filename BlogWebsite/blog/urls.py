from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('blogs/blogdetails/<int:id>', views.blogdetails, name='blogdetails'),
    path('blogs/', views.blogs, name='blogs'),
    path('categories/', views.categories, name='categories'),
    path('comments/', views.comments, name='comments'),
    path('users/', views.users, name='users'),

]

