from django.conf.urls import url, include
from rest_framework import routers
from myblog.views import list_view, detail_view, UserViewSet, GroupViewSet


urlpatterns = [
    url(r'^$', list_view, name="blog_index"),
    # url(r'^posts/(?P<post_id>\d+)/$', list_view, name="blog_detail"),
    url(r'^posts/(?P<post_id>\d+)/$', detail_view, name="blog_detail"),
]
