import logging

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class BasePage:
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename='../log/myapp.log',
                        filemode='w')

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, by, locator):
        logging.info("find:")
        logging.info(by)
        logging.info(locator)

        return self.driver.find_element(by, locator)

    def find_by_scroll(self, text):
        logging.info("find_by_scroll")
        logging.info(text)
        return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                        'new UiScrollable(new UiSelector()'
                                        '.scrollable(true).instance(0))'
                                        '.scrollIntoView(new UiSelector()'
                                        f'.text("{text}").instance(0));')

    def get_toast_text(self):
        logging.info("get toast:")
        result = self.find(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        logging.info(result)
        return result

    def verify_toast(self):
        # result = self.find(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        result = self.get_toast_text()
        return result