from appium.webdriver.common.mobileby import MobileBy

from app.page.base_page import BasePage
from app.page.personal_edit_page import PersonalEditPage


class PersonalDetailPage(BasePage):
    def goto_personal_edit_page(self):
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/i6d").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='编辑成员']").click()
        return PersonalEditPage(self.driver)
