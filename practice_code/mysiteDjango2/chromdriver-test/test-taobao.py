# -*- coding: utf-8 -*-
# 已测试成功 - https://bot.sannysoft.com/

# 有检测防护
from undetected_chromedriver import Chrome
from selenium.webdriver.common.by import By
import time
import datetime

# 创建驱动对象
driver = Chrome(executable_path=r"C:\py\chromedriver.exe")
# driver.maximize_window()


def login():
    # 打开淘宝登录页，并进行扫码登录
    driver.get("https://www.taobao.com")
    time.sleep(5)
    if driver.find_element(By.PARTIAL_LINK_TEXT, "亲，请登录"):
        driver.find_element(By.PARTIAL_LINK_TEXT, "亲，请登录").click()

    print("请在20秒内完成扫码")
    time.sleep(20)

    driver.get("https://cart.taobao.com/cart.htm")
    time.sleep(10)
    # 点击购物车里全选按钮
    if driver.find_element("J_CheckBox_939775250537"):
        driver.find_element("J_CheckBox_939775250537").click()
    if driver.find_element("J_CheckBox_939558169627"):
        driver.find_element("J_CheckBox_939558169627").click()
    if driver.find_element("J_SelectAll1"):
        driver.find_element("J_SelectAll1").click()
    now = datetime.datetime.now()
    print('login success:', now.strftime('%Y-%m-%d %H:%M:%S'))


def buy(buytime):
    while True:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        # 对比时间，时间到的话就点击结算
        if now > buytime:
            try:
                # 点击结算按钮
                if driver.find_element("J_Go"):
                    driver.find_element("J_Go").click()
                driver.find_element(By.PARTIAL_LINK_TEXT, '提交订单').click()
            except:
                time.sleep(0.1)
                print(now)
                time.sleep(0.1)


if __name__ == "__main__":
    # times = input("请输入抢购时间：")
    # 时间格式："2018-09-06 11:20:00.000000"
    login()
    buy("2022-12-07 15:08:00.000000")