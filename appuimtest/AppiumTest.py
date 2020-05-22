# !/usr/bin/python
# -*- coding:UTF-8 -*-
import unittest
from page.ContactsPage import ContactsList
from page.DriverPage import BaseDriver
from page.LoginPage import LoginHoom
from page.SendmessagePage import SendMessage
from page.ToastPage import FindToast


class CaseTest(unittest.TestCase):
    def setUp(self):
        BD = BaseDriver()
        self.driver = BD.android_driver()
        # StartAction(self.driver).swipe_left(n=2)

    # 用户名或密码错误
    def test_logerror(self):
        FT = FindToast(self.driver)
        FT.errorlogin()
        FT.get_toast(self.driver)

    # 登录
    def test_login(self):
        LH1 = LoginHoom(self.driver)
        LH1.loginhoom()

    # 从通讯录点击好友
    def test_talk(self):
        CL = ContactsList(self.driver)
        CL.talk_action()

    # 发送消息
    def test_send_message(self):
        CL = ContactsList(self.driver)
        CL.talk_action()
        SM = SendMessage(self.driver)
        SM.send_message()



if __name__ == "__main__":
    unittest.main()
