import time

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import os

class LoginPage(BasePage):

    # Locators for the login page elements
    USERNAME_INPUT = (By.CSS_SELECTOR, "div[class='loginForm loginForm--signIn'] input[placeholder='Username']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "div[class='loginForm loginForm--signIn'] input[placeholder='Password']")
    error_message = (By.CSS_SELECTOR, "h1[class='loginMessage'] p")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    # Methods to interact with the login page elements
    # Method to enter username
    def enterUserName(self, username):
        self.find(*self.USERNAME_INPUT).send_keys(username)

    # Method to enter password
    def enterPassword(self, password):
        self.find(*self.PASSWORD_INPUT).send_keys(password)

    # Method to click the login button
    def clickLogin(self):
        self.find(*self.LOGIN_BUTTON).click()

    # Method to get the error message displayed on the login page
    def loginError(self):
        return self.find(*self.error_message).text

    # Method to log in with provided username and password
    def logIn(self, username, password):
        self.find(*self.USERNAME_INPUT).send_keys(username)
        self.find(*self.PASSWORD_INPUT).send_keys(password)
        time.sleep(1)
        self.find(*self.LOGIN_BUTTON).click()

    # Method to pause for captcha resolution
    # def pauseForCaptcha(self):
    #     print("\n Please solve the Captcha in the browser.")
    #     input(" Press ENTER here once the captcha is solved...\n")
    #     time.sleep(2)

    def pauseForCaptcha(self):
        if os.getenv("JENKINS_HOME"):  # if running in Jenkins
            print("[SKIP CAPTCHA] Running in Jenkins. Skipping CAPTCHA wait.")
            time.sleep(10)
            return
        input("Solve the CAPTCHA and press Enter to continue...")
