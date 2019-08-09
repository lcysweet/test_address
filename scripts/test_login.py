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
        self.page.home_page.click_mine()
        self.page.mine_page.click_login_and_sign_up()
        self.page.login_and_sign_up_page.input_phone(phone)
        self.page.login_and_sign_up_page.input_password(password)
        self.page.login_and_sign_up_page.click_login()
        assert self.page.login_and_sign_up_page.find_toast(expect)


    def test_login_f(self):
        self.page.home_page.click_mine()
        self.page.mine_page.click_login_and_sign_up()
        self.page.login_and_sign_up_page.input_phone("18513107283")
        self.page.login_and_sign_up_page.input_password("12345")
        self.page.login_and_sign_up_page.click_login()
        assert self.page.login_and_sign_up_page.find_toast("密码错误")

