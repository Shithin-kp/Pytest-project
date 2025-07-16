import time

from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    USERNAME_INPUT = (By.CSS_SELECTOR, "div[class='loginForm loginForm--signIn'] input[placeholder='Username']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "div[class='loginForm loginForm--signIn'] input[placeholder='Password']")
    error_message = (By.CSS_SELECTOR, "h1[class='loginMessage'] p")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    def load(self):
        self.driver.get("https://kefitechlynks.com/")

    def enterUserName(self, username):
        self.find(*self.USERNAME_INPUT).send_keys(username)

    def enterPassword(self, password):
        self.find(*self.PASSWORD_INPUT).send_keys(password)

    def clickLogin(self):
        self.find(*self.LOGIN_BUTTON).click()

    def loginError(self):
        return self.find(*self.error_message).text

    def logIn(self, username, password):
        self.find(*self.USERNAME_INPUT).send_keys(username)
        self.find(*self.PASSWORD_INPUT).send_keys(password)
        time.sleep(15)
        self.find(*self.LOGIN_BUTTON).click()


