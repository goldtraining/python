from selenium.webdriver.common.by import By
from Base.base_class import BaseClass


class LoginPage(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    username_field = "username2"
    password_field = "password2"
    submit_button = "submit"

    def valid_login(self,):
        self.enter_text(By.NAME, self.username, self.XML.find("username").text)
        self.enter_text(By.NAME, self.password_field, self.XML.find("password").text)
        self.click_element(By.NAME, self.submit_button)

