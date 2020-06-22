# !/usr/bin/python
# -*- coding:UTF-8 -*-
from time import sleep
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LogoutHoom:
    skip_mime = (By.ID, "com.showfires.im:id/iv_mine")
    setting = (By.ID, "com.showfires.im:id/mine_setting_layout")
    setting_logout = (By.ID, "com.showfires.im:id/setting_logout")

    def __init__(self, appium_driver):
        self.driver = appium_driver
        # self.driver = webdriver.Remote()

    def skip_mime_action(self):
        self.driver.find_element(*self.skip_mime).click()

    def setting_action(self):
        self.driver.find_element(*self.setting).click()

    def setting_logout_action(self):
        self.driver.find_element(*self.setting_logout).click()

    def always_allow1(self, appium_driver, number=5):
        for i in range(number):
            loc = ("xpath", "//*[@text='确定']")
            try:
                e = WebDriverWait(appium_driver, 1, 0.5).until(EC.presence_of_element_located(loc))
                e.click()
            except:
                pass


    def logouthoom(self):
        self.skip_mime_action()
        sleep(2)
        self.setting_action()
        sleep(2)
        self.setting_logout_action()
        sleep(2)
        self.always_allow1(self.driver)





