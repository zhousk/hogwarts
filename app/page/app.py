from appium import webdriver

from app.page.base_page import BasePage
from app.page.main import Main


class App(BasePage):

    def start(self):
        if self.driver == None:
            print("driver == None")
            caps = {}
            caps["platformName"] = "Android"
            caps["platformVersion"] = "5"
            caps["deviceName"] = "127.0.0.1:62001"
            caps["appPackage"] = "com.tencent.wework"
            caps["appActivity"] = ".launch.LaunchSplashActivity"
            caps["noReset"] = True
            # 最重要的代码，建立客户端与服务端的连接
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            self.driver.implicitly_wait(5)
        else:
            print("driver is not None")
            # 启动app, 启动的页面是desirecaps 里面设置的activity
            self.driver.launch_app()
            # self.driver.start_activity("com.tencent.wework",".launch.LaunchSplashActivity")
        return self

    def restart(self):
        pass

    def stop(self):
        self.driver.quit()

    def goto_main(self):
        return Main(self.driver)