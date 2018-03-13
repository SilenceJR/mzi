#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'PJ'
__mtime__ = '2018/3/12'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""

from urllib import request, parse
from bs4 import BeautifulSoup

header = {'Accept-Encoding' : 'gzip, deflate', 'Accept-Language' : 'zh-CN,zh;q=0.9',
		  'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8', 'Host' : 'www.hn9xiang.com',
		  'Origin' : 'http://www.hn9xiang.com', 'Proxy-Connection' : 'keep-alive',
		  'Referer' : 'http://www.hn9xiang.com/index/login/login.html',
		  'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
		  'X-Requested-With' : 'XMLHttpRequest'}


def getLogin () :
	loginHttp = 'http://www.hn9xiang.com/index/login/ajaxlogin.html'
	phone = '18522179401'
	password = 'qwer1234'

	data = {'phone1' : '18522179401', 'password1' : 'qwer1234'}

	data = parse.urlencode(data).encode('utf-8')
	req = request.Request(loginHttp, data=data, headers=header)
	urlopen = request.urlopen(req)
	read = urlopen.read()
	login = BeautifulSoup(read, 'lxml')

	ul = login.find_all("ul", class_='nav-list float-left clearfix')

	print(login)
	print('----------')
	print(ul)


if __name__ == '__main__' :
	getLogin()
