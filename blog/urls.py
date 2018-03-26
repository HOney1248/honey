from django.conf.urls import url
from .views import post_list, post_new, post_detail,edit_post,delete_post

urlpatterns = [
    url(r'^$', post_list, name='post_list'),
    url(r'^new-post/$', post_new, name='anyword'),
    url(r'^post-details/(?P<pk>\d+)$', post_detail, name='anyword'),
    url(r'^edit-post/(?P<pk>\d+)$', edit_post, name='edit_post'),
    url(r'^Delete-post/(?P<pk>\d+)$', delete_post, name='delete_post'),
]

