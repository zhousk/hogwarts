from appium import webdriver
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException


class BasePage:

    def __init__(self, driver: WebDriver = None):
        self.driver = driver
        if self.driver is None:
            caps = {}
            caps["platformName"] = "Android"
            caps["platformVersion"] = "5"
            caps["deviceName"] = "127.0.0.1:62001"
            caps["appPackage"] = "com.tencent.wework"
            caps["appActivity"] = ".launch.LaunchSplashActivity"
            caps["noReset"] = True

            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            self.driver.implicitly_wait(5)
