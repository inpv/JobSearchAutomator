from utils.crypt import Crypt
from pages.web_page import SearchHelper
from datas.login_datas import LoginDatas
from datas.connection_datas import ConnectionDatas
from datas.webpage_datas import HeadHunterLocators


class TestCvAutoupdate:

    hh_page = None

    @staticmethod
    def test_pageload(browser):
        TestCvAutoupdate.hh_page = SearchHelper(browser)
        for page in ConnectionDatas.PAGE_ADDRESSES:
            TestCvAutoupdate.hh_page.go_to_page(page)

    @staticmethod
    def test_authorize(browser):
        TestCvAutoupdate.hh_page.click_on_button(HeadHunterLocators.LOCATOR_HH_ALLCORRECT_BUTTON)
        TestCvAutoupdate.hh_page.click_on_button(HeadHunterLocators.LOCATOR_HH_LOGIN_LINK)

        TestCvAutoupdate.hh_page.click_on_button(HeadHunterLocators.LOCATOR_HH_BYPASSWORD_BUTTON)

        TestCvAutoupdate.hh_page.enter_word_into_input(HeadHunterLocators.LOCATOR_HH_LOGININPUT_FIELD,
                                                       LoginDatas.LOGIN_ENCODED_STR)
        TestCvAutoupdate.hh_page.enter_word_into_input(HeadHunterLocators.LOCATOR_HH_PASSWORDINPUT_FIELD,
                                                       str(Crypt.get_random_decrypted_pass()))

        TestCvAutoupdate.hh_page.click_on_button(HeadHunterLocators.LOCATOR_HH_LOGINSUBMIT_BUTTON)

    @staticmethod
    def test_cv_autoupdate(browser):
        TestCvAutoupdate.hh_page.click_on_button(HeadHunterLocators.LOCATOR_HH_MYRESUMES_LINK)
        TestCvAutoupdate.hh_page.click_on_buttons(HeadHunterLocators.LOCATOR_HH_RESUMEUPDATE_BUTTON)
