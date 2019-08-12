import time
from base.base_driver import init_driver
from page.page import Page


class TestAddress:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(2)
        # self.driver.quit()

    def test_address(self):
        # 首页 点击 我的
        self.page.home_page.click_mine()
        # 我的 点击 设置
        self.page.mine_page.click_setting()

        # 判断 是否已登录
        if not self.page.setting_page.is_logined():
            # 如果没有登录，此时页面会来到登录页面，直接输入用户名和密码即可
            # 登录 输入用户名
            self.page.login_and_sign_up_page.input_phone("18513107283")
            # 登录 输入密码
            self.page.login_and_sign_up_page.input_password("123456")
            # 登录 点击登录
            self.page.login_and_sign_up_page.click_login()
            # 登录成功后会自动的回到，"我的"页面
            assert self.page.login_and_sign_up_page.is_login_toast("登录成功")


