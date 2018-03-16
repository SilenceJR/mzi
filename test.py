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
import random
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
headers0 = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
headers2 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}
headers3 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}

headers4 = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0',
			'Referer':''
			}


def getPhotoUrl(siteUrl) :
	"""

	:param siteUrl:
	:return:
	"""
	bsObj = getBsObj(siteUrl)

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
		if l != '/' and l != " " and l != "\\" and l != "." and l != '?' and l != "？" and l != "\"" and l != "*" and l != "<" and l != ">" and l != ":":
			DirectoryNameNew.append(l)
	root = 'E:\\Python\\Python妹子图\\'
	path = root + "".join(DirectoryNameNew)
	try:
		os.makedirs(path)
	except Exception as e:
		print(root + "".join(DirectoryNameNew) + "已经存在")
	return path

def getBsObj(url):
	try :
		req = request.Request(url, headers=headers1 or headers2 or headers3 or headers0)
		html = request.urlopen(req)
		bsObj = BeautifulSoup(html.read(), 'lxml')
		html.close()

	except UnicodeDecodeError as e :
		print("-----UnicodeDecodeError url", photoUrl)
	except urllib.error.URLError as e :
		print("-----urlError url:", photoUrl)
	except socket.timeout as e :
		print("-----socket timout:", photoUrl)

	return bsObj


def getPhotoPageUrl(photoUrl):
	bsObj = getBsObj(photoUrl)

	numberList = []
	photoPageUrlList = []
	print("正在连接到%s,并解析该链接的页面链接"%photoUrl)
	if bsObj !='':
		numberMax = 1
		for pageList in bsObj.findAll('div', class_='pagenavi'):
			a = pageList.findAll('a', href=re.compile('http://www.mzitu.com/([0-9]+)/([0-9]*$)'))
			numberMax = a[-2].get_text()

			# for link in pageList.findAll('a', href=re.compile('http://www.mzitu.com/([0-9]+)/([0-9]*$)')):
			# 	url = link.attrs['href']
			# 	print(url)
			# 	number = url.replace(photoUrl + "/", "")
			# 	numberList.append(int(number))
		# numberMax = max(numberList)
		for i in range(1, int(numberMax) + 1) :
			if i != 1 :
				photoPageUrl = photoUrl + '/' + str(i)
			else :
				photoPageUrl = photoUrl
			photoPageUrlList.append(photoPageUrl)

	return photoPageUrlList

def isset(v):
   try :
     type (eval(v))
   except :
     return  0
   else :
     return  1

def getPhotoImageUrl(photoUrl, path, replaceurl):
	bsObj = getBsObj(photoUrl)

	number = photoUrl.replace(replaceurl + '/', '')

	if number == replaceurl :
		number = 1

	try:

		for temp in bsObj.findAll('div', class_='main-image'):
			for imag in temp.findAll('img'):
				imageUrl = imag.attrs['src']

				ImageName = imag.attrs['alt']
				ImageNameNew = []
				for l in ImageName:
					if l != '/' and l != " " and l != "\\" and l != "." and l != '?' and l != "？" and l != "\"" and l != "*" and l != "<" and l != ">" and l != ":":
						ImageNameNew.append(l)
				if len(ImageNameNew) != 0:
					print("正在下载文件：" + str(path) + "\\" + "".join(ImageNameNew) + str(number) + ".jpg")  # join将列表转为字符串

					down(imageUrl, str(path), "".join(ImageNameNew) + str(number) + ".jpg")
					#
					# try :
					# 	urlretrieve(imageUrl, str(path) + '\\' + ''.join(ImageNameNew) + str(number) + '.jpg', jindu)
					# 	while(True == jindu):
					# 		print("下载完成")
					# 		break
					# except Exception as e:
					# 	print(e)
					# 	time.sleep(10)
	except Exception as e:
		print(e)

def down(imageUrl, path, imageName):
	if os.path.isfile(path + '/' + imageName) :
		print("文件已下载， 跳过中。。。")
	else:
		headers4['Referer'] = imageUrl
		html = request.urlopen(request.Request(imageUrl, headers=headers4))
		f = open(path + '/' + imageName, 'wb')
		f.write(html.read())
		f.close()


# urlretrieve()的回调函数，显示当前的下载进度
# a为已经下载的数据块
# b为数据块大小
# c为远程文件的大小
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

def get_ip_list(self):
	print("正在获取代理列表...")
	url = 'http://www.xicidaili.com/nn/'
	html = request.get(url=url, headers=self.headers).text
	soup = BeautifulSoup(html, 'lxml')
	ips = soup.find(id='ip_list').find_all('tr')
	ip_list = []
	for i in range(1, len(ips)):
		ip_info = ips[i]
		tds = ip_info.find_all('td')
		ip_list.append(tds[1].text + ':' + tds[2].text)
	print("代理列表抓取成功.")
	return ip_list

def get_random_ip(self,ip_list):
    print("正在设置随机代理...")
    proxy_list = []
    for ip in ip_list:
        proxy_list.append('http://' + ip)
    proxy_ip = random.choice(proxy_list)
    proxies = {'http': proxy_ip}
    print("代理设置成功.")
    return proxies


if __name__ == '__main__':
	photoDict = getPhotoUrl("http://www.mzitu.com/all")
	# proxies = get_random_ip(get_ip_list())
	for photoList in photoDict.keys():
		path = CreateDirectory(photoList)
		photoPageUrl = getPhotoPageUrl(photoDict.get(photoList))
		for photoUrl in photoPageUrl:
			getPhotoImageUrl(photoUrl, path, photoDict.get(photoList))