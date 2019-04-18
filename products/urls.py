from django.urls import path
from . import views


# Paths to different views
urlpatterns = [
    path('', views.home),
    path('products/', views.index)
]
