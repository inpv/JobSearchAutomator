from selenium.webdriver.common.by import By
from dataclasses import dataclass


@dataclass
class HeadHunterLocators:
    LOCATOR_HH_ALLCORRECT_BUTTON = (By.CSS_SELECTOR, "button[data-qa='region-clarification-confirm']")
    LOCATOR_HH_LOGIN_LINK = (By.CSS_SELECTOR, "a[data-qa='login']")
    LOCATOR_HH_BYPASSWORD_BUTTON = (By.CSS_SELECTOR, "button[data-qa='expand-login-by-password']")
    LOCATOR_HH_LOGININPUT_FIELD = (By.CSS_SELECTOR, "input[data-qa='login-input-username']")
    LOCATOR_HH_PASSWORDINPUT_FIELD = (By.CSS_SELECTOR, "input[data-qa='login-input-password']")
    LOCATOR_HH_LOGINSUBMIT_BUTTON = (By.CSS_SELECTOR, "button[data-qa='account-login-submit']")
    LOCATOR_HH_NOTIFICATIONCLOSE_BUTTON = (By.CSS_SELECTOR, "div[data-qa='notification-close-button']")
    LOCATOR_HH_MYRESUMES_LINK = (By.CLASS_NAME, "supernova-link")
    LOCATOR_HH_RESUMEUPDATE_BUTTON = (By.CSS_SELECTOR, "button[data-qa='resume-update-button_actions']")
