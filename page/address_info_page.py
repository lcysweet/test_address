from selenium.webdriver.common.by import By
from base.base_action import BaseAction
import allure

class TestAddressInfoPage(BaseAction):
    # 收货人信息
    consignee_name_et_text = By.ID,"com.tpshop.malls:id/consignee_name_et"
    # 收货人电话
    consignee_mobile_et_text = By.ID, "com.tpshop.malls:id/consignee_mobile_et"
    # 收货人所在区
    consignee_region_tv_button = By.ID, "com.tpshop.malls:id/consignee_region_tv"
    # 收货人详细地址
    consignee_address_et_text = By.ID, "com.tpshop.malls:id/consignee_address_et"
    # 默认收获地址
    set_default_sth_button = By.ID,"com.tpshop.malls:id/set_default_sth"
    # 保存收货地址按钮
    save_tv_button = By.ID, "com.tpshop.malls:id/save_tv"



    @allure.step(title="输入-收货人信息")
    def input_consignee_name(self,text):
        self.input(self.consignee_name_et_text,text)

    @allure.step(title="输入 收货人电话")
    def input_consignee_mobile(self,text):
        self.input(self.consignee_mobile_et_text,text)

    @allure.step(title="点击 收货人所在区")
    def click_consignee_region(self):
        self.click(self.consignee_region_tv_button)

    @allure.step(title="输入 收货人详细地址")
    def input_consignee_address(self,text):
        self.input(self.consignee_address_et_text,text)

    @allure.step(title="点击 保存收货地址按钮")
    def click_consignee_save(self):
        self.click(self.save_tv_button)