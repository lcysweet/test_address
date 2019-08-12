import random

import time
from selenium.webdriver.common.by import By
from base.base_action import BaseAction
import allure

class TestAddressRegionPage(BaseAction):
    # 收货人地址 选择区-城市id
    tv_city_button = By.ID,"com.tpshop.malls:id/tv_city"

    # 收货人 选择区-确定按钮
    # city_commit_button = By.ID,"com.tpshop.malls:id/btn_right"
    city_commit_button = By.XPATH,"//*[@text='确定']"

    @allure.step(title="选择区  点击 -随机选择省,市,区,镇")
    def click_random_city(self):
        for _ in range(4):
            # 获取当前屏幕内所有的城市(省,市,区,镇/街道)--因为id一样
            city_list = self.find_elements(self.tv_city_button)
            # 获取城市的长度/个数
            len_cities_count = len(city_list)
            # 根据长度/个数 生成随机下标
            random_index = random.randint(0, len_cities_count-1)
            # 通过随机下标,取一个随机城市,并点击
            city_list[random_index].click()
            time.sleep(3)

    @allure.step(title="选择区 点击 -确定按钮")
    def click_city_commit(self):
        self.click(self.city_commit_button)