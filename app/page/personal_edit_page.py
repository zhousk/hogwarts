from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

from app.page.base_page import BasePage


class PersonalEditPage(BasePage):
    def delete_member(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='删除成员']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='确定']").click()
        # 局部调用比面循环调用问题
        from app.page.contact_page import ContactPage
        return ContactPage(self.driver)

    def edit_member(self, name, gender, phonenum, mail=None, address=None):
        # 先找父类，再找子类，值得借鉴
        self.find(MobileBy.XPATH, '//*[contains(@text, "姓名")]/../android.widget.EditText').send_keys(
            name)
        self.find(MobileBy.XPATH, "//*[@text='性别']/..//*[@text='男']").click()
        if gender == "男":
            WebDriverWait(self.driver, 10).until(lambda x: x.find_element(MobileBy.XPATH, "//*[@text='女']"))
            self.find(MobileBy.XPATH, "//*[@text='男']").click()
        else:
            self.find(MobileBy.XPATH, "//*[@text='女']").click()
        self.find(MobileBy.XPATH, "//*[@text='手机号']").send_keys(phonenum)

        if mail is not None:
            self.find(MobileBy.XPATH, '//*[contains(@text, "邮箱")]/../android.widget.EditText').send_keys(mail)
        if address is not None:
            self.find(MobileBy.XPATH, '//*[contains(@text, "地址")]/..//*android.widget.ImageView').click()
            self.find(MobileBy.XPATH, "//*[@text='请输入公司地址，例如“腾讯大厦”']").send_keys(address)
            self.find(MobileBy.XPATH, "//*[@text='确定']").click()

        self.find(MobileBy.XPATH, "//*[@text='保存']").click()
        from app.page.contact_page import ContactPage
        return ContactPage(self.driver)
