from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException

from app.page.base_page import BasePage
from app.page.personal_detail_page import PersonalDetailPage


class SearchPage(BasePage):
    def search(self, value):
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/gpg").send_keys(value)
        try:
            return self.driver.find_elements(MobileBy.ID, "com.tencent.wework:id/b6b")
        except NoSuchElementException:
            return []

    def goto_personal_detail_page(self, element: WebElement):
        element.click()
        return PersonalDetailPage(self.driver)
