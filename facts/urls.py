from django.urls import path

from . import views

app_name = "facts"

urlpatterns = [
    path('', views.home, name="home"),
    path('artist/<str:let>', views.artists, name="home"),
    path('song/<str:let>', views.songs, name="home"),
    ]