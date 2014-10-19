from django.contrib.auth.models import User
from django.db import models
from django.db.models import permalink

try:
    from ckeditor.fields import RichTextField as TextField
except ImportError:
    from django.db.models import TextField


class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __unicode__(self):
        return self.title

    @permalink
    def get_absolute_url(self):
        return ('blog.category', None, {'slug': self.slug})


class Entry(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = TextField()
    posted = models.DateTimeField(db_index=True, auto_now_add=True)
    published = models.BooleanField(default=True)
    category = models.ManyToManyField(Category)
    author = models.ForeignKey(User)

    def __unicode__(self):
        return self.title

    @permalink
    def get_absolute_url(self):
        return ('blog.post', None, {'slug': self.slug})
