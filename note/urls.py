# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/11/14 下午12:10
# @Author : 白铎
# @Email : ohh_1024@163.com
# @File : urls.py
# @Software: PyCharm

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('add_note', views.add_view)
]
