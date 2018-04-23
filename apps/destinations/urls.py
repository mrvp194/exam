from django.conf.urls import url, include
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index, name='index'),    
    url(r'^new$', views.new, name='new'),
    url(r'^create$', views.create, name='create'),
    url(r'^destination/(?P<id>[0-9]+)$', views.show, name='show'),
    url(r'^update/(?P<id>[0-9]+)$', views.update, name='update'),
]