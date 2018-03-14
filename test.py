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
from urllib.request import urlretrieve

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

def getPhotoPageUrl(photoUrl):

	try:
		req = request.Request(photoUrl, headers=headers1 or headers2 or headers3)
		html = request.urlopen(req)
		bsObj = BeautifulSoup(html.read(), 'lxml')
		html.close()

	except UnicodeDecodeError as e:
		print("-----UnicodeDecodeError url", photoUrl)
	except urllib.error.URLError as e :
		print("-----urlError url:", photoUrl)
	except socket.timeout as e :
		print("-----socket timout:", photoUrl)

	numberList = []
	photoPageUrlList = []
	print("正在连接到" + photoUrl + ",并解析该链接的页面链接")
	if bsObj !='':
		for pageList in bsObj.findAll('div', class_='pagenavi'):
			for link in pageList.findAll('a', href=re.compile('http://www.mzitu.com/([0-9]+)/([0-9]*$)')):
				url = link.attrs['href']
				number = url.replace(photoUrl + "/", "")
				numberList.append(int(number))
		numberMax = max(numberList)
		for i in range(1, numberMax + 1):
			photoPageUrl = photoUrl + '/' + str(i)
			photoPageUrlList.append(photoPageUrl)
	return photoPageUrlList

def getPhotoImageUrl(photoUrl, path, replaceurl):
	try:
		req = request.Request(photoUrl, headers=headers1 or headers2 or headers3)
		html = request.urlopen(req)
		bsObj = BeautifulSoup(html.read(), 'lxml')
		html.close()

		number = photoUrl.replace(replaceurl + '/', '')
		for temp in bsObj.findAll('div', class_='main-image'):
			for image in temp.finAll('img'):
				imageUrl = image.attes['src']

				ImageName = image.attes['alt']
				ImageNameNew = []
				for l in ImageName:
					if l != '/' and l != " " and l != "\\" and l != "." :
						ImageNameNew.append(l)
				if len(ImageNameNew) != 0:
					print("正在下载文件：" + str(path) + "\\" + "".join(ImageNameNew) + str(number) + ".jpg")  # join将列表转为字符串
					try :
						urlretrieve(imageUrl, str(path) + '\\' + ''.join(ImageNameNew) + str(number) + '.jpg', jindu)
						while(True == jindu):
							print("下载完成")
							break
					except Exception as e:
						time.sleep(10)
	except UnicodeDecodeError as e:
		print("-----UnicodeDecodeError url", photoUrl)
	except urllib.error.URLError as e :
		print("-----urlError url:", photoUrl)
	except socket.timeout as e :
		print("-----socket timout:", photoUrl)
		print("正在获取" + photoUrl + "的图片链接")


def jindu(a, b, c):
    if not a:
        print("连接打开")
    if c < 0:
        print("要下载的文件大小为0")
    else:
        global myper
        per = 100 * a * b / c

        if per > 100:
            per = 100
        myper = per
        print("myper0=" + str(myper))
        print("当前下载进度为：" + '%.2f%%' % per)
    if per == 100:
        return True



if __name__ == '__main__':
	photoDict = getPhotoUrl("http://www.mzitu.com/all")
	for photoList in photoDict.keys():
		path = CreateDirectory(photoList)
		photoPageUrl = getPhotoPageUrl(photoDict.get(photoList))
		for photoUrl in photoPageUrl:
			getPhotoImageUrl(photoUrl, path, photoDict.get(photoUrl))