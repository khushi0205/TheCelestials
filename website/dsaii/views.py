from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
#from .models import MenuItem, Category, OrderModel
from django.core.mail import send_mail
from django.conf import settings
import datetime
class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')
class Blogs(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'blogs.html')

class Team(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'about.html')