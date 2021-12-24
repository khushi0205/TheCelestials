from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView, CreateView
from django.http import HttpResponseRedirect
from .models import Post, Comments, Event, EveComm
from django.urls import reverse_lazy, reverse
from django.core.mail import send_mail
from django.conf import settings
import datetime
from .forms import CommentForm, CF
class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

class Quiz(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'quiz.html')

class Inaug(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'inauguration.html')

class Blogs(ListView):
    model = Post
    template_name = 'blogs.html'

class Events(ListView):
    #model = Event
    #template_name = 'events.html'
    def get(self, request, *args, **kwargs):
        return render(request, 'events.html')


class Eve(ListView):
    model = Event
    template_name = 'eve.html'


class Article(DetailView):
    model = Post
    template_name = 'article.html'



class Team(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'about.html')
class Login(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'l1.html')

class AddC(CreateView):
     model = Comments
     form_class = CommentForm
     template_name = 'addcomm.html'
     #fields = '__all__'
     def form_valid(self, form):
         form.instance.post_id = self.kwargs['pk']
         return super().form_valid(form)
     succes_url = reverse_lazy('blogs')


class EveC(CreateView):
    model = EveComm
    form_class = CF
    template_name = 'addcomm.html'

    # fields = '__all__'
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    succes_url = reverse_lazy('events')
