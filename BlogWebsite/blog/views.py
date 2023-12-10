from django.http import HttpResponse
from django.template import loader
from .models import Post, Category, Comment
from django.contrib.auth.models import User

from django.shortcuts import render

def index(request):
  all_post = Post.objects.all().values()
  template = loader.get_template('index.html')
  context = {
    'all_post': all_post,
  }
  return HttpResponse(template.render(context, request))



def categories(request):
  all_categories = Category.objects.all().values()
  template = loader.get_template('categories.html')
  context = {
    'all_categories': all_categories,
  }
  return HttpResponse(template.render(context, request))


def comments(request):
  all_comments = Comment.objects.all().values()
  template = loader.get_template('comments.html')
  context = {
    'all_comments': all_comments,
  }
  return HttpResponse(template.render(context, request))


def users(request):
  all_users = User.objects.all().values()
  template = loader.get_template('users.html')
  context = {
    'all_users': all_users,
  }
  return HttpResponse(template.render(context, request))

def blogs(request):
  all_blogs = Post.objects.all().values()
  template = loader.get_template('blogs.html')
  context = {
    'all_blogs': all_blogs,
  }
  return HttpResponse(template.render(context, request))


def blogdetails(request, id):
  details = Post.objects.get(id=id)
  template = loader.get_template('blogdetails.html')
  context = {
    'details': details,
  }
  return HttpResponse(template.render(context, request))

