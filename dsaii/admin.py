from django.contrib import admin
from .models import Post, Comments, Event, EveComm
from django.contrib.admin import AdminSite
from . import models
#admin.site.register(Post)
#admin.site.register(Comments)
#class MyAdminSite(AdminSite):
#    login_template = 'login.html'

#site = MyAdminSite()
#site.register(Post)
#site.register(Comments)

class DSAIIAdminArea(admin.AdminSite):
    site_header = 'DSAII Admin Area'
    login_template = 'login.html'

d_site = DSAIIAdminArea(name='DSAIIAdmin')
d_site.register(models.Post)
d_site.register(models.Comments)
d_site.register(models.Event)
d_site.register(models.EveComm)
