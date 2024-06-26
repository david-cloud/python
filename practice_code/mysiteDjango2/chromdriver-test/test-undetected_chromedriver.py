# -*- coding: utf-8 -*-
# 已测试成功 - https://bot.sannysoft.com/


#有检测防护
from undetected_chromedriver import Chrome
import time

# 在创建驱动对象时，我们还可以设置相关配置，例如设置User-Agent，
# options = {
#     "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
# }
# 创建驱动对象
driver = Chrome(executable_path=r"C:\py\chromedriver.exe")

# 打开百度
driver.get("https://www.baidu.com/")

# 定位搜索框并输入关键字
search_input = driver.find_element_by_css_selector("#kw")
search_input.send_keys("undetected_chromedriver")

# 点击搜索按钮
search_button = driver.find_element_by_css_selector("#su")
search_button.click()

# 等待页面加载完成
time.sleep(5)

# 获取搜索结果标题并打印
results = driver.find_elements_by_css_selector(".result .t")
for result in results:
    print(result.text)

# 关闭浏览器
#driver.quit()