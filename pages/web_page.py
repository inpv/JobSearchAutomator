from pages.base_page import BasePage


class SearchHelper(BasePage):

    def enter_word_into_input(self, locator, word):
        input_field = self.find_element(locator)
        input_field.click()
        input_field.send_keys(word)

    def click_on_button(self, locator):
        return self.find_element(locator, time=60).click()

    def click_on_buttons_if_text_found(self, locator):
        for btn in self.find_elements(locator, time=60):
            if btn.text == "Поднять в поиске":
                btn.click()

    def click_on_element_if_appeared(self, locator):
        element = self.find_element_or_ignore(locator, time=60)
        if element is not None:
            element.click()
