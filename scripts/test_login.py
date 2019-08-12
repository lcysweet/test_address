import sys
sys.path.append('D:\\Projects\workes\\test_address')
from base.base_driver import init_driver
import random
import time
import pytest
from page.page import Page
from base.base_analyze import analyze_data

def random_password():
    password = ""
    for i in range(8):
        password += str(random.randint(0, 9))
    return password

class TestLogin:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(2)
        self.driver.quit()

    # 1登录参数化正常流程
    @pytest.mark.parametrize("args", analyze_data("login_data", "test_login"))
    def test_login(self, args):
        # 解析数据
        username = args["phone"]
        password = args["password"]
        toast = args["expect"]

        # 首页 - 点击 我
        self.page.home_page.click_mine()
        # 注册 - 点击 登录/注册
        self.page.mine_page.click_login_and_sign_up()
        # 登录- 输入 用户名
        self.page.login_and_sign_up_page.input_phone(username)
        # 登录- 输入 密码
        self.page.login_and_sign_up_page.input_password(password)
        # 登登录 - 点击 登录
        self.page.login_and_sign_up_page.click_login()
        # 断言 toast
        assert self.page.login_and_sign_up_page.is_login_toast(toast)
        print("判断 登录参数化")

    # 2判断 登录名和密码有一个为空登录按钮是否可用状态
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
        print("判断 登录按钮 是否可用")
        # if self.page.login_and_sign_up_page.is_login_enabled() == False:
        #     assert True
        # else:
        #     assert False
        # 登录名和密码有一个为空判断登录按钮是否可用状态

    # 3判断 密码眼睛是否可用
    @pytest.mark.parametrize("password", [random_password(), random_password()])
    def test_show_password(self,password):
        # 首页 - 点击 我
        self.page.home_page.click_mine()
        # 注册 - 点击 登录/注册
        self.page.mine_page.click_login_and_sign_up()
        # 登录- 输入 密码
        self.page.login_and_sign_up_page.input_password(password)
        # 判断 输入的密码找不到
        assert not self.page.login_and_sign_up_page.is_password_eys_show(password)
        # 点击显示密码
        self.page.login_and_sign_up_page.click_show_password_eys()
        # 找到 输入的密码
        assert self.page.login_and_sign_up_page.is_password_eys_show(password)
        print("判断 密码眼睛 是否可用")
        # # 判断-显示密码按钮 是否可用
        # if not self.page.login_and_sign_up_page.is_password_eys_show(password):
        #     # 点击显示密码
        #     self.page.login_and_sign_up_page.click_show_password_eys()
        #     # 截图，上传到报告
        #     allure.attach("截图：", self.driver.get_screenshot_as_png(), allure.attach_type.PNG)
        #     # 找到显示密码 判断 找到的密码和显示的密码是否一致
        #     assert self.page.login_and_sign_up_page.is_password_eys_show(password)



