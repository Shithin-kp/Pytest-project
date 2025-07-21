from pages.base_page import BasePage
from selenium.webdriver.common.by import By



class UserToolsPage(BasePage):
    # User tools page elements
    usermanual_button = (By.XPATH, "(//div[@class='MuiCardContent-root css-3sze9j'])[1]")
    holidaycalendar_button = (By.XPATH, "(//div[@class='MuiCardContent-root css-3sze9j'])[2]")
    reimbursement_button = (By.XPATH, "(//div[@class='MuiCardContent-root css-3sze9j'])[3]")
    changepassword_button = (By.XPATH, "(//div[@class='MuiCardContent-root css-3sze9j'])[4]")

    # Methods to interact with the user tools page elements
    def usermanualbuttonDisplayed(self):
        return self.driver.find_element(*self.usermanual_button).is_displayed()

    def holidaycalendarbuttonDisplayed(self):
        return self.driver.find_element(*self.holidaycalendar_button).is_displayed()

    def reimbursementbuttonDisplayed(self):
        return self.driver.find_element(*self.reimbursement_button).is_displayed()

    def changepasswordbuttonDisplayed(self):
        return self.driver.find_element(*self.changepassword_button).is_displayed()

    def clickUserManual(self):
        self.driver.find_element(*self.usermanual_button).click()

    def clickHolidayCalendar(self):
        self.driver.find_element(*self.holidaycalendar_button).click()

    def clickReimbursement(self):
        self.driver.find_element(*self.reimbursement_button).click()

    def clickChangePassword(self):
        self.driver.find_element(*self.changepassword_button).click()

