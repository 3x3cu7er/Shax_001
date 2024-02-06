from django.urls import path
from . import views
urlpatterns = [
    path("", views.x1, name="xterminal"),
    path("", views.x2, name="xupdate"),
    path("", views.x3, name="xbase"),
    path("", views.x4, name="xmain"),
    path("", views.x5, name="sys_manage"),
    path("", views.x6, name="root_parent"),
    path("", views.x7, name="dash_content_overview"),
    path("", views.x8, name="xlanding"),
    path("", views.x9, name="xhome"),
    path("", views.x10 , name="board_confg"),
    path("", views.x11 , name="temp_access_student"),
    path("", views.x12 , name="xactive"),
    path("", views.x13 , name="temp_access_student"),
    path("", views.x14 , name="temp_access_student"),
]
