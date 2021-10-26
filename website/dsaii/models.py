from django.db import models
from django.contrib.auth.models import User

class Comment(models.Model):
    post = models.ForeignKey(User, related_name="comments", on_delete= models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
            return '%s - %s' % (self.post.title, self.name)