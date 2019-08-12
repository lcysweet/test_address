from selenium.webdriver.common.by import By
from base.base_action import BaseAction
import allure

class TestAddressListPage(BaseAction):
    # 地址 新建地址按钮
    new_address_button = By.ID,"com.tpshop.malls:id/add_address_tv"

    @allure.step(title="收货人地址  点击 -新建地址按钮")
    def click_new_address(self):
        self.click(self.new_address_button)