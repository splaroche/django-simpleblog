from django.db import models
from django.db.models import permalink


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
    body = models.TextField()
    posted = models.DateTimeField(db_index=True, auto_now_add=True)
    published = models.BooleanField(default=True)
    category = models.ManyToManyField(Category)

    def __unicode__(self):
        return self.title

    @permalink
    def get_absolute_url(self):
        return ('blog.post', None, {'slug': self.slug})
