from pages.base_page import BasePage
from datas.connection_datas import ConnectionDatas


class SearchHelper(BasePage):

    def enter_word_into_input(self, locator, word):
        input_field = self.find_element(locator, time=ConnectionDatas.MAX_WAIT_VALUE)
        input_field.click()
        input_field.send_keys(word)

    def click_on_button(self, locator):
        return self.find_element(locator, time=ConnectionDatas.MAX_WAIT_VALUE).click()

    def click_on_buttons_if_text_found(self, locator, text: str):
        for btn in self.find_elements(locator, time=ConnectionDatas.MAX_WAIT_VALUE):
            if btn.text == text:
                btn.click()

    def click_on_elements_if_appeared(self, locator):
        elements = self.find_elements_or_ignore(locator, time=ConnectionDatas.MAX_WAIT_VALUE)
        if elements is not None:
            for element in elements:
                element.click()
