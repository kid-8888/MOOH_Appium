# !/usr/bin/python
# -*- coding:UTF-8 -*-
from appium import webdriver
from selenium.webdriver.common.by import By


class LoginHoom:
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

    def loginhoom(self, un="a123456", pw="a1234567"):
        self.un_clear_action()
        self.un_enter_action(un)
        self.pw_enter_action(pw)
        self.login_button_action()

