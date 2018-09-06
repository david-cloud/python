# -*- coding:utf8 -*-
__Author__ = "David"

import urllib2,random

base_url = 'http://www.xicidaili.com/'
# 构造一个请求  给关键字参数
# 构造 headers   ----》 要求字典类型
# 爬虫和反爬虫 第一步  user-agent
user_list = [
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4620.400 QQBrowser/9.7.13014.400',
    'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2 ',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36'
]
UserAgent = random.choice(user_list)   #随机一个 user-agent ， 避免被封禁
print UserAgent

headers = {
    # 默认user-agent  python-spider
    'User-Agent':UserAgent
}

'''
也可以用次方法 来设置user-agent信息
request.add_header('User-Agent',UserAgent)   #设置一个 请求报头
print request.get_header('User-agent')

makecert.exe -r -ss my -n "CN=DO_NOT_TRUST_FiddlerRoot, O=DO_NOT_TRUST, OU=Created by http://www.fiddler2.com" -sky signature -eku 1.3.6.1.5.5.7.3.1 -h 1 -cy authority -a sha1 -m 120 -b 04/15/2018

'''

request = urllib2.Request(url=base_url,headers=headers)
response = urllib2.urlopen(request)
print response.read()