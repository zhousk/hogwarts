from appium.webdriver.common.mobileby import MobileBy

from app.page.contact_page import ContactPage
from app.page.base_page import BasePage


class Main(BasePage):
    _contact_list = (MobileBy.XPATH, "//*[@text='通讯录']")

    def goto_contact_page(self):
        '''
       进入到通讯录
       '''
        # 点击【通讯录】
        # *号起到拆分元组的作用
        self.find(*self._contact_list).click()
        return ContactPage(self.driver)
