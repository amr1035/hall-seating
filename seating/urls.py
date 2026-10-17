from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search/", views.search, name="search"),
    path("view/", views.view_table, name="view"),
    path("api/guests/", views.guests, name="guests"),
    path("data.json", views.download, name="download"),
]
