from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("views2", views.snowstorm, name="snowstorm "),
]