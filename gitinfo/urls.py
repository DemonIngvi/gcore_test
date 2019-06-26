from django.urls import path

from . import views

urlpatterns = [
    path('', views.gitinfo, name='gitinfo'),
]