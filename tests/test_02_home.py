import time

import pytest

from pages.home_page import HomePage
from pages.login_page import LoginPage
from conftest import username, password


@pytest.mark.priority1
def test_home_page_elements(driver):
    """
               Test description: Verify the presence of key elements on the home page after login.
        """
    login_page = LoginPage(driver)
    home_page = HomePage(driver)
    # Pause to let you solve the CAPTCHA manually
    login_page.pauseForCaptcha()
    login_page.logIn(username, password)
    time.sleep(1)
    assert "home" in driver.current_url, "Failed to redirect to the home page after login"
    print(home_page.dashboardDisplayed())
    assert home_page.dashboardDisplayed() is True, "Dashboard option is not displayed on the home page"
    print(home_page.timesheetDisplayed())
    assert home_page.timesheetDisplayed() is True, "Timesheet option is not displayed on the home page"
    assert home_page.attendanceDisplayed() is True, "Attendance option is not displayed on the home page"
    assert home_page.userToolsDisplayed() is True, "User Tools option is not displayed on the home page"

@pytest.mark.priority2
def test_timsheet_navigation(driver):
    """
               Test description: Verify navigation to the Timesheet page.
    """
    login_page = LoginPage(driver)
    home_page = HomePage(driver)
    # Pause to let you solve the CAPTCHA manually
    login_page.pauseForCaptcha()
    login_page.logIn(username, password)
    time.sleep(1)
    home_page.clickHamburgerMenu()
    home_page.clickTimesheet()
    assert "time" in driver.current_url, "Failed to navigate to the Timesheet page"
@pytest.mark.priority3
def test_attendance_navigation(driver):
    """
               Test description: Verify navigation to the Attendance page.
    """
    login_page = LoginPage(driver)
    home_page = HomePage(driver)
    # Pause to let you solve the CAPTCHA manually
    login_page.pauseForCaptcha()
    login_page.logIn(username, password)
    time.sleep(1)
    home_page.clickAttendance()
    assert "attendance" in driver.current_url, "Failed to navigate to the Attendance page"
@pytest.mark.priority4
def test_user_tools_navigation(driver):
    """
               Test description: Verify navigation to the User Tools page.
    """
    login_page = LoginPage(driver)
    home_page = HomePage(driver)
    # Pause to let you solve the CAPTCHA manually
    login_page.pauseForCaptcha()
    login_page.logIn(username, password)
    time.sleep(1)
    home_page.clickUserTools()
    assert "User-tools" in driver.current_url, "Failed to navigate to the User Tools page"
@pytest.mark.priority5
def test_hamburger_menu(driver):
    """
               Test description: Verify the functionality of the hamburger menu.
    """
    login_page = LoginPage(driver)
    home_page = HomePage(driver)
    # Pause to let you solve the CAPTCHA manually
    login_page.pauseForCaptcha()
    login_page.logIn(username, password)
    time.sleep(1)
    home_page.clickHamburgerMenu()
    home_page.clickHamburgerMenu()
    assert home_page.dashboardDisplayed() is True, "Dashboard option is not displayed in the hamburger menu"
    assert home_page.timesheetDisplayedInHamburgerMenu() is True, "Timesheet option is not displayed in the hamburger menu"

@pytest.mark.priority6
def test_logout(driver):
    """
               Test description: Verify the logout functionality.
    """
    login_page = LoginPage(driver)
    home_page = HomePage(driver)
    # Pause to let you solve the CAPTCHA manually
    login_page.pauseForCaptcha()
    login_page.logIn(username, password)
    time.sleep(1)
    home_page.clickProfileIcon()
    home_page.clickLogout()
    assert "https://kefitechlynks.com/" in driver.current_url, "Failed to log out successfully"
