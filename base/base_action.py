from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:

    # 因为这个类中的其他对象方法需要使用driver对象
    def __init__(self, driver):
        self.driver = driver

    # 根据元素特征找元素并返回
    def find_element(self, feature, timeout=10.0, poll=1.0):
        """
        根据元素的从特征（元组），定位对应的元素
        :param feature: 特征
        :param timeout: 超时时间
        :param poll: 每多久照一次
        :return: 找到元素本身
        """
        # by = feature[0]
        # value = feature[1]
        # by, value = feature
        # element = self.driver.find_element(by, value)
        by, value = feature
        element = WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(by, value))
        return element

    # 根据元素特征找到并返回
    def find_elements(self, feature, timeout=10.0, poll=1.0):
        """
        根据元素的从特征（元组），定位符合特征条件的多个元素
        :param feature: 特征
        :param timeout: 超时时间
        :param poll: 每多久照一次
        :return: 列表，符合条件的元素
        """
        by, value = feature
        element = WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(by, value))
        return element
        # 点击

    def clicks(self, feature, timeout=10.0, poll=1.0):
        """
        根据传进来的特征，去找对应的元素，并且点击
        :param feature: 特征
        :param timeout: 超时时间
        :param poll: 每多久照一次
        """
        self.find_elements(feature, timeout, poll).click()
    # 点击
    def click(self, feature, timeout=10.0, poll=1.0):
        """
        根据传进来的特征，去找对应的元素，并且点击
        :param feature: 特征
        :param timeout: 超时时间
        :param poll: 每多久照一次
        """
        self.find_element(feature, timeout, poll).click()

    # 输入
    def input(self, feature, text, timeout=10.0, poll=1.0):
        """
        根据传进来的特征，去找对应的元素，并且输入文字
        :param feature: 特征
        :param text: 要输入的文字
        :param timeout: 超时时间
        :param poll: 每多久照一次
        """
        self.find_element(feature, timeout, poll).send_keys(text)

    # 清除
    def clear(self, feature, timeout=10.0, poll=1.0):
        """
        根据传进来的特征，去找对应的元素，并且清空
        :param feature: 特征
        :param timeout: 超时时间
        :param poll: 每多久照一次
        """
        self.find_element(feature, timeout, poll).clear()

    # 获取toast文本并返回
    def find_toast(self, content):
        """
        根据部分toast内容，获取全部的toast内容
        :param content: 部分内容
        :return: 全部内容
        """
        feature = By.XPATH, "//*[contains(@text,'" + content + "')]"
        return self.find_element(feature, 5, 0.1).text
        # return self.find_element(By.XPATH,"//*[contains(@text,'" + content + "')]").text

    # 滑动一次
    def swipe_one_time(self,dir="bottom"):
        """
        滑动 半屏 从4/3 到 4/1
        :Parma dir:方向
        top:从上往下
        bottom:从下往上
        left:从左向右
        right:从右向左
        """
        # 1- 获取屏幕分辨率 宽和高
        window_size = self.driver.get_window_size()
        width = window_size["width"]
        height = window_size["height"]

        # 2-元素坐标点
        # 上
        top_x = width * 0.5
        top_y = height * 0.25
       # 下
        bottom_x = top_x
        bottom_y = height * 0.75
        # 左
        left_x = height * 0.5
        left_y = height * 0.25
        # 右
        right_x = left_x
        right_y = height * 0.75

        # 判断 滑动方向
        if dir == "top":
            self.driver.swipe(top_x, top_y, bottom_x, bottom_y)
        elif dir == "bottom":
            self.driver.swipe( bottom_x, bottom_y,top_x, top_y )
        elif dir == "left":
            self.driver.swipe(left_x, left_y, right_x, right_y)
        elif dir == "right":
            self.driver.swipe( right_x, right_y,left_x, left_y )
        else:
            raise Exception("请输入正确的参数 top/bottom/lef/right")

    # 循环滑动 边滑边找
    def swipe_find(self,feature,dir="bottom"):
        """
        边滑边找,如果找到就返回,如果没有就抛异常
        :param feature:元素特征
        :return:返回元素
        """
        while True:
            # 获取当前的页面元素
            source = self.driver.page_source
            try:
                # 根据元素特征找到元素并返回
                return self.find_element(feature)
            except Exception:
                # 调用封装滑动
                self.swipe_one_time(dir)
                # 4 判断 当前的页面和之前的保存的页面是否一致
                if source == self.driver.page_source:
                    # 滑动到底部
                    raise Exception("滑动到底")

    # 循环滑动点击 默认从下往上循环滑动
    def click_swipe_while(self,feature,dir="bottom"):
        # 如果没有就滑动
        while True:
            # 获取当前的页面元素
            source = self.driver.page_source
            try:
                # find_element :根据元素特征找到元素并返回
                self.find_element(feature).click()
                break
            except Exception:
                # 调用封装滑动
                self.swipe_one_time(dir)
                # 4 判断 当前的页面和之前的保存的页面是否一致
                if source == self.driver.page_source:
                    # 滑动到底部
                    raise Exception("滑动到底")



