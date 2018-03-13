#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'PJ'
__mtime__ = '2017/11/16'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""

import datetime
import re
import time
import urllib
from collections import OrderedDict
from urllib import request, parse

import os
from bs4 import BeautifulSoup
import socket

socket.setdefaulttimeout(5000)


headers1 = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
headers2 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}
headers3 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}


def getPhotoUrl(siteUrl) :
	"""

	:param siteUrl:
	:return:
	"""
	try:
		req = request.Request(siteUrl, headers= headers1 or headers2 or headers3)
		http = request.urlopen(req)
		bsObj = BeautifulSoup(http.read(), 'lxml')
		http.close()
	except UnicodeDecodeError as e:
		print("-----UnicodeDecodeError url", siteUrl)
	except urllib.error.URLError as e:
		print("-----URLError url", siteUrl)
	except socket.timeout as e:
		print("-----socket timeout:", siteUrl)

	i = 0
	# 申明字典
	photoDict = OrderedDict()
	print('正在连接到网站' + siteUrl)
	# print(bsObj.findAll('a', href=re.compile("^[/u2E80-/u9FFF]+$")))
	for tempList in bsObj.findAll('a', href=re.compile("http://www.mzitu.com/([0-9]+)")):
		i += 1
		photoUrl = tempList.attrs['href']
		photoName = tempList.get_text()
		photoDict[photoName] = photoUrl

	return photoDict

def CreateDirectory(DirectoryName):
	DirectoryNameNew = []
	if DirectoryName == '':
		DirectoryNameNew = '新建文件夹'
	for l in DirectoryName:
		if l != '/' and l != '\\':
			DirectoryNameNew.append(l)
		root = 'E:\\Python\\Python妹子图\\'
		path = root + "".join(DirectoryNameNew)
		try:
			os.makedirs(path)
		except Exception as e:
			print(root + "".join(DirectoryNameNew) + "已经存在")
		return path


if __name__ == '__main__':
	photoDict = getPhotoUrl("http://www.mzitu.com/all")
	for photoList in photoDict.keys():
		phth = CreateDirectory(photoList)