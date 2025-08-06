from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import time
from selenium.webdriver.support.ui import Select


class TimesheetPage(BasePage):
    # Timesheet page elements
    save_button = (By.XPATH, "(//div[@class='MuiBox-root css-0']//button)[1]")
    submit_button = (By.XPATH, "//button[normalize-space(text())='Submit Timesheet']")
    addnewday_button = (By.XPATH, "//button[normalize-space(text())='Add New Day']")
    addproject_button = (By.XPATH, "(//div[@class='MuiBox-root css-i3pbo']/following-sibling::button)[3]")
    addtask_button = (By.XPATH, "(//div[@class='MuiBox-root css-1qm1lh']/following-sibling::button)[3]")
    hours_error = (By.XPATH, "//p[text()='Hours required']")
    submit_error = (By.XPATH, "//div[@class='MuiAlert-message css-1xsto0d']")
    date_picker = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/span[1]/div[1]/div[1]/div[1]/input[1]")
    date_validation = (By.XPATH, "//div[@class='MuiAlert-message css-1xsto0d']")
    selectproject_dropdown = (By.XPATH, "//div[@class='MuiSelect-select MuiSelect-outlined Mui-error MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputSizeSmall css-1an95j8']")
    activity_dropdown = (By.XPATH, "//div[@class='MuiSelect-select MuiSelect-outlined Mui-error MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputSizeSmall css-1an95j8']")
    # Methods to interact with the timesheet page elements

    # Method to click the 'Add New Day' button
    def clickaddNewDay(self):
        self.driver.find_element(*self.addnewday_button).click()

    def clickSaveButton(self):
        self.driver.find_element(*self.save_button).click()

    def clickSubmitButton(self):
        self.driver.find_element(*self.submit_button).click()

    def getHoursErrorText(self):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.visibility_of_element_located(self.hours_error)).text

    def getSubmitErrorText(self):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.visibility_of_element_located(self.submit_error)).text

    def selectDate(self, date):
        # Locate the input field using your page object's locator
        date_input = self.driver.find_element(*self.date_picker)
        date_input.clear()  # Clear any existing date
        date_input.click()
        date_input.send_keys(date)  # Enter the date in the format dd-mm-yyyy

    def getdate(self):
        return datetime.now().strftime("%d-%m-%Y")  # Or change the format as per your app

    def dateValidationIsDisplayed(self):
        return self.driver.find_element(*self.date_validation).is_displayed()

    def selectProject(self ):
        # Click to open the dropdown
        self.driver.find_element(*self.selectproject_dropdown).click()
        time.sleep(1)  # Optional: Wait for dropdown options to appear

        # Now select the option by visible text
        # Adjust the locator below to match the actual dropdown option structure
        project_option = self.driver.find_element(By.XPATH, f"//li[normalize-space()='Internal Testing']")
        project_option.click()

    def selectActivity(self):
        # Click to open the dropdown
        self.driver.find_element(*self.activity_dropdown).click()
        time.sleep(1)
        # Now select the option by visible text
        # Adjust the locator below to match the actual dropdown option structure
        activity_option = self.driver.find_element(By.XPATH, f"//li[normalize-space()='Internal']")
        activity_option.click()



