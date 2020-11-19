from appium.webdriver.common.mobileby import MobileBy

from app.page.contact_page import ContactPage
from app.page.base_page import BasePage


class IndexPage(BasePage):
    def goto_contact_page(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        return ContactPage(self.driver)
