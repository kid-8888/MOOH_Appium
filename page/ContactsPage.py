# !/usr/bin/python
# -*- coding:UTF-8 -*-
from time import sleep
from appium import webdriver
from selenium.webdriver.common.by import By

from page.StartPage import StartAction


class ContactsList:
    contacts_button = (By.ID, "com.showfires.im:id/iv_contacts")
    friend_list = (By.XPATH, "//*[@text='aa1234']")
    talk_button = (By.XPATH, "//*[@text='对话']")

    def __init__(self, appium_driver):
        self.driver = appium_driver
        # self.driver = webdriver.Remote()

    # 点击【通讯录】
    def contacts_button_action(self):
        self.driver.find_element(*self.contacts_button).click()

    # 点击好友列表
    def friend_list_action(self):
        self.driver.find_element(*self.friend_list).click()

    # 点击【对话】
    def talk_button_action(self):
        self.driver.find_element(*self.talk_button).click()

    def talk_action(self):
        sleep(2)
        self.contacts_button_action()
        sleep(2)
        self.friend_list_action()
        sleep(2)
        self.talk_button_action()
