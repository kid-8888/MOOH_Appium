#!/usr/bin/python
# -*- coding: UTF-8 -*-
from time import sleep

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from page.ContactsPage import ContactsList
from page.SendmessagePage import SendMessage


class ReplyMessage:

    chat_ele = (By.ID, "com.showfires.im:id/chat_info_layout_out")
    reply_ele = (By.XPATH, "//*[@text='回复']")

    def __init__(self, appium_driver):
        self.driver = appium_driver
        # self.driver = webdriver.Remote()

    # 定位文本内容
    def chat_ele_action(self):
        el = self.driver.find_elements(*self.chat_ele)
        TouchAction(self.driver).long_press(el[0]).wait(3000).perform()

    # 点击菜单栏中的【回复】
    def reply_ele_action(self):
        self.driver.find_element(*self.reply_ele).click()

    def reply_message(self):
        sleep(2)
        CL = ContactsList(self.driver)
        sleep(2)
        CL.talk_action()
        sleep(2)
        SM = SendMessage(self.driver)
        sleep(2)
        SM.send_element_action()
        SM.send_msg_bt_action()
        sleep(2)
        self.chat_ele_action()
        sleep(2)
        self.reply_ele_action()
        sleep(2)
        SM.send_element_action()
        SM.send_msg_bt_action()

