#!/usr/bin/python
# -*- coding: UTF-8 -*-
from time import sleep
from appium import webdriver

desired_caps = {
    "platformName": "Android",
    "automationName": "Uiautomator2",
    "deviceName": "43448bf9",
    "appPackage": "com.chuanxin.im",
    "appActivity": "com.showfires.uesr.activity.SplashActivity",
    "noReset": "true",
    "unicodeKeyboard": "true",
    "resetKeyboard": "true"
}
# 驱动
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
sleep(5)
"""
用户已添加社区，在传信直接登录，使web端产生窗口
"""
for un in range(10000014590, 10000014601):
    driver.find_element_by_id("com.chuanxin.im:id/login_phonr_ed").send_keys(un)
    sleep(1)
    driver.find_element_by_id("com.chuanxin.im:id/login_pwd_ed").send_keys("1")
    sleep(1)
    driver.find_element_by_id("com.chuanxin.im:id/login_bt").click()
    sleep(2)
    driver.find_element_by_id("com.chuanxin.im:id/registerpwd_pwd_ed").send_keys("a1234567")
    sleep(1)
    driver.find_element_by_id("com.chuanxin.im:id/registerpwd_affirm_bt").click()
    sleep(3)
    driver.find_element_by_id("com.chuanxin.im:id/iv_mine").click()
    sleep(3)
    driver.find_element_by_id("com.chuanxin.im:id/mine_more_rl").click()
    sleep(3)
    driver.find_element_by_id("com.chuanxin.im:id/mine_more_log_out_tv").click()
    sleep(3)
    driver.find_element_by_xpath("//*[@resource-id='com.chuanxin.im:id/affirm_tv']").click()
    sleep(3)