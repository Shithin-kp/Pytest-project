import time

import pytest

from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.timesheet_page import TimesheetPage
from conftest import username, password


@pytest.mark.priority1
def test_save_button_blank_fields(driver):
    """
    Test description: Verify that the 'Save' button is disabled when all fields are blank on the Timesheet page.
    """
    login_page = LoginPage(driver)
    home_page = HomePage(driver)
    timesheet_page = TimesheetPage(driver)
    # Pause to let you solve the CAPTCHA manually
    login_page.pauseForCaptcha()
    login_page.logIn(username, password)
    time.sleep(1)
    home_page.clickHamburgerMenu()
    home_page.clickTimesheet()
    assert "time" in driver.current_url, "Failed to navigate to the Timesheet page"
    # Check if the 'Save' button is disabled when all fields are blank
    timesheet_page.clickSaveButton()
    assert "Hours required" in timesheet_page.getHoursErrorText()

@pytest.mark.priority2
def test_submit_button_blank_fields(driver):
    """
    Test description: Verify that the 'Submit' button is disabled when all fields are blank on the Timesheet page.
    """
    login_page = LoginPage(driver)
    home_page = HomePage(driver)
    timesheet_page = TimesheetPage(driver)
    # Pause to let you solve the CAPTCHA manually
    login_page.pauseForCaptcha()
    login_page.logIn(username, password)
    time.sleep(1)
    home_page.clickHamburgerMenu()
    home_page.clickTimesheet()
    assert "time" in driver.current_url, "Failed to navigate to the Timesheet page"
    # Check if the 'Submit' button is disabled when all fields are blank
    timesheet_page.clickSubmitButton()
    assert "Please fill in all required fields before submitting" in timesheet_page.getSubmitErrorText()

@pytest.mark.priorit3
def test_add_new_day_button(driver):
    """
    Test description: Verify the presence and functionality of the 'Add New Day' button on the Timesheet page.
    """
    login_page = LoginPage(driver)
    home_page = HomePage(driver)
    timesheet_page = TimesheetPage(driver)
    # Pause to let you solve the CAPTCHA manually
    login_page.pauseForCaptcha()
    login_page.logIn(username, password)
    time.sleep(1)
    assert "home" in driver.current_url, "Failed to redirect to the home page after login"
    print(home_page.dashboardDisplayed())
    home_page.clickHamburgerMenu()
    home_page.clickTimesheet()
    timesheet_page.clickaddNewDay()

@pytest.mark.priority4
def test_datepicker_functionality(driver):
    """
    Test description: Verify the functionality of the date picker on the Timesheet page.
    """
    login_page = LoginPage(driver)
    home_page = HomePage(driver)
    timesheet_page = TimesheetPage(driver)
    # Pause to let you solve the CAPTCHA manually
    login_page.pauseForCaptcha()
    login_page.logIn(username, password)
    time.sleep(1)
    home_page.clickHamburgerMenu()
    home_page.clickTimesheet()
    assert "time" in driver.current_url, "Failed to navigate to the Timesheet page"
    # Check if the date picker is functional
    time.sleep(1)
    print(timesheet_page.getdate())
    timesheet_page.selectDate(timesheet_page.getdate())
    assert timesheet_page.dateValidationIsDisplayed() is False, "Date validation error message is displayed after selecting a valid date"

@pytest.mark.priority5
def test_selectproject_functionality(driver):
    """
    Test description: Verify the functionality of the 'Select Project' dropdown on the Timesheet page.
    """
    login_page = LoginPage(driver)
    home_page = HomePage(driver)
    timesheet_page = TimesheetPage(driver)
    # Pause to let you solve the CAPTCHA manually
    login_page.pauseForCaptcha()
    login_page.logIn(username, password)
    time.sleep(1)
    home_page.clickHamburgerMenu()
    home_page.clickTimesheet()
    assert "time" in driver.current_url, "Failed to navigate to the Timesheet page"
    # Check if the 'Select Project' dropdown is functional
    timesheet_page.selectProject()

@pytest.mark.priority6
def test_selectactivity_functionality(driver):
    """
    Test description: Verify the functionality of the 'Select Activity' dropdown on the Timesheet page.
    """
    login_page = LoginPage(driver)
    home_page = HomePage(driver)
    timesheet_page = TimesheetPage(driver)
    # Pause to let you solve the CAPTCHA manually
    login_page.pauseForCaptcha()
    login_page.logIn(username, password)
    time.sleep(1)
    home_page.clickHamburgerMenu()
    home_page.clickTimesheet()
    assert "time" in driver.current_url, "Failed to navigate to the Timesheet page"
    # Check if the 'Select Activity' dropdown is functional
    timesheet_page.selectProject()
    timesheet_page.selectActivity()




