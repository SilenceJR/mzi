#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'PJ'
__mtime__ = '2018/3/19'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""
import http.cookiejar
from urllib import request, parse
from bs4 import BeautifulSoup

headers1 = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
headers0 = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
headers2 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}
headers3 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}

http1 = 'http://www.chsi.com.cn/'
http2 = 'https://account.chsi.com.cn/passport/login?service=https%3A%2F%2Fmy.chsi.com.cn%2Farchive%2Fj_spring_cas_security_check'

def getBsObj(url) :
	req = request.Request(url, headers=headers0 or headers1 or headers2 or headers3)
	return BeautifulSoup(request.urlopen(req).read(), 'lxml')

def login(account, password) :
	bsObj = getBsObj(http2)
	data = {'username':account, 'password':password}
	for div in bsObj.findAll('form', {'id':'fm1'}):
		for put in div.findAll('input', {'type':'hidden'}):
			# print(put)
			name = put.attrs['name']
			value = put.attrs['value']
			data[name] = value
		for put in div.findAll('input', {'type':'submit'}):
			# print(put)
			name = put.attrs['name']
			value = put.attrs['value']
			data[name] = value
	# print(data)

	data = parse.urlencode(data).encode('utf-8')
	req = request.Request(http2, data=data, headers=headers1 or headers2 or headers3)
	print(data)
	urlopen = request.urlopen(req)
	print(urlopen.info())
	bsObj = BeautifulSoup(urlopen.read(), 'lxml')
	return bsObj


def getOpener(head) :
	cj = http.cookiejar.CookieJar()
	pro = request.HTTPCookieProcessor(cj)
	opener = request.build_opener(pro)
	header = []
	for key, value in head.items() :
		elem = (key, value)
		header.append(elem)
	opener.addheaders = header
	return opener


if __name__ == '__main__':
	account = input('输入账号')
	password = input('输入密码')
	bsObj = login(account, password)
	print(bsObj)