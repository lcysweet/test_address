import time
import pytest
import sys
sys.path.append('D:\\Projects\workes\\user_login')
from base.base_driver import init_driver
from page.page import Page
from base.base_analyze import analyze_file


class TestLogin:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(2)
        self.driver.quit()
    @pytest.mark.parametrize(("phone","password","expect"),analyze_file("login_data","test_login"))
    def test_login(self,phone,password,expect):
        # 首页 - 点击 我
        self.page.home_page.click_mine()
        # 注册 - 点击 登录/注册
        self.page.mine_page.click_login_and_sign_up()
        # 登录- 输入 用户名
        self.page.login_and_sign_up_page.input_phone(phone)
        # 登录- 输入 密码
        self.page.login_and_sign_up_page.input_password(password)
        # 登登录 - 点击 登录
        self.page.login_and_sign_up_page.click_login()
        # 断言 toast
        assert self.page.login_and_sign_up_page.find_toast(expect)
