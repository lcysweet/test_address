import time
import sys
sys.path.append('D:\\Projects\workes\\user_login')
from base.base_driver import init_driver
from page.page import Page
class TestLogin:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(2)
        self.driver.quit()

    def test_login(self):
        self.page.home_page.click_mine()
        self.page.mine_page.click_login_and_sign_up()
        self.page.login_and_sign_up_page.input_phone("18513107283")
        self.page.login_and_sign_up_page.input_password("123456")
        self.page.login_and_sign_up_page.click_login()
        assert self.page.login_and_sign_up_page.find_toast("登录成功")


    def test_login_f(self):
        self.page.home_page.click_mine()
        self.page.mine_page.click_login_and_sign_up()
        self.page.login_and_sign_up_page.input_phone("18513107283")
        self.page.login_and_sign_up_page.input_password("12345")
        self.page.login_and_sign_up_page.click_login()
        assert self.page.login_and_sign_up_page.find_toast("密码错误")

