from appium.webdriver.common.mobileby import MobileBy

from app.page.base_page import BasePage
from app.page.personal_edit_page import PersonalEditPage
from app.page.search_page import SearchPage


class ContactPage(BasePage):
    def goto_search_page(self):
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/i6n").click()
        return SearchPage(self.driver)

    def add_contact_manually(self):
        self.find(MobileBy.XPATH, "//*[@text='添加成员']").click()
        self.find(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        return PersonalEditPage(self.driver)
