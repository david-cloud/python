# -*- encoding: utf-8 -*-
__Author__ = "David"
import json
import urllib2,random
import sys,re,os
import signal

reload(sys)
sys.setdefaultencoding('utf-8')
# 调用 函数生成 ip列表, 并将ip 传入 ip_local函数，进行数据获取
def ip_list():
    #读取 ip地址文件 写入 ip_address 列表
    ip_address = []
    with open('zsip.txt','r') as f:
        for ip in f.readlines():
            if ip != None:
                ip_address.append(ip)
    f.close()
    print(ip_address,len(ip_address))
    # 获取 ip 所在地 并写入到 ip_output.txt文件中
    for i in ip_address:
        # 在 ip_local函数中定义要输出的地址信息 详细程度，在此处定义变量进行接收
        country_address,city_address = ip_local(i.strip())
        #print(i.strip(),type(i))
        #country_address = ip_local(i.strip())
        with open('zsip_output.txt','a') as f2:
            f2.write(i.strip() + " " + country_address + "" + city_address + '\n')
            #f2.write(i.strip() + " " + country_address + "" + '\n')


# 模拟用户行为
#def ip_local(ip):
def ip_local():
    #url = "http://ip.taobao.com/service/getIpInfo.php?ip=%s" % ip
    url = "http://www.ip181.com/"
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

    # 读取 代理 ip地址文件 写入 ip_proxy 列表
    ip_proxy = []
    with open('proxy.txt', 'r') as f2:
        for ip in f2.readlines():
            if ip != None:
                ip_proxy.append(ip.strip())
    f2.close()

    # 使用一组ip调用random函数来随机使用其中一个ip 参数是一个字典{'类型':'代理ip:端口号'}
    print(random.choice(ip_proxy),type(random.choice(ip_proxy)))
    proxy_support = urllib2.ProxyHandler({'http':random.choice(ip_proxy)})
    # 定制opener
    opener = urllib2.build_opener(proxy_support)
    opener.add_handler = [('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36')]
    urllib2.install_opener(opener)
    response = urllib2.urlopen(url)
    print response.read()

ip_local()

    #request = urllib2.Request(url=url, headers=headers)
    # response = urllib2.urlopen(url)
    # data = response.read()
    # datadict = json.loads(data)
    # for oneinfo in datadict:
    #     if "code" == oneinfo:
    #         if datadict[oneinfo] == 0:
    #             return datadict["data"]["country"],datadict["data"]["region"]
                #return datadict["data"]["country"]


# 调用 函数生成 ip列表, 并将ip 传入 ip_local函数，进行数据获取
#ip_list()
# print(ip_local("8.8.8.8"))
# country_address = ip_local("8.8.8.8")
# with open('zsip_output.txt', 'a') as f2:
#     f2.write(country_address + "" + '\n')