from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from my_selenium.podemo.add_member_oage import AddMemberPage
from my_selenium.podemo.base_page import BasePage


class IndexPage(BasePage):

    # 覆盖父类的类变量
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"


    def add_member(self):
        self.driver.find_element_by_class_name("index_service_cnt_itemWrap").click()
        return AddMemberPage(self.driver)