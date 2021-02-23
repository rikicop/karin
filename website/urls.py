from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('details.html', views.details, name="details"),
    path('inmuebles.html', views.inmuebles, name="inmuebles"),
]