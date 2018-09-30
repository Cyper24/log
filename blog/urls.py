from django.urls import path, re_path
from django.views.generic import ListView, DetailView
from blog.models import post
from django.conf.urls import handler404, handler500
from . import views

urlpatterns = [
    path('', ListView.as_view(queryset=post.objects.all().order_by("-date")[:25], template_name="blog.html")),
    re_path(r'^(?P<pk>\d+)$', DetailView.as_view(model=post, template_name='post.html')),
]


handler404 = views.handler404
handler500 = views.handler500