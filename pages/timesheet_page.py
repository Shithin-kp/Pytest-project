from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class TimesheetPage(BasePage):
    # Timesheet page elements
    save_button = (By.XPATH, "//button[normalize-space(text())='Save']")
    submit_button = (By.XPATH, "//button[normalize-space(text())='Submit Timesheet']")
    addnewday_button = (By.XPATH, "//button[normalize-space(text())='Add New Day']")
    addproject_button = (By.XPATH, "(//div[@class='MuiBox-root css-i3pbo']/following-sibling::button)[3]")
    addtask_button = (By.XPATH, "(//div[@class='MuiBox-root css-1qm1lh']/following-sibling::button)[3]")

    def clickaddNewDay(self):
        self.driver.find_element(*self.addnewday_button).click()