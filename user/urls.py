# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/11/13 下午6:01
# @Author : 白铎
# @Email : ohh_1024@163.com
# @File : urls.py
# @Software: PyCharm

from django.urls import path
from . import views

urlpatterns = [
    # 127.0.0.1:8000/user/register
    path('register', views.register),
    # 127.0.0.1:8000/user/login
    path('login', views.login),
    # 127.0.0.1:8000/user/logout
    path('logout', views.logout),
]
