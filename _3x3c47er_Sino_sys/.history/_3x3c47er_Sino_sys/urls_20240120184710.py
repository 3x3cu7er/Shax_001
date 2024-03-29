"""_3x3c47er_Sino_sys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("_hadez_.urls")),
    path("xterminal/", include("_hadez_.urls")),
    path('main/', include('_hadez_.urls')),
    path('update-my-data/', include('_hadez_.urls')),
    path('records/', include('_hadez_.urls')),
    path('menu/', include('_hadez_.urls')),
    path('monitor/', include('_hadez_.urls')),
    path('dash_content_overview/', include('_hadez_.urls')),
    path('platform/', include('_hadez_.urls')),
]
