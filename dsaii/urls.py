from django.contrib import admin
from django.urls import path
from django import views
from django.conf.urls import url
from website.settings import STATIC_URL

from django.conf import settings
from django.conf.urls.static import static
from dsaii.views import Index, Blogs,Team, Login, Article, AddC,Events, Eve, EComm
from django.views.static import serve
from django.conf.urls import url


urlpatterns = [
    path('Blogs/', Blogs.as_view(), name="blogs"),
    path('Article/<int:pk>', Article.as_view(), name = "article"),
    path('Article/<int:pk>/Add/', AddC.as_view(), name="addc" ),
    path('Events/', Events.as_view(), name="events"),
    path('Event/<int:pk>', Eve.as_view(), name="event"),
    path('Event/<int:pk>/Add/', EComm.as_view(), name="ecomm"),

              ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
