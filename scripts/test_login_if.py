import time
import pytest
import sys
sys.path.append('D:\\Projects\workes\\user_login')
from base.base_driver import init_driver
from page.page import Page
from base.base_analyze import analyze_data


class TestLogin:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(2)
        self.driver.quit()

    # 登录名和密码有一个为空判断登录按钮是否可用状态
    @pytest.mark.parametrize("args", analyze_data("login_data_if", "test_login_if"))
    def test_login_if(self, args):
        # 获取数据
        username = args["phone"]
        password = args["password"]
        # 首页 - 点击 我
        self.page.home_page.click_mine()
        # 注册 - 点击 登录/注册
        self.page.mine_page.click_login_and_sign_up()
        # 登录- 输入 用户名
        self.page.login_and_sign_up_page.input_phone(username)
        # 登录- 输入 密码
        self.page.login_and_sign_up_page.input_password(password)

        # 判断登录按钮是否可用
        assert not self.page.login_and_sign_up_page.is_login_enabled("enabled")

        # if self.page.login_and_sign_up_page.is_login_enabled() == False:
        #     assert True
        # else:
        #     assert False