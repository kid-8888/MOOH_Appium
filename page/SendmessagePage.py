# !/usr/bin/python
# -*- coding:UTF-8 -*-
from random import randint
from time import sleep
from appium import webdriver
from selenium.webdriver.common.by import By

from page.ContactsPage import ContactsList


class SendMessage:
    send_text_element = (By.ID, "com.showfires.im:id/send_input_ed")
    send_picture_element = (By.ID, "com.showfires.im:id/chat_picture_img")
    send_voice_element = (By.ID, "")
    send_file_element = (By.ID, "")
    send_msg_bt = (By.ID, "com.showfires.im:id/send_msg_bt")

    def __init__(self, appium_driver):
        self.driver = appium_driver
        # self.driver = webdriver.Remote()

    def send_element_action(self):
        value = str(randint(1, 99))
        self.driver.find_element(*self.send_text_element).send_keys(value)

    def send_msg_bt_action(self):
        self.driver.find_element(*self.send_msg_bt).click()

    def send_message(self):
        CL = ContactsList(self.driver)
        sleep(2)
        CL.talk_action()
        sleep(2)
        self.send_element_action()
        sleep(2)
        self.send_msg_bt_action()
