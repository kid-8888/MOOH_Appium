# !/usr/bin/python
# -*- coding:UTF-8 -*-
from time import sleep

from appium.webdriver.common.touch_action import TouchAction
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from page.ContactsPage import ContactsList
from selenium.webdriver.support import expected_conditions as EC

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
    # 选择成员
    transmit_select = (By.ID, "com.showfires.im:id/contacts_check")
    # 确认转发
    tv_transmit = (By.ID, "com.showfires.im:id/tv_transmit")

    def __init__(self, appium_driver):
        self.driver = appium_driver
        # self.driver = webdriver.Remote()

    # 转发文本
    def transmit_text_ele_action(self):
        el = self.driver.find_elements(*self.transmit_text_ele)
        TouchAction(self.driver).long_press(el[0]).wait(3000).perform()

    # 转发图片
    def transmit_picture_ele_action(self):
        el = self.driver.find_elements(*self.transmit_picture_ele)
        TouchAction(self.driver).long_press(el[0]).wait(3000).perform()

    # 转发语音
    def transmit_voice_ele_action(self):
        el = self.driver.find_elements(*self.transmit_voice_ele)
        TouchAction(self.driver).long_press(el[0]).wait(3000).perform()

    # 转发文件
    def transmit_file_ele_action(self):
        el = self.driver.find_elements(*self.transmit_file_ele)
        TouchAction(self.driver).long_press(el[0]).wait(3000).perform()

    # 转发按钮
    def transmit_ele_action(self):
        self.driver.find_element(*self.transmit_ele)

    # 选择成员
    def transmit_select_action(self):
        self.driver.find_element(*self.transmit_select).click()

    # 里面的【转发】
    def transmit_action(self):
        self.driver.find_element(*self.tv_transmit).click()

    def transmit_message(self):
        CL = ContactsList(self.driver)
        sleep(2)
        CL.talk_action()
        sleep(2)
        self.transmit_text_ele_action()
        sleep(10)
        self.transmit_ele_action()
        sleep(5)
        self.transmit_select_action()
        sleep(2)
        self.transmit_action()

    def get_toast(self, appium_driver):
        sleep(1)
        toast_ele = ("xpath", "//*[@text='转发成功']")
        try:
            e = WebDriverWait(appium_driver, 5, 0.1).until(EC.presence_of_element_located(toast_ele))
            e.click()
        except:
            pass
