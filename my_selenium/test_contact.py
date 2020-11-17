import time

from selenium import webdriver
import pytest
import yaml
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


def load_data(path='data.yaml'):
    with open(path) as f:
        data = yaml.safe_load(f)
        return list(data.values())


class TestContacts:
    data = load_data()

    # 命令行指定端口打开命令：chrome - -remote - debugging - port = 9222
    #复用浏览器是为了跳过登陆的过程，手动登陆，然后复用就行
    def setup(self):
        # option = Options()
        # option.debugger_address = '127.0.0.1:9222'
        # self.driver = webdriver.Chrome(options=option)
        # self.driver.get('https://work.weixin.qq.com/wework_admin/frame#contacts')
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    # 忽略了验证input的过程，算是偷懒了
    @pytest.mark.parametrize('data',
                             data
                             )
    def test_add_contacts(self, data):

        name = 'neal'
        phone = '15622771111'

        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#contacts')
        cookies = data

        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)
        self.driver.refresh()
        time.sleep(10)

        element = self.driver.find_element_by_xpath(
            "//div[@class='ww_operationBar']//*[@class='qui_btn ww_btn js_add_member']")
        print("文本是", element.text)
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(
            (By.XPATH, "//div[@class='ww_operationBar']//*[@class='qui_btn ww_btn js_add_member']")))
        element.click()
        self.driver.find_element_by_id('username').send_keys(name)
        self.driver.find_element_by_id('memberAdd_acctid').send_keys('nealChen')
        self.driver.find_element_by_id('memberAdd_phone').send_keys(phone)
        self.driver.find_element_by_name('sendInvite').click()
        self.driver.find_element_by_link_text("保存并继续添加").click()
        assert self.assert_visible('%s' % name) and self.assert_visible('%s' % phone)

    @pytest.mark.skip
    def test_cookie(self):
        cookies = self.driver.get_cookies()
        print(cookies)

    # 验证添加成员成功
    def assert_visible(self, message):
        try:
            return self.driver.find_element_by_xpath("//*[contains(text(), '{}')]".format(message))
        except NoSuchElementException:
            return False
        return False
