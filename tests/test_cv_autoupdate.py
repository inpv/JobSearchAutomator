from utils.crypt import Crypt
from datas.login_datas import LoginDatas
from datas.webpage_datas import HeadHunterLocators
from datas.connection_datas import ConnectionDatas


class TestCvAutoupdate:

    @staticmethod
    def test_cv_autoupdate(browser, hh_page):
        for page in ConnectionDatas.PAGE_ADDRESSES:
            hh_page.go_to_page(page)

            hh_page.click_on_button(HeadHunterLocators.LOCATOR_HH_ALLCORRECT_BUTTON)
            hh_page.click_on_button(HeadHunterLocators.LOCATOR_HH_LOGIN_LINK)

            hh_page.click_on_button(HeadHunterLocators.LOCATOR_HH_BYPASSWORD_BUTTON)

            hh_page.enter_word_into_input(HeadHunterLocators.LOCATOR_HH_LOGININPUT_FIELD,
                                          LoginDatas.LOGIN_ENCODED_STR)
            hh_page.enter_word_into_input(HeadHunterLocators.LOCATOR_HH_PASSWORDINPUT_FIELD,
                                          str(Crypt.get_random_decrypted_pass()))

            hh_page.click_on_button(HeadHunterLocators.LOCATOR_HH_LOGINSUBMIT_BUTTON)

            hh_page.click_on_button(HeadHunterLocators.LOCATOR_HH_MYRESUMES_LINK)
            hh_page.click_on_buttons(HeadHunterLocators.LOCATOR_HH_RESUMEUPDATE_BUTTON)
