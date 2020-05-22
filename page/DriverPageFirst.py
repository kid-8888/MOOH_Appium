# !/usr/bin/python
# -*- coding:UTF-8 -*-
from time import sleep
from appium import webdriver


class BaseDriver:

    def android_driver(self):

        desired_caps = {
            "platformName": "Android",
            "deviceName": "43448bf9",
            "appPackage": "com.showfires.im",
            "appActivity": "com.showfires.uesr.activity.SplashActivity",
        }
        # 驱动
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        sleep(5)
        return driver

