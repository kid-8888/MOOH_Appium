# !/usr/bin/python
# -*- coding:UTF-8 -*-
from appium.webdriver.common.touch_action import TouchAction
from selenium import webdriver
from selenium.webdriver.common.by import By


class TransmitMessage:
    # 回复文本
    transmit_text_ele = (By.ID, "com.showfires.im:id/chat_info_layout_out")
    # 回复图片
    transmit_picture_ele = (By.ID, "com.showfires.im:id/chat_picture_img")
    # 回复语音
    transmit_voice_ele = (By.ID, "com.showfires.im:id/chat_voice_anim_layout")
    # 回复文件
    transmit_file_ele = (By.ID, "com.showfires.im:id/chat_file_layout")
    # 点击菜单栏中转发
    transmit_ele = (By.XPATH, "//*[@text='转发']")

    def __init__(self, appium_driver):
        # self.driver = appium_driver
        self.driver = webdriver.Remote()

    # 转发文本
    def transmit_text_ele_action(self):
        el = self.driver.find_elements(*self.transmit_text_ele)
        TouchAction(self.driver).long_press(el[0]).wait(3000).perform()

    # 转发图片
    def transmit_picture_ele_action(self):
        el = self.driver.find_elements(*self.transmit_text_ele)
        TouchAction(self.driver).long_press(el[0]).wait(3000).perform()

    # 转发语音
    def transmit_voice_ele_action(self):
        el = self.driver.find_elements(*self.transmit_text_ele)
        TouchAction(self.driver).long_press(el[0]).wait(3000).perform()

    # 转发文件
    def transmit_file_ele_action(self):
        el = self.driver.find_elements(*self.transmit_text_ele)
        TouchAction(self.driver).long_press(el[0]).wait(3000).perform()

    # 转发按钮
    def transmit_ele_action(self):
        self.driver.find_element(*self.transmit_ele).click()
