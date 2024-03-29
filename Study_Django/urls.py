"""Study_Django URL Configuration

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
# MEDIA_URL과 업로드 연결하기 위해 추가
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path("",views.index),
    path("pyburger/",include("pyburger.urls")),
    path("blog/",include("blog.urls")),
    path("admin/", admin.site.urls),
]

#사용자 업로드 파일 URL 연결...
urlpatterns += static(
    prefix=settings.MEDIA_URL,  #MEDIA_URL 접두어가 들어오면
    document_root = settings.MEDIA_ROOT, #MEDIA_ROOT에서 찾아서 돌려줄것
)