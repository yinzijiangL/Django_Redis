from django.conf.urls import include, url
from django.contrib import admin
from app01 import views

urlpatterns = [

    url(r'^index$', views.index),

    url(r'^show_news/(\d+)/(\d+)$', views.show_news),

    url(r'^show_news2/(?P<category>\d+)/(?P<page_no>\d+)$', views.show_news2),

    url(r'^do_post$', views.do_post),

    url(r'^post$', views.post),

    url(r'^test_redirect$', views.test_redirect),

    url(r'^get_json$', views.get_json),

    url(r'^do_json$', views.do_json),


]
