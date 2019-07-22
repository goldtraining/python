import unittest
from selenium import webdriver
from Pages.login_page import LoginPage


class LoginTests(unittest.TestCase):

    driver = webdriver.Chrome()
    login_page = LoginPage(driver)

    @classmethod
    def setUpClass(cls):
        cls.driver.maximize_window()
        cls.driver.get(cls.XML.find("URL").text)
        cls.driver.implicitly_wait(5)

    def test_valid_login(self):
        self.login_page.valid_login()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    if __name__ == '__main__':
        unittest.main(verbosity=2)
