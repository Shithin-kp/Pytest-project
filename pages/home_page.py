import time

from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    timesheet_option = (By.XPATH, "//h2[normalize-space()='Timesheet']")
    attendance_option = (By.XPATH, "//h2[normalize-space()='Attendance']")
    userTools_option = (By.XPATH, "//h2[normalize-space()='User Tools']")
    hamburger_menu = (By.XPATH, "(//div[contains(@class,'MuiToolbar-root MuiToolbar-gutters')]//button)[2]")
    profile_icon = (By.XPATH, "//div[contains(@class,'MuiAvatar-root MuiAvatar-circular')]")
    logout_button = (By.XPATH, "//li[normalize-space(text())='Logout']")
    dashboard_option_in_hamburger_menu = (By.XPATH, "//span[normalize-space(text())='Dashboard']")
    timesheet_option_in_hamburger_menu = (By.XPATH, "//span[normalize-space(text())='Timesheet']")

    def timesheetDisplayed(self):
        return self.driver.find_element(*self.timesheet_option).is_displayed()
    def attendanceDisplayed(self):
        return self.driver.find_element(*self.attendance_option).is_displayed()
    def userToolsDisplayed(self):
        return self.driver.find_element(*self.userTools_option).is_displayed()
    def clickTimesheet(self):
        self.driver.find_element(*self.timesheet_option).click()
        time.sleep(2)
    def clickAttendance(self):
        self.driver.find_element(*self.attendance_option).click()
        time.sleep(2)
    def clickUserTools(self):
        self.driver.find_element(*self.userTools_option).click()
        time.sleep(2)
    def clickHamburgerMenu(self):
        self.driver.find_element(*self.hamburger_menu).click()
        time.sleep(2)
    def clickProfileIcon(self):
        self.driver.find_element(*self.profile_icon).click()
    def clickLogout(self):
        self.driver.find_element(*self.logout_button).click()
        time.sleep(2)
    def dashboardDisplayed(self):
        return self.driver.find_element(*self.dashboard_option_in_hamburger_menu).is_displayed()
    def timesheetDisplayedInHamburgerMenu(self):
        return self.driver.find_element(*self.timesheet_option_in_hamburger_menu).is_displayed()
