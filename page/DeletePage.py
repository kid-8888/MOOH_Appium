# !/usr/bin/python
# -*- coding:UTF-8 -*e
from time import sleep

from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction

from page.ContactsPage import ContactsList


class DeleteMessage:
    # 删除文本
    delete_text_ele = (By.ID, "com.showfires.im:id/chat_info_layout_out")
    # 删除图片
    delete_picture_ele = (By.ID, "com.showfires.im:id/chat_picture_img")
    # 删除语音
    delete_voice_ele = (By.ID, "com.showfires.im:id/chat_voice_anim_layout")
    # 删除文件
    delete_file_ele = (By.ID, "com.showfires.im:id/chat_file_layout")
    # 删除按钮
    delete_ele = (By.XPATH, "//*[@text='删除'']")
    # 删除消息
    delete_button_ele = (By.ID, "com.showfires.im:id/chat_transmit_delete_tv")
    # 二次确认弹窗
    all_delete_ele = (By.XPATH, "//*[@text='为所有人删除']")

    def __init__(self, appium_driver):
        self.driver = appium_driver
        # self.driver = webdriver.Remote()

    # 文本长按后删除
    def delete_text_ele_action(self):
        el = self.driver.find_elements(*self.delete_text_ele)
        TouchAction(self.driver).long_press(el[0]).wait(3000).perform()

    # 图片长按后删除
    def delete_picture_ele_action(self):
        el = self.driver.find_elements(*self.delete_text_ele)
        TouchAction(self.driver).long_press(el[0]).wait(3000).perform()

    # 语音长按后删除
    def delete_voice_ele_action(self):
        el = self.driver.find_elements(*self.delete_text_ele)
        TouchAction(self.driver).long_press(el[0]).wait(3000).perform()

    # 文件长按后删除
    def delete_file_ele_action(self):
        el = self.driver.find_elements(*self.delete_text_ele)
        TouchAction(self.driver).long_press(el[0]).wait(3000).perform()

    def delete_action(self):
        self.driver.find_element(*self.delete_ele)

    # 点击删除
    def delete_button_action(self):
        self.driver.find_element(*self.delete_button_ele).click()

    # 为所有人删除
    def all_delete_action(self):
        self.driver.find_element(*self.all_delete_ele).click()

    def delete_message(self):
        CL = ContactsList(self.driver)
        sleep(2)
        CL.talk_action()
        sleep(2)
        self.delete_text_ele_action()
        sleep(1)
        self.delete_action()
        sleep(1)
        self.delete_button_action()
        sleep(1)
        self.all_delete_action()