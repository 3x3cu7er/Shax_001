from django.urls import path
from . import views
urlpatterns = [
    path("/xterminal", views.x1, name="xterminal"),
    path("/xterminal", views.x2, name="xupdate"),
    path("/xbase", views.x3, name="xbase"),
    path("/xmain", views.x4, name="xmain"),
    path("/sys_manage", views.x5, name="sys_manage"),
    path("/root_parent", views.x6, name="root_parent"),
    path("/dash_content_overview", views.x7, name="dash_content_overview"),
    path("/xlanding", views.x8, name="xlanding"),
    path("/xhome", views.x9, name="xhome"),
    path("/board_confg", views.x10 , name="board_confg"),
    path("/temp_access_student", views.x11 , name="temp_access_student"),
    path("/xactive", views.x12 , name="xactive"),
    path("/xplatform", views.x13 , name="xplatform"),
    path("/sys_major", views.x14 , name="sys_major"),
]
