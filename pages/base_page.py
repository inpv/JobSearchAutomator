from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, time):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def find_element_or_ignore(self, locator, time):
        try:
            return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                          message=f"Can't find elements by locator {locator}")
        except TimeoutException:
            pass

    def go_to_page(self, page):
        return self.driver.get(page)
