import time
import sys
sys.path.append('D:\\Projects\workes\\test_address')
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

        # 1-判断 是否已登录
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
            print("判断 是否已登录成功")

        # 2-点击地址管理
        self.page.mine_page.click_address()
        print("点击地址管理")
        # 3-点击新建收货地址
        self.page.address_list_page.click_new_address()
        # 4-填写 收货人姓名
        self.page.address_info_page.input_consignee_name("李春燕")
        # 5-填写 收货人手机号
        self.page.address_info_page.input_consignee_mobile("18513107283")
        # 6-点击 收货人区域
        self.page.address_info_page.click_consignee_region()
        # 6-1 随机 选择区域
        self.page.address_region_page.click_random_city()
        # 6-2 确定
        self.page.address_region_page.click_city_commit()
        # 7-填写 详细地址
        self.page.address_info_page.input_consignee_address("龙跃苑东四区 5号楼 1单元")
        # 8-点击 保存地址按钮
        self.page.address_info_page.click_consignee_save()
        # 9-断言 收货地址toast添加成功
        assert self.page.address_info_page.is_save_toast("添加成功")
        print("断言 添加收货地址")




