from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from my_selenium.podemo.base_page import BasePage


class AddMemberPage(BasePage):
    # def __init__(self,driver:WebDriver):
    #     self.driver = driver

    def add_member(self):
        # input name
        self.driver.find_element_by_id("username").send_keys("xiaoming")
        self.driver.find_element_by_id("memberAdd_acctid").send_keys("123345")
        self.driver.find_element_by_id("memberAdd_phone").send_keys("123")
        # 匹配到多个元素，会选第一个
        self.driver.find_element_by_class_name("qui_btn ww_btn js_btn_save")
        return True

    # 判断指定人是否有添加，返回真假
    def get_member(self, value):
        elements = self.finds(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        # for 直接括起来就是队列，很方便
        titles = [element.get_attribute("title") for element in elements]
        # 没有写类型，就要直接写出extend，提示都没有，没有编译过程真的考验记忆力
        title_total = []
        title_total.extend(titles)
        if value in titles:
            return True
        page: str = self.find(By.CSS_SELECTOR, ".ww_pageNav_info_text")
        # "1/2分割为1，2，这里省略了括号"
        num, total = page.split("/", 1)
        # 到最后一页都没有找到
        if num == total:
            return False
        else:
            self.find(By.CSS_SELECTOR, ".ww_commonImg_PageNavArrowRightNormal").click()
        # 其实这是废的
        return titles