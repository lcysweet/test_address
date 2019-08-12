import allure
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class MinePage(BaseAction):
    # 登录 - 登录/注册
    # login_and_sign_up_button = By.XPATH, "//*[@text='登录/注册']"
    login_and_sign_up_button = By.ID,"com.tpshop.malls:id/head_img"

    # 设置
    setting_button = By.ID,"com.tpshop.malls:id/setting_btn"

    # 地址管理
    address_button = By.XPATH,"//*[@text='地址管理']"


    # 我的 - 登录/注册
    @allure.step(title="我的 点击 -登 录/注册按钮")
    def click_login_and_sign_up(self):
        self.click(self.login_and_sign_up_button)
        # WebDriverWait(self.driver,  timeout=10.0, poll=1.0).until(lambda x: x.find_elements(By.ID,"com.tpshop.malls:id/head_img")).click()

    # 我的 - 设置
    @allure.step(title="我的 点击 - 设置")
    def click_setting(self):
        self.click(self.setting_button)

    # 3-我的 - 地址管理
    @allure.step(title="我的 点击 - 地址管理")
    def click_address(self):
        self.swipe_find(self.address_button).click()

    """
     # 1-我的 - 地址管理
    @allure.step(title="我的 点击 - 地址管理")
    def click_address(self):
        self.click_swipe_while(self.address_button)
    """

    """
    # 2-我的 - 地址管理
    @allure.step(title="我的 点击 - 地址管理")
    def click_address(self):
        # 如果有就点击地址管理
        # 如果没有就滑动
        while True:
            # 获取当前的页面元素
            source = self.driver.page_source
            try:
                # find_element :根据元素特征找到元素并返回
                self.find_element(self.address_button).click()
                # self.click(self.click_address)
                break
            except Exception:
                # 调用封装滑动
                self.swipe_one_time()
                # 4 判断 当前的页面和之前的保存的页面是否一致
                if source == self.driver.page_source:
                    # 滑动到底部
                    raise Exception("滑动到底")
        """

"""
    # 1-我的 - 地址管理
    @allure.step(title="我的 点击 - 地址管理")
    def click_address(self):
        # 如果有就点击地址管理
        # 如果没有就滑动
        while True:
            # 获取当前的页面元素
            source = self.driver.page_source
            try:
                # find_element :根据元素特征找到元素并返回
                self.find_element(self.address_button).click()
                # self.click(self.click_address)
                break
            except Exception:
                # 调用封装滑动
                 # 1-获取屏幕分辨率,根据分辨率宽和高  从 3/4 滑动到 1/4
                window_size = self.driver.get_window_size()
                # 屏幕宽度["width"]
                width = window_size["width"]
                # 屏幕高度["height"]
                height = window_size["height"]

                # 2-坐标点 元素开始的坐标(x,y) --元素结束的坐标(x,y)
                start_x = width * 0.5
                start_y = height * 0.75
                end_x = start_x
                end_y = height * 0.25

                # 3- 开始滑动swipe:
                self.driver.swipe(start_x, start_y, end_x, end_y, 3000)
                # 4 判断 当前的页面和之前的保存的页面是否一致
                if source == self.driver.page_source:
                    # 滑动到底部
                    raise Exception("滑动到底")
        """
