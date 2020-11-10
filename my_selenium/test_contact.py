import time

from selenium import webdriver
import pytest
import yaml
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options


def load_data(path='data.yaml'):
    with open(path) as f:
        data = yaml.safe_load(f)
        return list(data.values())


class TestContacts:
    data = load_data()

    # 命令行指定端口打开命令：chrome - -remote - debugging - port = 9222
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
        self.driver.implicitly_wait(10)
        element.click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id('username').send_keys('neal')
        self.driver.find_element_by_id('memberAdd_acctid').send_keys('nealChen')
        self.driver.find_element_by_id('memberAdd_phone').send_keys('15622771111')
        self.driver.find_element_by_name('sendInvite').click()
        self.driver.find_element_by_link_text("保存并继续添加").click()
        assert self.assert_visible('neal') and self.assert_visible('15622771111')

    @pytest.mark.skip
    def test_cookie(self):
        cookies = self.driver.get_cookies()
        print(cookies)

    def assert_visible(self, message):
        try:
            return self.driver.find_element_by_xpath("//*[contains(text(), '{}')]".format(message))
        except NoSuchElementException:
            return False
        return False
