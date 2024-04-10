from Pages.basepage import BasePage
import time
# import subprocess
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import WebDriverException
import time
import unittest
import pytest
from Config.config import TestData
import json
import imaplib
import email
from email.header import decode_header
import re
import sys

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        # self.base_url_mode = base_url_mode

    

    def login_github(self):
        self.driver.get(TestData.BASE_URL)
        
        time.sleep(7)
        

        # maximosing the window
        self.driver.maximize_window()
        self.wait_and_click("(//p[normalize-space()='Continue with Github'])[1]")
        time.sleep(7)
        
        print("Done successfully")
