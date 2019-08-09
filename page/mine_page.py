import allure
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class MinePage(BaseAction):

    # login_and_sign_up_button = By.XPATH, "//*[@text='登录/注册']"
    login_and_sign_up_button = By.ID,"com.tpshop.malls:id/head_img"
    @allure.step("点击登录/注册按钮")
    def click_login_and_sign_up(self):
        self.click(self.login_and_sign_up_button)
        # WebDriverWait(self.driver,  timeout=10.0, poll=1.0).until(lambda x: x.find_elements(By.ID,"com.tpshop.malls:id/head_img")).click()