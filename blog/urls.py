from django.conf.urls import patterns, url

from blog.views import EntryDetailView, EntryListView, CategoryDetailView


urlpatterns = patterns('',
                       url(r'^$', EntryListView.as_view(), name='blog.list'),
                       url(r'^post/(?P<slug>[^\.]+)$',
                           EntryDetailView.as_view(), name='blog.post'),
                       url(r'^category/(?P<slug>[^\.]+)$',
                           CategoryDetailView.as_view(), name='blog.category'),
)
