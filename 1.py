#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'PJ'
__mtime__ = '2018/3/3'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""
from urllib import request, parse
import chardet
import lxml
from bs4 import BeautifulSoup

http = "http://qlm.tuoxinjz.cn/index.php?g=search&m=apih&a=check"
headers = {
			  'User-Agent' :  # 'Mozilla/5.0 (Linux; Android 7.0; PRO 5 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043906 Mobile Safari/537.36 MicroMessenger/6.6.3.1260(0x26060339) NetType/WIFI Language/zh_CN'
				  'Mozilla/5.0 (Linux; Android 7.0; PRO 5 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043906 Mobile Safari/537.36 MicroMessenger/6.6.3.1260(0x26060339) NetType/WIFI Language/zh_CN',
			  # 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 MicroMessenger/6.5.2.501 NetType/WIFI WindowsWechat QBCore/3.43.691.400 QQBrowser/9.0.2524.400',
			  'Referer' : 'http://qlm.tuoxinjz.cn/index.php?g=search&m=apih&a=index', 'Connection' : 'keep-alive',
			  'Content-Type' : 'application/x-www-form-urlencoded',
			  'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,image/wxpic,image/sharpp,image/apng,*/*;q=0.8',
				# 'Accept-Encoding' : 'gzip, deflate',
	'Accept-Language': 'zh-CN,en-US;q=0.8'}

proxy_info = {'host' : '110.72.28.9:8123'}


def goHttp (name, phone, idcard) :
	data = {'name' : name, 'phone' : phone, 'idcard' : idcard}

	# opener = request.build_opener(request.ProxyHandler(proxy_info))
	#
	# request.install_opener(opener)

	data = parse.urlencode(data).encode('utf-8')
	# data = bytes(parse.urlencode(data), encoding='utf-8')
	print(data)
	# data = parse.urlencode(data).encode('utf-8')
	req = request.Request(http, data=data, headers=headers)
	urlopen = request.urlopen(req)
	print(urlopen.info())
	if urlopen.getcode() == 302 :
		response = BeautifulSoup(urlopen.read(), 'lxml')
	else:
		print("未找到302")

	# response = request.urlopen(req)
	# print(response.info())
	# page = response.read()


	print(response)


if __name__ == '__main__' :
	# name = input("姓名 : ")
	# phone = input("手机号 : ")
	# idcard = input("身份证号 : ")
	name = '王维朕'
	phone = '15890425955'
	idcard = '411324199707220011'

	goHttp(name, phone, idcard)
