# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/11/7 上午11:14
# @Author : 白铎
# @Email : ohh_1024@163.com
# @File : urls.py
# @Software: PyCharm


from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # 127.0.0.1:8000/bookstore/test_html
    path('test_html', views.test_html),
    # 127.0.0.1:8000/bookstore/test_static
    path('test_static', views.test_static),
    # 127.0.0.1:8000/bookstore/book_all
    path('book_all', views.book_all),
    # 127.0.0.1:8000/bookstore/delete_book
    path('delete_book', views.delete_book),
    # 127.0.0.1:8000/bookstore/update_book
    path('update_book/<int:bid>', views.update_book)
]
