# !/usr/bin/python
# -*- coding:UTF-8 -*-
from random import randint
from time import sleep
from appium import webdriver
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction
from page.ContactsPage import ContactsList


class SendMessage:
    # 发送文本
    send_text_element = (By.ID, "com.showfires.im:id/send_input_ed")
    # 发送按钮
    send_msg_bt = (By.ID, "com.showfires.im:id/send_msg_bt")

    # 发送图片
    send_picture_element = (By.ID, "com.showfires.im:id/chat_picture_img")
    # 更多按钮
    more_ele = (By.ID, "com.showfires.im:id/send_more_img")
    # 图片按钮
    picture_button = (By.XPATH, "//*[@text='照片']")
    # 图片选择
    picture_check = (By.ID, "com.showfires.im:id/check")
    # 图片选择完成
    picture_tv_ok = (By.ID, "com.showfires.im:id/picture_tv_ok")

    # 发送语音
    permission_button = (By.ID, "com.android.packageinstaller:id/permission_allow_button")
    send_voice_element = (By.ID, "com.showfires.im:id/send_voice_img")
    send_voice_button_ele = (By.ID, "com.showfires.im:id/send_voice_bt")

    # 文件按钮
    more_ele1 = (By.ID, "com.showfires.im:id/send_more_img")
    file_button = (By.ID,  "com.showfires.im:id/select_file")

    def __init__(self, appium_driver):
        self.driver = appium_driver
        # self.driver = webdriver.Remote()

    # 发送文本
    def send_text_element_action(self):
        value = str(randint(1, 99)) + u"测试"
        self.driver.find_element(*self.send_text_element).send_keys(value)

    def send_msg_bt_action(self):
        self.driver.find_element(*self.send_msg_bt).click()

    # 发送图片
    def send_picture_element_action(self):
        self.driver.find_element(*self.more_ele).click()
        sleep(2)
        self.driver.find_element(*self.picture_button).click()
        sleep(2)
        self.driver.find_element(*self.picture_check).click()
        sleep(2)
        self.driver.find_element(*self.picture_tv_ok).click()

    # 发送语音
    def send_voice_element_action(self):
        self.driver.find_element(*self.send_voice_element).click()
        ele = self.driver.find_element(*self.send_voice_button_ele)
        TouchAction(self.driver).long_press(ele).wait(8000).release().perform()

    # 发送文件
    def send_file_element_action(self):
        self.driver.find_element(*self.more_ele1).click()
        self.driver.find_element(*self.file_button).click()

    def send_message(self):
        CL = ContactsList(self.driver)
        sleep(2)
        CL.talk_action()
        sleep(2)
        self.send_text_element_action()
        sleep(2)
        self.send_msg_bt_action()
        sleep(2)
        self.send_picture_element_action()
        sleep(3)
        self.send_voice_element_action()
