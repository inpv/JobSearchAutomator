from pages.base_page import BasePage


class SearchHelper(BasePage):

    def enter_word_into_input(self, locator, word):
        input_field = self.find_element(locator)
        input_field.click()
        input_field.send_keys(word)

    def click_on_button(self, locator):
        return self.find_element(locator, time=60).click()

    def click_on_buttons(self, locator):
        for btn in self.find_elements(locator, time=60):
            btn.click()
