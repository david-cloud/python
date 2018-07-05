# -*- encoding: utf-8 -*-
__Author__ = "David"

# https://www.jb51.net/article/63012.htm
import json
import urllib
import socket
import sys,re,os
import signal

# 使用淘宝 ip库 接口
url = "http://ip.taobao.com/service/getIpInfo.php?ip="

def ip_list():
    reload(sys)
    sys.setdefaultencoding('utf-8')
    #读取 ip地址文件 写入 ip_address 列表
    ip_address = []
    with open('ip.txt','r') as f:
        for ip in f.readlines():
            if ip != None:
                ip_address.append(ip)
    f.close()
    # 获取 ip 所在地 并写入到 ip_output.txt文件中
    for i in ip_address:
        country_address,city_address = ip_local(i)
        with open('ip_output.txt','a') as f2:
            f2.write(i.strip() + " " + country_address + "" + city_address + '\n')
#			f2.write(city_address + '\n')
#        print i.strip() + ":" + city_address

# 获取 ip 所在地 接口 函数
def ip_local(ip):
    data = urllib.urlopen(url + ip).read()
    datadict=json.loads(data)

    for oneinfo in datadict:
        if "code" == oneinfo:
            if datadict[oneinfo] == 0:
                return datadict["data"]["country"],datadict["data"]["region"]
ip_list()