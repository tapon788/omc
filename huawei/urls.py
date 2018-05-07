__author__ = 't.paul'
from django.conf.urls import url,include
from .views import hello_world

urlpatterns = [
    url(r'^hello/', hello_world),
]
