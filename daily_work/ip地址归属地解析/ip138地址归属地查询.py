__Author__ = "David"

import urllib2,random
import re
import sys
reload(sys)
sys.setdefaultencoding('utf8')

# try:
while True:
    ipaddr =  raw_input("Enter IP Or Domain Name:")
    if ipaddr == "" or ipaddr == 'exit':
        break
    else:
        url = "http://www.ip138.com/ips138.asp?ip=%s&action=2" % ipaddr
        user_list = [
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4620.400 QQBrowser/9.7.13014.400',
            'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2 ',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36'
        ]
        UserAgent = random.choice(user_list)
        headers = {
            'User-Agent': UserAgent
        }

        request = urllib2.Request(url=url, headers=headers)
        response = urllib2.urlopen(request)
        s = response.read()

        # Get IP Address
        ip = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',s)

        print("\n****** Below Result From IP138 Database *****")
        print("IP Address:",ip[0])
        #Get IP Address Location
        result = re.findall(r'(<li>.*?</li>)',s)
        #print(type(result),result)
        for i in result:
            #print(i)
            print(i[4:-5])
        print("*"*45)
        print("\n")
# except:
#     print("Not Data Find")