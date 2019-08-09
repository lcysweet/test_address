from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class HomePage(BaseAction):

    mine_button = By.XPATH, "//*[@text='我的' and @resource-id='com.tpshop.malls:id/mine_tv']"

    def click_mine(self):
        self.click(self.mine_button)