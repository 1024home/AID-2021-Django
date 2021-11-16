# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/11/7 上午10:53
# @Author : 白铎
# @Email : ohh_1024@163.com
# @File : views.py
# @Software: PyCharm


from django.shortcuts import render, HttpResponse
from django.views.decorators.cache import cache_page
import time


def index(request):
    return render(request, 'index.html')


@cache_page(120)
def test_cache(request):
    time.sleep(3)

    t = time.time()
    return HttpResponse(f'当前时间戳:{t}')
