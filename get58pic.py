#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'PJ'
__mtime__ = '2017/8/11'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""

import urllib3
import requests
from userAgentManage import getUserAgent

url = 'http://www.58pic.com/'

def Http_Manage():
	http = urllib3.PoolManager()
	req = http.request('GET', url)
	print(req.data.decode('GBK'))

if __name__ == '__main__':
    Http_Manage()
