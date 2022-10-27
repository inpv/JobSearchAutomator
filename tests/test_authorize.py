from utils.crypt import Crypt
from datas.login_datas import LoginDatas
from datas.webpage_datas import HeadHunterLocators


class TestAuthorize:

    @staticmethod
    def test_authorize(browser, hh_page):
        hh_page.click_on_button(HeadHunterLocators.LOCATOR_HH_ALLCORRECT_BUTTON)
        hh_page.click_on_button(HeadHunterLocators.LOCATOR_HH_LOGIN_LINK)

        hh_page.click_on_button(HeadHunterLocators.LOCATOR_HH_BYPASSWORD_BUTTON)

        hh_page.enter_word_into_input(HeadHunterLocators.LOCATOR_HH_LOGININPUT_FIELD,
                                      LoginDatas.LOGIN_ENCODED_STR)
        hh_page.enter_word_into_input(HeadHunterLocators.LOCATOR_HH_PASSWORDINPUT_FIELD,
                                      str(Crypt.get_random_decrypted_pass()))

        hh_page.click_on_button(HeadHunterLocators.LOCATOR_HH_LOGINSUBMIT_BUTTON)
