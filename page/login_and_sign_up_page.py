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


    # 判断 登录后toast文本内容
    @allure.step(title='判断登录后toast文本')
    def is_login_toast(self, content):
        try:
            self.find_toast(content)
            return True
        except Exception as e:
            return False

    # 判断 登录按钮是否可用
    @allure.step(title='判断登录按钮是否可用')
    def is_login_enabled(self,attribute):
        """
        判断 登录按钮中的 enabled 属性值 是不是 可用的
        true 表示可用
        false 表示不可用
        :return: 是否可用
        """
        return self.find_element(self.login_button).get_attribute(attribute) == "true"

        # if self.find_element(self.login_button).get_attribute("enabled") == "true":
        #     return True
        # else:
        #     return False
        # try:
        #     self.find_get_attribute(self.login_button)
        #     return True
        # except Exception as e:
        #     return False