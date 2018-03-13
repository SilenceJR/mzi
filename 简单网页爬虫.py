#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'PJ'
__mtime__ = '2018/1/4'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""
import urllib.request
import requests
from bs4 import BeautifulSoup

#网址
url = "http://www.douban.com/"

#请求
# request = urllib.request.Request(url)
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")

# response = urllib.request.urlopen(request)

# data = response.read()

# data = data.decode("UTF-8")

# 打印结果
html = soup.body.select('div[class="albums"]')
for i in html:
	print(i.img + ':' + i.text)

# 打印爬取网页的各类信息

# print(type(response))
# print(response.geturl())
# print(response.info())
# print(response.getcode())

