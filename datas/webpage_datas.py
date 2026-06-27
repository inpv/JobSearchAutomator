from selenium.webdriver.common.by import By
from dataclasses import dataclass


@dataclass
class HeadHunterLocators:
    LOCATOR_HH_ALLCORRECT_BUTTON = (By.CSS_SELECTOR, "button[data-qa='region-clarification-confirm']")
    LOCATOR_HH_LOGIN_LINK = (By.CSS_SELECTOR, "a[data-qa='login']")
    LOCATOR_HH_WITHEMAIL_FIELD = (By.CSS_SELECTOR, "input[data-qa='credential-type-EMAIL']")
    LOCATOR_HH_BYPASSWORD_BUTTON = (By.CSS_SELECTOR, "button[data-qa='expand-login-by-password']")
    LOCATOR_HH_LOGININPUT_FIELD = (By.CSS_SELECTOR, "input[data-qa='applicant-login-input-email']")
    LOCATOR_HH_PASSWORDINPUT_FIELD = (By.CSS_SELECTOR, "input[data-qa='applicant-login-input-password']")
    LOCATOR_HH_LOGINSUBMIT_BUTTON = (By.CSS_SELECTOR, "button[data-qa='submit-button']")
    LOCATOR_HH_CAPTCHA_FIELD = (By.CSS_SELECTOR, "input[data-qa='account-captcha-input']")
    LOCATOR_HH_CAPTCHA_IMAGE = (By.CSS_SELECTOR, "img[data-qa='account-captcha-picture']")
    LOCATOR_HH_CAPTCHA_SUBMIT_BUTTON = (By.XPATH, "//button[.//span[text()='Отправить']]")
    LOCATOR_HH_EMPLOYER_REVIEW_CLOSE_BUTTON = (By.CSS_SELECTOR, "div[data-qa='notification-close-button']")
    LOCATOR_HH_SERVICE_REVIEW_CLOSE_BUTTON = (By.CLASS_NAME, "uxs-1h3RIxayGx")
    LOCATOR_HH_RESUMEUPDATE_BUTTON = (By.CSS_SELECTOR, "span[data-qa='resume-update-button-text']")
    LOCATOR_HH_RESUMEUPDATE_BUTTONTEXT = "Поднять в поиске"
    LOCATOR_HH_ALLCLEAR_BUTTON = (By.XPATH, "//div[@data-qa='actions-container']//button[.//span[text()='Понятно']]")
