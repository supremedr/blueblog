from operator import mod
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    owner = models.ForeignKey(User, editable=False, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    slug = models.CharField(max_length=500, editable=False)

    def __str__(self):
        return self.title

class BlogPost(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.DO_NOTHING)
    # owner = models.ForeignKey(User, editable=False, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    body = models.TextField()
    is_published = models.BooleanField(default=False)
    slug = models.SlugField(max_length=500, editable=False)
    shared_to = models.ManyToManyField(Blog, related_name='shared_posts')

    def __str__(self):
        return self.title