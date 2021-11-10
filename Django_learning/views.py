# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/11/7 上午10:53
# @Author : 白铎
# @Email : ohh_1024@163.com
# @File : views.py
# @Software: PyCharm


from django.shortcuts import render


def index(request):
    return render(request, 'index.html')
