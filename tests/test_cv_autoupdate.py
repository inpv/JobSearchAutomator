from datas.webpage_datas import HeadHunterLocators


class TestCvAutoupdate:

    @staticmethod
    def test_cv_autoupdate(browser, hh_page):
        hh_page.click_on_button(HeadHunterLocators.LOCATOR_HH_MYRESUMES_LINK)
        hh_page.click_on_buttons(HeadHunterLocators.LOCATOR_HH_RESUMEUPDATE_BUTTON)
