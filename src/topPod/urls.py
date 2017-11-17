from django.contrib import admin
from django.conf.urls import *
from django.contrib import admin
from topPod import views
from config.settings import base_settings
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.Home.as_view(), name = 'home'),
    url(r'^(?P<slug>[\w-]+)/$', views.Sports.as_view(), name = 'sports'),
    url(r'^1/search/$', views.AllPods.as_view(), name = 'pods'),
]
