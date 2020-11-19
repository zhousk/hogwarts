from appium.webdriver.common.mobileby import MobileBy

# from app.page.contact_page import ContactPage
from app.page.base_page import BasePage


class PersonalEditPage(BasePage):
    def delete_member(self):
        self.driver.find_element(MobileBy.XPATH,"//*[@text='删除成员']").click()
        self.driver.find_element(MobileBy.XPATH,"//*[@text='确定']").click()
        # return ContactPage(self.driver)