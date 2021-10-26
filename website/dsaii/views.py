from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from django.http import HttpResponseRedirect
from .models import Post
from django.core.mail import send_mail
from django.conf import settings
import datetime
class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class Blogs(ListView):
    model = Post
    template_name = 'blogs.html'

class Article(DetailView):
    model = Post
    template_name = 'article.html'


class Team(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'about.html')
class Login(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')