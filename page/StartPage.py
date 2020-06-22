# !/usr/bin/python
# -*- coding:UTF-8 -*-
from appium.webdriver.common.touch_action import TouchAction


class StartAction:
    def __init__(self, appium_driver):
        self.driver = appium_driver

    # 向左滑动屏幕
    def swipe_left(self, n=1, t=500):
        size = self.driver.get_window_size()
        x1 = size['width'] * 0.75
        y1 = size['height'] * 0.5
        x2 = size['width'] * 0.2
        for i in range(n):
            self.driver.swipe(x1, y1, x2, y1, t)

    # # 向右滑动屏幕
    # def swipe_Right(self, n=1):
    #     size = self.driver.get_window_size()
    #     x1 = size['width'] * 0.25
    #     y1 = size['height'] * 0.5
    #     x2 = size['width'] * 0.75
    #     self.driver.swipe(x1, y1, x2, y1)
    #
    #
    # # 向上滑动屏幕
    # def scroll_up(self):
    #     size = self.driver.get_window_size()
    #     for i in range(3):
    #         TouchAction(self.driver) \
    #             .long_press(x=size['width'] * 0.5, y=size['height'] * 0.8) \
    #             .move_to(x=size['width'] * 0.5, y=size['height'] * 0.2) \
    #             .release() \
    #             .perform()

    #
    #
    # # 向上滑动屏幕
    # def scroll_down(self):
    #     size = self.driver.get_window_size()
    #     for i in range(3):
    #         TouchAction(self.driver) \
    #             .long_press(x=size['width'] * 0.5, y=size['height'] * 0.2) \
    #             .move_to(x=size['width'] * 0.5, y=size['height'] * 0.8) \
    #             .release() \
    #             .perform()



# if __name__ == '__main__':
#     StartAction("appium_driver").swipe_Left(n=2)
