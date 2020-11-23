import yaml
import pytest

from selenium import webdriver


def load_data(path):
    with open(path, encoding='utf-8') as f:
        return yaml.safe_load(f)


class TestDemo:

    def setup_class(self):
        self.data = load_data("test_data.yaml")

    @pytest.mark.parametrize('send_value', load_data('test_data.yaml')['send_value'])
    def test_demo(self,send_value):
        # print(self.data)
        for step in self.data["steps"]:
            if 'webdriver' in step:
                browser = step.get('webdriver').get('browser')
                if browser == 'chrome':
                    driver = webdriver.Chrome()
                elif browser == 'firefox':
                    driver = webdriver.Firefox()
                else:
                    raise Exception("no such browser")

            if 'get' in step:
                url = step.get('get')
                driver.get(url)

            if 'find_element' in step:
                operate = step.get('find_element')
                element = driver.find_element(operate['by'], operate['locator'])
                if 'click' in operate:
                    element.click()
                if 'send_keys' in operate:
                    value= operate.get('send_keys').replace('${value}',send_value)
                    element.send_keys(value)

