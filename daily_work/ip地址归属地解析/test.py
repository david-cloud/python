__Author__ = "David"

import urllib
import json

ip =  "103.37.140.78"
url = "http://ip.taobao.com/service/getIpInfo.php?ip="

data = urllib.urlopen(url + ip).read()
datadict=json.loads(data)

for oneinfo in datadict:
    if "code" == oneinfo:
        if datadict[oneinfo] == 0:
            print datadict["data"]["region"]