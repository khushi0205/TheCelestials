from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, default="Awesome BLogs" )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to='images/')


    def __str__(self):
        return self.title + '|' + str(self.author)


class Comments(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    def get_absolute_url(self):
        return reverse('blogs')

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)
