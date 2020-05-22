# !/usr/bin/python
# -*- coding:UTF-8 -*-
from random import randint
from time import sleep
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HoomFristregister:
    # 属性:元素定位
    button_next = (By.ID, "com.showfires.im:id/iv_next")
    register_button = (By.ID, "com.showfires.im:id/login_register_tv")
    username_enter = (By.ID, "com.showfires.im:id/register_user_name_ed")
    username_next_button = (By.ID, "com.showfires.im:id/register_next")
    password_enter = (By.ID, "com.showfires.im:id/register_pwd_ed")
    password_confirm_enter = (By.ID, "com.showfires.im:id/register_confirm_pwd_ed")
    password_next_button = (By.ID, "com.showfires.im:id/register_next_bt")
    skip_button = (By.ID, "com.showfires.im:id/edit_nick_skip")

    def __init__(self, appium_driver):
        self.driver = appium_driver
        # self.driver = webdriver.Remote()

    # 方法
    def button_next_action(self):
        self.driver.find_element(*self.button_next).click()

    def register_button_action(self):
        self.driver.find_element(*self.register_button).click()

    def username_enter_action(self):
        value = "a" + str(randint(100000000, 999999999))
        self.driver.find_element(*self.username_enter).send_keys(value)

    def username_next_button_action(self):
        self.driver.find_element(*self.username_next_button).click()

    def password_enter_action(self, pw):
        self.driver.find_element(*self.password_enter).send_keys(pw)

    def password_confirm_enter_action(self, pw1):
        self.driver.find_element(*self.password_confirm_enter).send_keys(pw1)

    def password_next_button_action(self):
        self.driver.find_element(*self.password_next_button).click()

    def skip_button_action(self):
        self.driver.find_element(*self.skip_button).click()

    def always_allow(self, appium_driver, number=5):
        for i in range(number):
            loc = ("xpath", "//*[@text='否']")
            try:
                e = WebDriverWait(appium_driver, 1, 0.5).until(EC.presence_of_element_located(loc))
                e.click()
            except:
                pass

    def HoomRegister(self, pw="a1234567", pw1="a1234567"):
        self.button_next_action()
        sleep(2)
        self.register_button_action()
        sleep(2)
        self.username_enter_action()
        self.username_next_button_action()
        sleep(2)
        self.password_enter_action(pw)
        self.password_confirm_enter_action(pw1)
        self.password_next_button_action()
        sleep(2)
        self.skip_button_action()
