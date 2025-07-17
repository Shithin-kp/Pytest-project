import time

import pytest

from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.timesheet_page import TimesheetPage


@pytest.mark.priority1
def test_add_new_day_button(driver):
    """
    Test description: Verify the presence and functionality of the 'Add New Day' button on the Timesheet page.
    """
    login_page = LoginPage(driver)
    home_page = HomePage(driver)
    timesheet_page = TimesheetPage(driver)
    # login_page.load()
    # Pause to let you solve the CAPTCHA manually
    login_page.pauseForCaptcha()
    login_page.logIn("shithin.kokkarni@kefitech.com", "DUlKKyKV")
    time.sleep(2)
    assert "home" in driver.current_url, "Failed to redirect to the home page after login"
    print(home_page.dashboardDisplayed())
    home_page.clickTimesheet()
    timesheet_page.clickaddNewDay()
