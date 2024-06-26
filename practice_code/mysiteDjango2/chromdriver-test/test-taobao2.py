# -*- coding: utf-8 -*-
# 已测试成功 - https://bot.sannysoft.com/

# 有检测防护
from undetected_chromedriver import Chrome
from selenium.webdriver.common.by import By
import time
import datetime

# 当前时间
#now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
# 秒杀时间
#ms_time = "2023-08-03 19:00:00.000000"
# 创建驱动对象
driver = Chrome(executable_path=r"C:\py\chromedriver.exe")
# driver.maximize_window()


def login():
    # 打开淘宝登录页，并进行扫码登录
    driver.get("https://www.taobao.com")
    time.sleep(5)
    if driver.find_element_by_link_text("亲，请登录"):
        driver.find_element_by_link_text("亲，请登录").click()

    print("请在30秒内完成扫码")
    time.sleep(30)

    # 进入购物车
    driver.get("https://cart.taobao.com/cart.htm")
    time.sleep(10)
    # 点击购物车里全选按钮
    while True:
        try:
            if driver.find_element_by_id("J_SelectAll1"):
                driver.find_element_by_id("J_SelectAll1").click()
                break
        except:
            print("找不到购买按钮，没有选中购物车，或购物车为空")
    now = datetime.datetime.now()
    print('已登录成功并选中购物车商品: {}'.format(now.strftime('%Y-%m-%d %H:%M:%S')))


def buy(buytime):
    while True:
        # 获取电脑现在的时间
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
#        print("当前时间：{}".format(now))
        # 对比时间，时间到的话就点击结算
        if now > buytime:
            # 结算
            while True:
                try:
                    if driver.find_element_by_link_text("结 算"):
                        driver.find_element_by_link_text("结 算").click()
                        print("结算成功....:", datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
                        break
                except:
                    time.sleep(0.01)
                    print("未找到结算按钮++++++++++++++++++++++++++++++++")
                    break

            # 提交订单
            while True:
                try:
                    if driver.find_element_by_link_text("提交订单"):
                        driver.find_element_by_link_text("提交订单").click()
                        print("抢购成功，请尽快付款....:{}".format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')))
                        break
                except:
                    time.sleep(0.01)
                    print("结算提交成功，请尽快付款....")
                    break



if __name__ == "__main__":
    # times = input("请输入抢购时间：")
    # 时间格式："2018-09-06 11:20:00.000000"
    login()
    buy("2023-08-18 14:36:00.000000")
