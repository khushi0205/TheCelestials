"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django import views
from django.conf.urls import url
from website.settings import STATIC_URL

from django.conf import settings
from django.conf.urls.static import static
from dsaii.views import Index, Blogs,Team, Login, Events
from django.views.static import serve
from django.conf.urls import url
#from dsaii.admin import site
#admin.site = site
#admin.autodiscover()
from dsaii.admin import d_site


urlpatterns = [
    path('admin/', admin.site.urls),
    path('DSAIIAdmin/', d_site.urls),
    path('', Index.as_view(), name='index'),
    path('Info/', Team.as_view(), name="about"),
    path('Login/', Login.as_view(), name="login"),
    path('TheCelestials/',include('dsaii.urls')),
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
