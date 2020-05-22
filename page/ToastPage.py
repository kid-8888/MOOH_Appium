# !/usr/bin/python
# -*- coding:UTF-8 -*-
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FindToast:
    un_clear = (By.ID, "com.showfires.im:id/login_user_ed")
    un_enter = (By.ID, "com.showfires.im:id/login_user_ed")
    pw_enter = (By.ID, "com.showfires.im:id/login_pwd_ed")
    login_button = (By.ID, "com.showfires.im:id/login_bt")

    def __init__(self, appium_driver):
        self.driver = appium_driver
        # self.driver = webdriver.Remote()

    def un_clear_action(self):
        self.driver.find_element(*self.un_clear).clear()

    def un_enter_action(self, un):
        self.driver.find_element(*self.un_enter).send_keys(un)

    def pw_enter_action(self, pw):
        self.driver.find_element(*self.pw_enter).send_keys(pw)

    def login_button_action(self):
        self.driver.find_element(*self.login_button).click()

    def errorlogin(self, un="a123456", pw="a123456"):
        self.un_clear_action()
        self.un_enter_action(un)
        self.pw_enter_action(pw)
        self.login_button_action()

    def get_toast(self, appium_driver):
        sleep(1)
        toast_ele = ("xpath", "//*[@text='用户名或密码错误']")
        try:
            e = WebDriverWait(appium_driver, 5, 0.1).until(EC.presence_of_element_located(toast_ele))
            e.click()
        except:
            pass