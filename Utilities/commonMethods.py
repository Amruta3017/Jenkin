import os
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime


def get_path(foldername, filename):
    parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    full_path = os.path.join(parent_directory, foldername, filename)
    return full_path


def format_date(given_date):
    try:
        formatted_date = given_date.strftime("%a, %B %#d")
        formatted_time = given_date.strftime("%#I:%M %p GMT")
        return formatted_date, formatted_time
    except Exception as e:
        print(f"{e}")
        return None


class CustomWait:

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator, timeout=20):
        try:
            wait = WebDriverWait(self.driver, timeout, poll_frequency=2)
            return wait.until(EC.presence_of_element_located(locator))
        except Exception as e:
            print(f"{e}")

    def wait_for_elements(self, locator, timeout=15):
        try:
            wait = WebDriverWait(self.driver, timeout, poll_frequency=2)
            return wait.until(EC.presence_of_all_elements_located(locator))
        except Exception as e:
            print(f"{e}")
