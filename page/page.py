from page.address_info_page import TestAddressInfoPage
from page.address_list_page import TestAddressListPage
from page.home_page import HomePage
from page.login_and_sign_up_page import LoginAndSignUpPage
from page.mine_page import MinePage
from page.setting_page import SettingPage


class Page:

    def __init__(self, driver):
        self.driver = driver

    # 首页
    @property
    def home_page(self):
        return HomePage(self.driver)

    # 我的
    @property
    def mine_page(self):
        return MinePage(self.driver)

    # 登录/注册
    @property
    def login_and_sign_up_page(self):
        return LoginAndSignUpPage(self.driver)

    # 设置
    @property
    def setting_page(self):
        return SettingPage(self.driver)

    # 收货人地址
    @property
    def address_list_page(self):
        return TestAddressListPage(self.driver)

# 收货人信息
    @property
    def address_info_page(self):
        return TestAddressInfoPage(self.driver)