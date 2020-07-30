# !/usr/bin/python
# -*- coding:UTF-8 -*-
import unittest

from page.DeletePage import DeleteMessage
from page.DriverPage import BaseDriver
from page.LoginPage import LoginHoom
from page.NewGroupPage import NewGroup
from page.RegisterPage import Register
from page.ReplyMessagePage import ReplyMessage
from page.SendmessagePage import SendMessage
from page.LoginToastPage import FindToast
from page.TransmitMessagePage import TransmitMessage


class CaseTest(unittest.TestCase):
    def setUp(self):
        BD = BaseDriver()
        self.driver = BD.android_driver()
        # StartAction(self.driver).swipe_left(n=2)

    # 注册
    # def test_001_repetition_name(self):
    #     Re = Register(self.driver)
    #     Re.register_login()

    # 不符合要求的用户名（用户名少于6位）
    def test_002_username_unqualified(self):
        Re = Register(self.driver)
        Re.register_login1()
        Re.get_toast(self.driver)

    # 不符合要求的用户名（用户名大于12位）
    def test_003_username_unqualified1(self):
        Re = Register(self.driver)
        Re.register_login2()
        Re.get_toast(self.driver)

    # 错误的用户名
    def test_004_username_error(self):
        FT = FindToast(self.driver)
        FT.error_username()
        FT.get_toast(self.driver)

    # 错误的密码
    def test_005_password_error(self):
        FT = FindToast(self.driver)
        FT.error_password()
        FT.get_toast(self.driver)

    # 登录
    def test_006_login(self):
        LH1 = LoginHoom(self.driver)
        LH1.loginhoom()

    # 从通讯录进入给好友发送消息
    def test_007_send_message(self):
        SM = SendMessage(self.driver)
        SM.send_message()

    # 回复聊天页面的消息
    def test_008_reply(self):
        RM = ReplyMessage(self.driver)
        RM.reply_message()

    # 转发聊天页面的消息
    def test_009_transmit(self):
        TM = TransmitMessage(self.driver)
        TM.transmit_message()
        TM.get_toast(self.driver)

    # 删除聊天页面的消息
    def test_010_delete(self):
        DM = DeleteMessage(self.driver)
        DM.delete_message()

    def test_011_group(self):
        NG = NewGroup(self.driver)
        NG.new_group()

if __name__ == "__main__":
    unittest.main()
