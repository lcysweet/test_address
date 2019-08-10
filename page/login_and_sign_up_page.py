import allure
from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class LoginAndSignUpPage(BaseAction):

    phone_edit_text = By.ID, "com.tpshop.malls:id/mobile_et"

    password_edit_text = By.ID, "com.tpshop.malls:id/pwd_et"

    login_button = By.ID, "com.tpshop.malls:id/login_tv"

    @allure.step('输入账号')
    def input_phone(self, text):
        self.input(self.phone_edit_text, text)

    @allure.step('输入密码')
    def input_password(self, text):
        self.input(self.password_edit_text, text)

    @allure.step('点击登录')
    def click_login(self):
        self.click(self.login_button)

    @allure.step('判断登录后toast文本')
    def is_login_toast(self, content):
        try:
            self.find_toast(content)
            return True
        except Exception as e:
            return False