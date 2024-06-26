# -*- coding: utf-8 -*-
# 引入JS测试-https://bot.sannysoft.com/
# 浏览器有提示：Chrome is being controlled by automated test software

import time
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

#chrome_options = Options()
#chrome_options.add_argument("--headless")
#chrome_options.add_argument('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36')
# 报错(unknown error: DevToolsActivePort file doesn't exist)
#chrome_options.add_argument("--remote-debugging-port=9222")  # this

#driver = Chrome(executable_path=r"C:\py\chromedriver.exe", options=chrome_options)
driver = Chrome(executable_path=r"C:\py\chromedriver.exe")

with open('C:\py\stealth.min.js') as f:
    js = f.read()

driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
  "source": js
})

driver.get("https://www.baidu.com/")