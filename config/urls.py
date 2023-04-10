"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.template.defaulttags import url
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

import accounts.views
import board.views

urlpatterns = [
                  path('', include('allauth.urls')),
                  path('admin/', admin.site.urls),
                  path('board/like/<int:bid>', board.views.like),
                  path('board/rest_list', board.views.rest_list),
                  path('board/register', board.views.register),
                  path('', board.views.list),
                  path('board/read/<int:bid>', board.views.read),
                  path('board/delete/<int:bid>', board.views.delete),
                  path('board/update/<int:bid>', board.views.update),
                  path('user/', include('allauth.urls')),
                  path('user/profile', accounts.views.profile),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
