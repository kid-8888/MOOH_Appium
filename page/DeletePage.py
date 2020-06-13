# !/usr/bin/python
# -*- coding:UTF-8 -*e
from selenium.webdriver.common.by import By


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
    delete_button = (By.ID, "com.showfires.im:id/chat_transmit_delete_tv")
