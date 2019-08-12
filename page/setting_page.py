import allure
from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class SettingPage(BaseAction):
    # 设置 标题
    setting_title = By.ID,"com.tpshop.malls:id/title_tv"

    # 设置 获取title文本
    @allure.step(title=" 设置 获取文本")
    def get_title(self):
        return self.find_element(self.setting_title).text

    # 判断 文本title
    @allure.step(title="判断是否登录 点击齿轮的标题是否设置")
    def is_logined(self):
        return self.get_title() == "设置"