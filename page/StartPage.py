# !/usr/bin/python
# -*- coding:UTF-8 -*-


class StartAction:
    def __init__(self, appium_driver):
        self.driver = appium_driver

    # 向左滑动屏幕
    def swipe_left(self, n=1, t=500):
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.75
        y1 = l['height'] * 0.5
        x2 = l['width'] * 0.2
        for i in range(n):
            self.driver.swipe(x1, y1, x2, y1, t)

    # # 向右滑动屏幕
    # def swipe_Right(self, n=1):
    #     l = self.driver.get_window_size()
    #     x1 = l['width'] * 0.25
    #     y1 = l['height'] * 0.5
    #     x2 = l['width'] * 0.75
    #     self.driver.swipe(x1, y1, x2, y1)
    #
    #
    # # 向上滑动屏幕
    # def swipe_up(self, n=1, t=500):
    #     l = self.driver.get_window_size()
    #     x1 = l['width'] * 0.5
    #     y1 = l['height'] * 0.75
    #     y = l['height'] * 0.25
    #     for i in range(n):
    #         self.driver.swipe(x1, y1, x1, y, t)
    #
    #
    # # 向上滑动屏幕
    # def swipe_Down(self, n=1):
    #     l = self.driver.get_window_size()
    #     x1 = l['width'] * 0.5
    #     y1 = l['height'] * 0.25
    #     y = l['height'] * 0.75
    #     self.driver.swipe(x1, y1, x1, y)

    # def swipe_On(self, direction):
    #     if direction == "up":
    #         swipe_Up()
    #     elif direction == "down":
    #         swipe_Down()
    #     elif direction == "left":
    #         swipe_Left()
    #     else:
    #         swipe_Right()


# if __name__ == '__main__':
#     StartAction("appium_driver").swipe_Left(n=2)
