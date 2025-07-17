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
    login_page.load()
    login_page.enterUserName("shithin.kokkarni@kefitech.com")
    login_page.enterPassword("DUlKKyKV")
    time.sleep(10)
    login_page.clickLogin()
    time.sleep(3)
    assert "home" in driver.current_url, "Failed to redirect to the home page after login"
    print(home_page.dashboardDisplayed())
    home_page.clickTimesheet()
    timesheet_page.clickaddNewDay()
