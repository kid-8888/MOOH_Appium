#!/usr/bin/python
# -*- coding: UTF-8 -*-
from random import randint
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Register:
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

    # 注册按钮
    def register_button_action(self):
        self.driver.find_element(*self.register_button).click()

    # 用户名输入框
    def username_enter_action(self, un):
        # value = "a" + str(randint(100000000, 999999999))
        self.driver.find_element(*self.username_enter).send_keys(un)

    # 用户名界面下一步按钮
    def username_next_button_action(self):
        self.driver.find_element(*self.username_next_button).click()

    # 密码输入框
    def password_enter_action(self, pw):
        self.driver.find_element(*self.password_enter).send_keys(pw)

    # 确认密码
    def password_confirm_enter_action(self, pw1):
        self.driver.find_element(*self.password_confirm_enter).send_keys(pw1)

    # 密码输入界面【下一步】
    def password_next_button_action(self):
        self.driver.find_element(*self.password_next_button).click()

    # 昵称设置界面【跳过】
    def skip_button_action(self):
        self.driver.find_element(*self.skip_button).click()

    def register_login(self,un="a12345", pw="a1234567", pw1="a1234567"):
        self.register_button_action()
        sleep(2)
        self.username_enter_action(un)
        self.username_next_button_action()
        sleep(2)
        self.password_enter_action(pw)
        self.password_confirm_enter_action(pw1)
        self.password_next_button_action()
        sleep(2)
        self.skip_button_action()

    def get_toast(self, appium_driver):
        sleep(1)
        toast_ele = ("xpath", "//*[@text='用户名支持英文，数字，下划线，且在6-12个字符之间']")
        try:
            e = WebDriverWait(appium_driver, 5, 0.1).until(EC.presence_of_element_located(toast_ele))
            e.click()
        except:
            pass

    # 用户名少于6位
    def register_login1(self, un="a1234"):
        sleep(2)
        self.register_button_action()
        sleep(2)
        try:
            self.username_enter_action(un)
        except NameError as e:
            return
        self.username_next_button_action()
        sleep(2)

    # 用户名大于15位
    def register_login2(self, un="a1234512345678"):
        sleep(2)
        self.register_button_action()
        sleep(2)
        try:
            self.username_enter_action(un)
        except NameError as e:
            return
        self.username_next_button_action()
        sleep(2)
