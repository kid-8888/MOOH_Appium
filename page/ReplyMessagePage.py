#!/usr/bin/python
# -*- coding: UTF-8 -*-
from time import sleep

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from page.ContactsPage import ContactsList
from page.SendmessagePage import SendMessage


class ReplyMessage:
    # 回复文本
    chat_text_ele = (By.ID, "com.showfires.im:id/chat_info_layout_out")
    # 回复图片
    chat_picture_ele = (By.ID, "com.showfires.im:id/chat_picture_img")
    # 回复语音
    chat_voice_ele = (By.ID, "com.showfires.im:id/chat_voice_anim_layout")
    # 回复文件
    chat_file_ele = (By.ID, "com.showfires.im:id/chat_file_layout")
    # 点击菜单栏中回复
    reply_ele = (By.XPATH, "//*[@text='回复']")

    def __init__(self, appium_driver):
        self.driver = appium_driver
        # self.driver = webdriver.Remote()

    # 定位文本内容
    def chat_text_ele_action(self):
        el = self.driver.find_elements(*self.chat_text_ele)
        TouchAction(self.driver).long_press(el[0]).wait(3000).perform()

    # 定位语音
    def chat_voice_ele_action(self):
        el = self.driver.find_elements(*self.chat_voice_ele)
        TouchAction(self.driver).long_press(el[0]).wait(3000).perform()

    # 定位图片
    def chat_picture_ele_action(self):
        el = self.driver.find_elements(*self.chat_picture_ele)
        TouchAction(self.driver).long_press(el[0]).wait(3000).perform()

    # 定位文件
    def chat_file_ele_action(self):
        el = self.driver.find_elements(*self.chat_file_ele)
        TouchAction(self.driver).long_press(el[0]).wait(3000).perform()

    # 点击菜单栏中的【回复】
    def reply_ele_action(self):
        self.driver.find_element(*self.reply_ele).click()

    def reply_message(self):
        CL = ContactsList(self.driver)
        sleep(2)
        CL.talk_action()
        sleep(5)
        self.chat_text_ele_action()
        sleep(2)
        self.reply_ele_action()
        sleep(2)
        SM = SendMessage(self.driver)
        SM.send_text_element_action()
        SM.send_msg_bt_action()
        sleep(2)

        self.chat_picture_ele_action()
        sleep(2)
        self.reply_ele_action()
        sleep(2)
        SM = SendMessage(self.driver)
        SM.send_text_element_action()
        SM.send_msg_bt_action()
        sleep(2)

        self.chat_voice_ele_action()
        sleep(2)
        self.reply_ele_action()
        sleep(2)
        SM = SendMessage(self.driver)
        SM.send_text_element_action()
        SM.send_msg_bt_action()
        sleep(2)
