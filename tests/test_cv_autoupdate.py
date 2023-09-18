import allure
from datas.login_datas import LoginDatas
from datas.webpage_datas import HeadHunterLocators
from datas.connection_datas import ConnectionDatas


@allure.suite('Test CV update')
class TestCvAutoupdate:

    @staticmethod
    @allure.title('Test CV update')
    def test_cv_autoupdate(browser, hh_page):
        for page in ConnectionDatas.PAGE_ADDRESSES:
            with allure.step('Open hh page'):
                hh_page.go_to_page(page)

            with allure.step('Confirm your city'):
                hh_page.click_on_button(HeadHunterLocators.LOCATOR_HH_ALLCORRECT_BUTTON)

            with allure.step('Choose registration by login instead of phone number'):
                hh_page.click_on_button(HeadHunterLocators.LOCATOR_HH_BYPASSWORD_BUTTON)

            with allure.step('Enter login data into login field'):
                hh_page.enter_word_into_input(HeadHunterLocators.LOCATOR_HH_LOGININPUT_FIELD,
                                              LoginDatas.LOGIN_ENCODED_STR)
            with allure.step('Enter passwd data into passwd field'):
                hh_page.enter_word_into_input(HeadHunterLocators.LOCATOR_HH_PASSWORDINPUT_FIELD,
                                              LoginDatas.LOGIN_PWD)
            with allure.step('Submit login and password data'):
                hh_page.click_on_button(HeadHunterLocators.LOCATOR_HH_LOGINSUBMIT_BUTTON)

            with allure.step('Close unwanted employer review popups'):
                hh_page.click_on_elements_if_appeared(HeadHunterLocators.LOCATOR_HH_EMPLOYER_REVIEW_CLOSE_BUTTON)

            with allure.step('Close unwanted service review popups'):
                hh_page.click_on_elements_if_appeared(HeadHunterLocators.LOCATOR_HH_SERVICE_REVIEW_CLOSE_BUTTON)

            with allure.step('Click all update buttons'):
                hh_page.click_on_buttons_if_text_found(HeadHunterLocators.LOCATOR_HH_RESUMEUPDATE_BUTTON,
                                                       HeadHunterLocators.LOCATOR_HH_RESUMEUPDATE_BUTTONTEXT)
