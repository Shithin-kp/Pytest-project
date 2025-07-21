from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class AttendancePage(BasePage):
    # Attendance page elements
    entry_tab = (By.XPATH, "//button[normalize-space(text())='Entry']")
    exit_tab = (By.XPATH, "//button[normalize-space(text())='Exit']")