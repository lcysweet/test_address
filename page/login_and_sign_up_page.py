import allure
from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class LoginAndSignUpPage(BaseAction):
    # 账号
    phone_edit_text = By.ID, "com.tpshop.malls:id/mobile_et"

    # 密码
    password_edit_text = By.ID, "com.tpshop.malls:id/pwd_et"

    # 登录
    login_button = By.ID, "com.tpshop.malls:id/login_tv"

    # 输入 账号
    @allure.step(title="登录页面 - 输入 账号")
    def input_phone(self, text):
        self.input(self.phone_edit_text, text)

    # 输入 密码
    @allure.step(title="登录页面 - 输入 密码")
    def input_password(self, text):
        self.input(self.password_edit_text, text)

    # 点击 登陆
    @allure.step(title="登录页面 - 点击 登录")
    def click_login(self):
        self.click(self.login_button)

    @allure.step(title='判断登录后toast文本')
    def is_login_toast(self, content):
        try:
            self.find_toast(content)
            return True
        except Exception as e:
            return False