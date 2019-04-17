from django.urls import path
from . import views


# Paths to different views
urlpatterns = [
    path('', views.index),
    path('new', views.new)
]
