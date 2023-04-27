from selenium import webdriver
from time import sleep

class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Safari()
        self.driver.get('https://www.baidu.com/')
        self.driver.maximize_window()

        kw = self.driver.find_element_by_id("kw")
        kw.send_keys("AP Capital")
        self.driver.find_element_by_id("su").click()

        sleep(6)
        self.driver.quit()

if __name__ == '__main__':
    case = TestCase()




