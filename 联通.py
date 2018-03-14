#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'PJ'
__mtime__ = '2018/3/14'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""

from urllib import request, parse
from bs4 import BeautifulSoup
import re

http = 'http://www.10010.com/net5/051/'

def Login():
	req = request.Request(http)
	url = request.urlopen(req)
	bsObj = BeautifulSoup(url.read(), 'lxml')

	for a in bsObj.findAll('div', class_=re.compile('user_phone line_block cur_pointer fl')):
		print(a)

if __name__ == '__main__':
    Login()