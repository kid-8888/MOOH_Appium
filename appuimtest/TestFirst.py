#!/usr/bin/python
# -*- coding: UTF-8 -*-
import unittest
from time import sleep
from page.DriverPageFirst import BaseDriver
from page.FristregisterPage import HoomFristregister
from page.LoginPage import LoginHoom
from page.LogoutPage import LogoutHoom
from page.StartPage import StartAction


class CaseTest(unittest.TestCase):
    def setUp(self):
        BD = BaseDriver()
        self.driver = BD.android_driver()
        StartAction(self.driver).swipe_left(n=2)

    # 注册
    def test_register(self):
        HF = HoomFristregister(self.driver)
        HF.HoomRegister()
        HF.always_allow(self.driver)
        LH = LogoutHoom(self.driver)
        LH.logouthoom()
        LH.always_allow1(self.driver)
        sleep(5)

    # # 登录
    # def test_login(self):
    #     LH1 = LoginHoom(self.driver)
    #     LH1.loginhoom()


if __name__ == "__main__":
    unittest.main()
