from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class AttendancePage(BasePage):
    # Attendance page elements
    entry_tab = (By.XPATH, "//button[normalize-space(text())='Entry']")
    exit_tab = (By.XPATH, "//button[normalize-space(text())='Exit']")
    exit_button=(By.XPATH, "//button[normalize-space(text())='Mark Exit']")

    #Methods

    def attendancePageEntryTabElements(self):
        return self.driver.find_element(*self.entry_tab).is_displayed()

    def attendancePageExitTabElements(self):
        return self.driver.find_element(*self.exit_tab).is_displayed()

    def clickMarkExit(self):
        self.driver.find_element(*self.exit_button).click()