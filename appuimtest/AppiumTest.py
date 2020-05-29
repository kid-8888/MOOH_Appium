# !/usr/bin/python
# -*- coding:UTF-8 -*-
import unittest
from page.ContactsPage import ContactsList
from page.DriverPage import BaseDriver
from page.LoginPage import LoginHoom
from page.RegisterPage import Register
from page.SendmessagePage import SendMessage
from page.LoginToastPage import FindToast


class CaseTest(unittest.TestCase):
    def setUp(self):
        BD = BaseDriver()
        self.driver = BD.android_driver()
        # StartAction(self.driver).swipe_left(n=2)

    # 注册
    def test_repetition_name(self):
        Re = Register(self.driver)
        Re.register_login()

    # 不符合要求的用户名（用户名少于6位）
    def test_username_unqualified(self):
        Re = Register(self.driver)
        Re.register_login1()
        Re.get_toast(self.driver)

    # 不符合要求的用户名（用户名大于12位）
    def test_username_unqualified1(self):
        Re = Register(self.driver)
        Re.register_login2()
        Re.get_toast(self.driver)

    # 错误的用户名
    def test_username_error(self):
        FT = FindToast(self.driver)
        FT.error_username()
        FT.get_toast(self.driver)

    # 错误的密码
    def test_password_error(self):
        FT = FindToast(self.driver)
        FT.error_password()
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
