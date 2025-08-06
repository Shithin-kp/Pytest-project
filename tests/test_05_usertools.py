import time

import pytest

from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.usertools_page import UserToolsPage
from conftest import username, password

@pytest.mark.priority1
def test_user_tools_page_elements(driver):
    """
    Test description: Verify the presence of key elements on the User Tools page after login.
    """
    login_page = LoginPage(driver)
    home_page = HomePage(driver)
    usertools_page = UserToolsPage(driver)
    # Pause to let you solve the CAPTCHA manually
    login_page.pauseForCaptcha()
    login_page.logIn(username, password)
    time.sleep(2)
    assert "home" in driver.current_url, "Failed to redirect to the home page after login"
    home_page.clickUserTools()
    assert usertools_page.usermanualbuttonDisplayed() is True, "User Manual button is not displayed on the User Tools page"
    assert usertools_page.holidaycalendarbuttonDisplayed() is True, "Holiday Calendar button is not displayed on the User Tools page"
    assert usertools_page.reimbursementbuttonDisplayed() is True, "Reimbursement button is not displayed on the User Tools page"
    assert usertools_page.changepasswordbuttonDisplayed() is True, "Change Password button is not displayed on the User Tools page"

@pytest.mark.priority2
def test_navigation_to_user_tools(driver):
    """
    Test description: Verify navigation to the User Tools page from the home page.
    """
    login_page = LoginPage(driver)
    home_page = HomePage(driver)
    usertools_page = UserToolsPage(driver)
    # Pause to let you solve the CAPTCHA manually
    login_page.pauseForCaptcha()
    login_page.logIn(username, password)
    time.sleep(1)
    assert "home" in driver.current_url, "Failed to redirect to the home page after login"
    home_page.clickUserTools()
    usertools_page.clickUserManual()
    assert "user-manual" in driver.current_url, "Failed to navigate to the User Manual page from the User Tools page"

@pytest.mark.priority3
def test_navigation_to_holiday_calendar(driver):
    """
    Test description: Verify navigation to the Holiday Calendar page from the User Tools page.
    """
    login_page = LoginPage(driver)
    home_page = HomePage(driver)
    usertools_page = UserToolsPage(driver)
    # Pause to let you solve the CAPTCHA manually
    login_page.pauseForCaptcha()
    login_page.logIn(username, password)
    time.sleep(1)
    assert "home" in driver.current_url, "Failed to redirect to the home page after login"
    home_page.clickUserTools()
    usertools_page.clickHolidayCalendar()
    assert "date" in driver.current_url, "Failed to navigate to the Holiday Calendar page from the User Tools page"

@pytest.mark.priority4
def test_navigation_to_reimbursement(driver):
    """
    Test description: Verify navigation to the Reimbursement page from the User Tools page.
    """
    login_page = LoginPage(driver)
    home_page = HomePage(driver)
    usertools_page = UserToolsPage(driver)
    # Pause to let you solve the CAPTCHA manually
    login_page.pauseForCaptcha()
    login_page.logIn(username, password)
    time.sleep(1)
    assert "home" in driver.current_url, "Failed to redirect to the home page after login"
    home_page.clickUserTools()
    usertools_page.clickReimbursement()
    assert "re-form" in driver.current_url, "Failed to navigate to the Reimbursement page from the User Tools page"

@pytest.mark.priority5
def test_navigation_to_change_password(driver):
    """
    Test description: Verify navigation to the Change Password page from the User Tools page.
    """
    login_page = LoginPage(driver)
    home_page = HomePage(driver)
    usertools_page = UserToolsPage(driver)
    # Pause to let you solve the CAPTCHA manually
    login_page.pauseForCaptcha()
    login_page.logIn(username, password)
    time.sleep(1)
    assert "home" in driver.current_url, "Failed to redirect to the home page after login"
    home_page.clickUserTools()
    usertools_page.clickChangePassword()
    assert "c-pass" in driver.current_url, "Failed to navigate to the Change Password page from the User Tools page"

