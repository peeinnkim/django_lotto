"""site_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views -> 주로 사용
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views -> 클래스 기반으로 자동 생성
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf -> 세부 url을 더 큰 카테고리 url에게 넘길 때 사용
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from lotto import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.index), # lotto
    path('hello/', views.hello, name='hello_main'),
    path('lotto/', views.index, name='lotto_main'),
    path('lotto/new/', views.post, name='new_lotto'),
    path('lotto/<int:lottokey>/detail/', views.detail, name='detail'),
]
# 참고: <a href='{% url hello_main %}'>~~~</a> -> {%%}: django 명령어
