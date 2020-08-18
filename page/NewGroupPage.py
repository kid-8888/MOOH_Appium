# !/usr/bin/python
# -*- coding:UTF-8 -*-
from time import sleep

from appium import webdriver
from selenium.webdriver.common.by import By


class NewGroup:
    talk_list = (By.ID, "com.showfires.im:id/talklist_add")
    group_check = (By.ID, "com.showfires.im:id/contacts_check")
    next_button = (By.ID, "com.showfires.im:id/next")
    creat_button = (By.ID, "com.showfires.im:id/tv_creat")

    def __init__(self, appium_driver):
        self.driver = appium_driver
        # self.driver = webdriver.Remote()

    def talk_list_action(self):
        self.driver.find_element(*self.talk_list).click()

    def group_check_action(self):
        for i in range(1, 3):
            ele = self.driver.find_elements(*self.group_check)
            ele[i].click()

    def next_button_action(self):
        self.driver.find_element(*self.next_button).click()

    def creat_button_action(self):
        self.driver.find_element(*self.creat_button).click()

    def new_group(self):
        self.talk_list_action()
        sleep(2)
        self.group_check_action()
        sleep(2)
        self.next_button_action()
        sleep(2)
        self.creat_button_action()
