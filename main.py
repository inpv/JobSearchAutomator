from selenium import webdriver
from pages.web_page import SearchHelper
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from datas.login_datas import LoginDatas
from datas.webpage_datas import HeadHunterLocators
from datas.connection_datas import ConnectionDatas


class Main:

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        # chrome_options.add_argument('--disable-notifications') # may help with unwanted popups
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

        try:
            hh_page = SearchHelper(driver)
            for page in ConnectionDatas.PAGE_ADDRESSES:
                    hh_page.go_to_page(page)

                    hh_page.click_on_button(HeadHunterLocators.LOCATOR_HH_ALLCORRECT_BUTTON)

                    hh_page.enter_word_into_input(HeadHunterLocators.LOCATOR_HH_LOGININPUT_FIELD,
                                                  LoginDatas.LOGIN_ENCODED_STR)

                    hh_page.click_on_button(HeadHunterLocators.LOCATOR_HH_BYPASSWORD_BUTTON)

                    hh_page.enter_word_into_input(HeadHunterLocators.LOCATOR_HH_PASSWORDINPUT_FIELD,
                                                  LoginDatas.LOGIN_PWD)
                    hh_page.click_on_button(HeadHunterLocators.LOCATOR_HH_LOGINSUBMIT_BUTTON)

                    hh_page.click_on_elements_if_appeared(HeadHunterLocators.LOCATOR_HH_EMPLOYER_REVIEW_CLOSE_BUTTON)

                    hh_page.click_on_elements_if_appeared(HeadHunterLocators.LOCATOR_HH_SERVICE_REVIEW_CLOSE_BUTTON)

                    hh_page.click_on_buttons_if_text_found(HeadHunterLocators.LOCATOR_HH_RESUMEUPDATE_BUTTON,
                                                           HeadHunterLocators.LOCATOR_HH_RESUMEUPDATE_BUTTONTEXT)
        finally:
            driver.quit()


if __name__ == "__main__":
    Main()
