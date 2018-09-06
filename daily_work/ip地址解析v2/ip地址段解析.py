# -*- coding: utf-8 -*-
__Author__ = "David"

import ipaddr
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# 读取 ip 地址段文件
with open('ip_zone.txt','r') as f:
    for ip in f.readlines():
        if ip != None:
            # 去除 读取文件数据每行后面的换行符
            MIP = ip.strip('\n')
            # 生成 一个迭代器对象
            hosts = ipaddr.IPv4Network(MIP).iterhosts()
            for IP in hosts:
                # 将解析的单个ip 写入 ip_list.txt文件
                with open('ip_list.txt','a') as f2:
                    print IP
                    f2.write(str(IP) + '\n')
f.close()
