from selenium.webdriver.common.by import By
from dataclasses import dataclass


@dataclass
class HeadHunterLocators:
    LOCATOR_HH_ALLCORRECT_BUTTON = (By.CSS_SELECTOR, "button[data-qa='region-clarification-confirm']")
    LOCATOR_HH_LOGIN_LINK = (By.CSS_SELECTOR, "a[data-qa='login']")
    LOCATOR_HH_BYPASSWORD_BUTTON = (By.CSS_SELECTOR, "span[data-qa='expand-login-by-password-text']")
    LOCATOR_HH_LOGININPUT_FIELD = (By.CSS_SELECTOR, "input[data-qa='account-signup-email']")
    LOCATOR_HH_PASSWORDINPUT_FIELD = (By.CSS_SELECTOR, "input[data-qa='login-input-password']")
    LOCATOR_HH_LOGINSUBMIT_BUTTON = (By.CSS_SELECTOR, "button[data-qa='account-login-submit']")
    LOCATOR_HH_CAPTCHA_FIELD = (By.CSS_SELECTOR, "input[data-qa='account-captcha-input']")
    LOCATOR_HH_EMPLOYER_REVIEW_CLOSE_BUTTON = (By.CSS_SELECTOR, "div[data-qa='notification-close-button']")
    LOCATOR_HH_SERVICE_REVIEW_CLOSE_BUTTON = (By.CLASS_NAME, "uxs-1h3RIxayGx")
    LOCATOR_HH_RESUMEUPDATE_BUTTON = (By.CSS_SELECTOR, "button[data-qa='resume-update-button_actions']")
    LOCATOR_HH_RESUMEUPDATE_BUTTONTEXT = "Поднять в поиске"
