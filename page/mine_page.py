import allure
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class MinePage(BaseAction):
    # 登录 - 登录/注册
    # login_and_sign_up_button = By.XPATH, "//*[@text='登录/注册']"
    login_and_sign_up_button = By.ID,"com.tpshop.malls:id/head_img"

    # 设置
    setting_button = By.ID,"com.tpshop.malls:id/setting_btn"

    # 我的 - 设置
    def click_setting(self):
        self.click(self.setting_button)

    # 我的 - 登录/注册
    @allure.step(title="点击登录/注册按钮")
    def click_login_and_sign_up(self):
        self.click(self.login_and_sign_up_button)
        # WebDriverWait(self.driver,  timeout=10.0, poll=1.0).until(lambda x: x.find_elements(By.ID,"com.tpshop.malls:id/head_img")).click()