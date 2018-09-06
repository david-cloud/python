# -*- coding:utf-8 -*-
__Author__ = "David"

import urllib2,random
import re
import sys
import chardet

#读取 ip地址文件 写入 ip_address 列表
ip_address = []
with open('zsip.txt', 'r') as f1:
    for ip in f1.readlines():
        if ip != None:
            # 从文件中读取行数据时，会带换行符，使用strip函数去掉 换行符后存入列表
            ip_address.append(ip.strip("\n"))
f1.close()
#ip_address2 = ["103.83.60.130","103.83.60.130"]
#print(ip_address)

for ipaddr in ip_address:
    url = "http://www.ip138.com/ips138.asp?ip=%s&action=2" % ipaddr
    #print(url)
    user_list = [
        'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4620.400 QQBrowser/9.7.13014.400',
        'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2 ',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36',
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.2)',
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
        'Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1',
        'Opera/9.27 (Windows NT 5.2; U; zh-cn)',
        'Mozilla/5.0 (iPhone; U; CPU like Mac OS X) AppleWebKit/420.1 (KHTML, like Gecko) Version/3.0 Mobile/4A93 Safari/419.3',
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.12) Gecko/20080219 Firefox/2.0.0.12 Navigator/9.0.0.6',
        'Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13'
    ]
    UserAgent = random.choice(user_list)
    headers = {
        'User-Agent': UserAgent
    }

    request = urllib2.Request(url=url, headers=headers)
    response = urllib2.urlopen(request)
    s = response.read()

    # 使用chardet检测字符串的编码格式
    #print(chardet.detect(s))
    s = s.decode('gb2312')
    s = s.encode('utf-8')

    # Get IP Address
    ip = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', s)

    # Get IP Address Location
    result = re.findall(r'(<li>.*?</li>)',s)
    for i in result:
        ip_addr = i[4:-5]
        #print(ip_addr.split()[0].split('：')[1])
        with open('zsip_output.txt','a') as f:
            f.write(ip[0] + " " + ip_addr.split()[0].split('：')[1] + "\n")
        # 此处break 意在 只提取result 结果的第一行内容
        break