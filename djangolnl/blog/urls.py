from django.conf.urls.defaults import patterns, include, url
from djangolnl.blog.views import home

urlpatterns = patterns('',
    url(r'^$', home),
)
