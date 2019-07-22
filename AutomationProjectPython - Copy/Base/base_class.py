from xml.etree import ElementTree
import traceback


class BaseClass:

    def __init__(self, driver):
        self.driver = driver
        self.XML = ElementTree.parse("C:\\seleniumDrivers\\config.xml")

    def enter_text(self, By, element, value):
        try:
            element = self.driver.find_element(By, element)
            element.clear()
            element.send_keys(value)
            print("enter_text - Was Successful")
        except:
            print("update_text_field - Failed")
            self.fail("enter_text - Failed" + str(element) + str(traceback.format_exc()))

    def click_element(self, By, element):
        try:
            element = self.driver.find_element(By, element)
            element.click()
        except:
            print("Could not click on Element!")
            self.fail("The click failed" + str(element) + str(traceback.format_exc()))



