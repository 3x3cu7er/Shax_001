from django.urls import path
from . import views
urlpatterns = [
    path("", views.x1, name="main"),
    path("", views.x2, name="landing"),
    path("", views.x3, name="records"),
    path("", views.x4, name="update"),
    path("", views.x5, name="mornitor"),
    path("", views.x6, name=""),
    path("", views.x7, name=""),
    path("", views.x8, name=""),
    path("", views.x9, name=""),
    path("", views.x10 , name=""),
]
