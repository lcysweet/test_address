from appium import webdriver


def init_driver():
    """
    只要调用，就可以打开对应的应用程序
    :return:
    """
    # server 启动参数
    desired_caps = {}
    # 设备信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    desired_caps['deviceName'] = '192.168.56.101:5555'
    # app的信息
    desired_caps['appPackage'] = 'com.android.systemui'
    desired_caps['appActivity'] = '.recents.RecentsActivity'
    # 不要重置应用
    desired_caps['noReset'] = True
    # 解决中文
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True

    # 声明我们的driver对象
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    # 判断app是否安装
    if driver.is_app_installed('com.android.systemui'):
        # 如果安装就卸载
        driver.remove_app('com.android.systemui')
    else:
        # 否则就安装
        driver.install_app('D:\apk\com.tpshop.malls_2.2.5_225.apk')

    return driver


