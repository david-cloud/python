# -*- coding: utf-8 -*-
# 无检测防护-https://bot.sannysoft.com/
# 浏览器有提示：Chrome is being controlled by automated test software

from selenium import webdriver
options = webdriver.ChromeOptions()

driver = webdriver.Chrome(executable_path=r"C:\py\chromedriver.exe", options=options)
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """
            Object.defineProperty(navigator, 'webdriver', {
              get: () => undefined
            })
            """
        })
driver.get("http://www.baidu.com")