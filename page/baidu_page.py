#coding=utf-8
try:
    from common.webdriver2 import WebDriver
except ImportError:
    from common.webdriver2 import WebDriver
from time import sleep


class BaiduPage(WebDriver):
    '''
    百度首页
    '''
    url = '/'

    # 百度输入框
    def search_input(self, search_key):
        self.type("#kw", search_key)

    # 百度按钮
    def search_button(self):
        self.click("#su")
        sleep(1)

    # 搜索标题
    def search_title(self):
        return self.get_title()

    # 设置
    def setings(self):
        self.click("link_text=>设置")

    # 搜索设置
    def search_setting(self):
        self.click(".setpref")

    # 保存设置
    def save_seting(self):
        self.click(".prefpanelgo")
        self.accept_alert()
