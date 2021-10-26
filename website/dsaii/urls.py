from django.contrib import admin
from django.urls import path
from django import views
from django.conf.urls import url
from website.settings import STATIC_URL

from django.conf import settings
from django.conf.urls.static import static
from dsaii.views import Index, Blogs,Team, Login
from django.views.static import serve
from django.conf.urls import url


urlpatterns = [
    path('', Blogs.as_view(), name="blogs"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
