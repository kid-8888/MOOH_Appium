# !/usr/bin/python
# -*- coding:UTF-8 -*-
from time import sleep
from appium import webdriver


class BaseDriver:
    def android_driver(self):
        desired_caps = {
            "platformName": "Android",
            "automationName": "Uiautomator2",
            "deviceName": "43448bf9",
            "appPackage": "com.showfires.im",
            "appActivity": "com.showfires.uesr.activity.SplashActivity",
            "noReset": "true",
            # "unicodeKeyboard": "true",
            # "resetKeyboard": "true"
        }
        # 驱动
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        sleep(5)
        return driver
