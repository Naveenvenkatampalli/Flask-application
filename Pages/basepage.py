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
import os
import random
import sys
from selenium.common.exceptions import NoSuchElementException

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)

    def button_clicks(self, type, value):
        if type == 1:
            button = self.driver.find_element(By.XPATH, value)
            button.click()
        if type == 2:
            button = self.driver.find_element(By.CLASS_NAME, value)
            button.click()
    def project_selection(self, name):
        user_profile = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//div[@role='alert'])[1]"))
        )
        user_profile.click()
        print("clicked on user profile")

        select_project = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//span[@id='select_project'])[1]"))
        )
        select_project.click()
        print("clicked on select another project")

        project_search = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//input[@id='search-projects-input'])[1]"))
        )
        project_search.send_keys(name)
        print("entered the project name")

        if name != 'demo':
            project_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "(//button[normalize-space()='{}'])[1]".format(name)))
            )
            project_button.click()
            print("clicked on the checked project name")
        else:
            demo_project_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "(//button[normalize-space()='Demo Project'])[1]"))
            )
            demo_project_button.click()
            print("clicked on the demo project name")
        time.sleep(10)

    def actions_pagination(self):
        actions_tab = self.driver.find_element(By.LINK_TEXT, "Actions")
        actions_tab.click()
        time.sleep(3)
        print("clicked on actions tab")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # time.sleep(3)
        print("scrolled the page to bottom")
        operator = self.driver.find_element(By.XPATH, "(//i[@class='dropdown icon'])[2]")
        operator.click()
        time.sleep(3)
        option_locator = "(//span[normalize-space()='5'])[1]"
        option = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, option_locator)))
        option.click()
        
        time.sleep(3)
        print("entered devices per page")
        self.driver.execute_script("window.scrollTo(0, 0);")
        # time.sleep(3)
        print("scrolled the page to top")
        first_page_action_id = self.driver.find_element(By.XPATH,"(//table[@class='ui selectable table sc-kMHJlo jPaBpe'])[1]//tr[1]/td[1]")
        first_page_action_id_text=first_page_action_id.text
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # time.sleep(3)
        print("scrolled the page to bottom")


        


        self.wait_and_click("(//a[normalize-space()='2'])[1]")
        time.sleep(2)
        print("clicked on second page")
        second_page = self.driver.find_element(By.XPATH, "(//a[normalize-space()='2'])[1]")
        icon_class_name = second_page.get_attribute('class')
        if 'active' in icon_class_name:
            print("second page is coming in focus which is correct")
        else:
            print("second page is not coming in focus which is incorrect")
        try:
            self.driver.execute_script("window.scrollTo(0, 0);")
            # time.sleep(3)
            print("scrolled the page to top")
            second_page_action_id = self.driver.find_element(By.XPATH,"(//table[@class='ui selectable table sc-kMHJlo jPaBpe'])[1]//tr[1]/td[1]")
            second_page_action_id_text=second_page_action_id.text
            if int(first_page_action_id_text)>int(second_page_action_id_text):
                print("pagination moved to second page properly which is correct")
            else:
                print("pagination hasn't moved to second page properly which is incorrect")
                
        
        except NoSuchElementException as e:
            print(e)
            print('Not working as expected')
            time.sleep(5)

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # time.sleep(3)
        print("scrolled the page to bottom")
        self.wait_and_click("(//a[contains(text(),'⟩')])[1]")
        time.sleep(2)
        print("clicked on forward_one")
        third_page = self.driver.find_element(By.XPATH, "(//a[normalize-space()='3'])[1]")
        icon_class_name = third_page.get_attribute('class')
        if 'active' in icon_class_name:
            print("forward icon is working successfully")
        else:
            print("forward icon is working")
        try:
            self.driver.execute_script("window.scrollTo(0, 0);")
            # time.sleep(3)
            print("scrolled the page to top")
            third_page_action_id = self.driver.find_element(By.XPATH,"(//table[@class='ui selectable table sc-kMHJlo jPaBpe'])[1]//tr[1]/td[1]")
            third_page_action_id_text=third_page_action_id.text
            if int(second_page_action_id_text)>int(third_page_action_id_text):
                print("pagination moved to third page properly which is correct")
            else:
                print("pagination hasn't moved to third page properly which is incorrect")
                
        
        except NoSuchElementException as e:
            print(e)
            print('Not working as expected')
            time.sleep(5)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # time.sleep(3)
        print("scrolled the page to bottom")
        self.wait_and_click("(//a[normalize-space()='»'])[1]")
        time.sleep(2)
        print("clicked on forward_last")
        # fourth_page = self.driver.find_element(By.XPATH, "(//a[normalize-space()='4'])[1]")
        # icon_class_name = fourth_page.get_attribute('class')
        # if 'active' in icon_class_name:
        #     print("forward to last icon is working successfully")
        # else:
        #     print("forward to last icon is working")
        try:
            self.driver.execute_script("window.scrollTo(0, 0);")
            # time.sleep(3)
            print("scrolled the page to top")
            last_page_action_id = self.driver.find_element(By.XPATH,"(//table[@class='ui selectable table sc-kMHJlo jPaBpe'])[1]//tr[1]/td[1]")
            last_page_action_id_text=last_page_action_id.text
            if int(third_page_action_id_text)>int(last_page_action_id_text):
                print("pagination moved to last page properly which is correct")
            else:
                print("pagination hasn't moved to last page properly which is incorrect")
                
        
        except NoSuchElementException as e:
            print(e)
            print('Not working as expected')
            time.sleep(5)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # time.sleep(3)
        print("scrolled the page to bottom")
        self.wait_and_click("(//a[contains(text(),'⟨')])[1]")
        time.sleep(2)
        print("clicked on backward_one")
        # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # # time.sleep(3)
        # print("scrolled the page to bottom")
        # third_page = self.driver.find_element(By.XPATH, "(//a[normalize-space()='3'])[1]")
        # icon_class_name = third_page.get_attribute('class')
        # if 'active' in icon_class_name:
        #     print("forward to last icon is working successfully")
        # else:
        #     print("forward to last icon is working")
        try:
            self.driver.execute_script("window.scrollTo(0, 0);")
            # time.sleep(3)
            print("scrolled the page to top")
            second_last_page_action_id = self.driver.find_element(By.XPATH,"(//table[@class='ui selectable table sc-kMHJlo jPaBpe'])[1]//tr[1]/td[1]")
            second_last_page_action_id_text=second_last_page_action_id.text
            if int(last_page_action_id_text)<int(second_last_page_action_id_text):
                print("pagination moved to second last page properly which is correct")
            else:
                print("pagination hasn't moved to second last page properly which is incorrect")
                
        
        except NoSuchElementException as e:
            print(e)
            print('Not working as expected')
            time.sleep(5)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # time.sleep(3)
        print("scrolled the page to bottom")
        self.wait_and_click("(//a[normalize-space()='«'])[1]")
        time.sleep(2)
        print("clicked on backward_last")
        first_page = self.driver.find_element(By.XPATH, "(//a[normalize-space()='1'])[1]")
        icon_class_name = first_page.get_attribute('class')
        if 'active' in icon_class_name:
            print("forward to last icon is working successfully")
        else:
            print("forward to last icon is working")
        try:
            self.driver.execute_script("window.scrollTo(0, 0);")
            # time.sleep(3)
            print("scrolled the page to top")
            again_first_page_action_id = self.driver.find_element(By.XPATH,"(//table[@class='ui selectable table sc-kMHJlo jPaBpe'])[1]//tr[1]/td[1]")
            again_first_page_action_id_text=again_first_page_action_id.text
            if int(first_page_action_id_text)==int(again_first_page_action_id_text):
                print("pagination moved to first page properly which is correct")
            else:
                print("pagination hasn't moved to first page properly which is incorrect")
                
        
        except NoSuchElementException as e:
            print(e)
            print('Not working as expected')
            time.sleep(5)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # time.sleep(3)
        print("scrolled the page to bottom")
        jump_to = self.driver.find_element(By.XPATH, "(//input[@placeholder='Jump to page...'])[1]")
        jump_to.send_keys("3")
        # time.sleep()
        jump_to.send_keys(Keys.RETURN)
        time.sleep(2)
        print("clicked on jump to")
        third_page = self.driver.find_element(By.XPATH, "(//a[normalize-space()='3'])[1]")
        icon_class_name = third_page.get_attribute('class')
        if 'active' in icon_class_name:
            print("forward to last icon is working successfully")
        else:
            print("forward to last icon is working")
        try:
            self.driver.execute_script("window.scrollTo(0, 0);")
            # time.sleep(3)
            print("scrolled the page to top")
            again_third_page_action_id = self.driver.find_element(By.XPATH,"(//table[@class='ui selectable table sc-kMHJlo jPaBpe'])[1]//tr[1]/td[1]")
            again_third_page_action_id_text=again_third_page_action_id.text
            if int(third_page_action_id_text)==int(again_third_page_action_id_text):
                print("pagination moved to third page properly which is correct")
            else:
                print("pagination hasn't moved to third page properly which is incorrect")
                
        
        except NoSuchElementException as e:
            print(e)
            print('Not working as expected')
            time.sleep(5)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # time.sleep(3)
        print("scrolled the page to bottom")
        
        # self.driver.execute_script("arguments[0].value = '';", jump_to)
        jump_to = self.driver.find_element(By.XPATH, "(//input[@placeholder='Jump to page...'])[1]")
        # time.sleep(3)
        jump_to.send_keys("234567")
        # time.sleep(3)
        jump_to.send_keys(Keys.RETURN)
        time.sleep(3)
        # fourth_page = self.driver.find_element(By.XPATH, "(//a[normalize-space()='4'])[1]")
        # icon_class_name = fourth_page.get_attribute('class')
        # if 'active' in icon_class_name:
        #     print("forward to last icon is working successfully")
        # else:
        #     print("forward to last icon is working")
        try:
            self.driver.execute_script("window.scrollTo(0, 0);")
            # time.sleep(3)
            print("scrolled the page to top")
            again_last_page_action_id = self.driver.find_element(By.XPATH,"(//table[@class='ui selectable table sc-kMHJlo jPaBpe'])[1]//tr[1]/td[1]")
            again_last_page_action_id_text=again_last_page_action_id.text
            if int(again_last_page_action_id_text)==int(last_page_action_id_text):
                print("pagination moved to last page properly which is correct")
            else:
                print("pagination hasn't moved to last page properly which is incorrect")
                
        
        except NoSuchElementException as e:
            print(e)
            print('Not working as expected')
            time.sleep(5)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # time.sleep(3)
        print("scrolled the page to bottom")
        
        # self.driver.execute_script("arguments[0].value = '';", jump_to)
        jump_to = self.driver.find_element(By.XPATH, "(//input[@placeholder='Jump to page...'])[1]")
        # time.sleep(3)
        jump_to.send_keys("0")
        # time.sleep(3)
        jump_to.send_keys(Keys.RETURN)
        time.sleep(3)
        first_page = self.driver.find_element(By.XPATH, "(//a[normalize-space()='1'])[1]")
        icon_class_name = first_page.get_attribute('class')
        if 'active' in icon_class_name:
            print("forward to last icon is working successfully")
        else:
            print("forward to last icon is working")
        try:
            self.driver.execute_script("window.scrollTo(0, 0);")
            # time.sleep(3)
            print("scrolled the page to top")
            again_again_first_page_action_id = self.driver.find_element(By.XPATH,"(//table[@class='ui selectable table sc-kMHJlo jPaBpe'])[1]//tr[1]/td[1]")
            again_again_first_page_action_id_text=again_again_first_page_action_id.text
            if int(again_again_first_page_action_id_text)==int(again_first_page_action_id_text):
                print("pagination moved to first page properly which is correct")
            else:
                print("pagination hasn't moved to first page properly which is incorrect")
                
        
        except NoSuchElementException as e:
            print(e)
            print('Not working as expected')
            time.sleep(5)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # time.sleep(3)
        print("scrolled the page to bottom")
        
        # self.driver.execute_script("arguments[0].value = '';", jump_to)
        jump_to = self.driver.find_element(By.XPATH, "(//input[@placeholder='Jump to page...'])[1]")
        # time.sleep(3)
        jump_to.send_keys("-1")
        # time.sleep(3)
        jump_to.send_keys(Keys.RETURN)
        time.sleep(2)
        toast_message = self.driver.find_element(By.XPATH, "(//div[@role='status'])[1]")
        print(toast_message.text)
        # time.sleep(5)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # time.sleep(3)
        print("scrolled the page to bottom")
        self.wait_and_click("(//a[normalize-space()='»'])[1]")
        time.sleep(2)
        print("clicked on forward_last")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # time.sleep(3)
        print("scrolled the page to bottom")
        operator = self.driver.find_element(By.XPATH, "(//i[@class='dropdown icon'])[2]")
        operator.click()
        time.sleep(3)
        option_locator = "(//span[normalize-space()='10'])[1]"
        option = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, option_locator)))
        option.click()
        
        time.sleep(3)
        print("entered devices per page")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # time.sleep(3)
        print("scrolled the page to bottom")
        first_page = self.driver.find_element(By.XPATH, "(//a[normalize-space()='1'])[1]")
        icon_class_name = first_page.get_attribute('class')
        if 'active' in icon_class_name:
            print("forward to last icon is working successfully")
        else:
            print("forward to last icon is working")
        self.wait_and_click("(//a[normalize-space()='»'])[1]")
        time.sleep(2)
        print("clicked on forward_last")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # time.sleep(3)
        print("scrolled the page to bottom")
        operator = self.driver.find_element(By.XPATH, "(//i[@class='dropdown icon'])[2]")
        operator.click()
        time.sleep(3)
        option_locator = "(//span[normalize-space()='25'])[1]"
        option = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, option_locator)))
        option.click()
        
        time.sleep(3)
        print("entered devices per page")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # time.sleep(3)
        print("scrolled the page to bottom")
        first_page = self.driver.find_element(By.XPATH, "(//a[normalize-space()='1'])[1]")
        icon_class_name = first_page.get_attribute('class')
        if 'active' in icon_class_name:
            print("forward to last icon is working successfully")
        else:
            print("forward to last icon is working")
        self.wait_and_click("(//a[normalize-space()='»'])[1]")
        time.sleep(2)
        print("clicked on forward_last")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # time.sleep(3)
        print("scrolled the page to bottom")
        operator = self.driver.find_element(By.XPATH, "(//i[@class='dropdown icon'])[2]")
        operator.click()
        time.sleep(3)
        option_locator = "(//span[normalize-space()='50'])[1]"
        option = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, option_locator)))
        option.click()
        
        time.sleep(3)
        print("entered devices per page")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # time.sleep(3)
        print("scrolled the page to bottom")
        first_page = self.driver.find_element(By.XPATH, "(//a[normalize-space()='1'])[1]")
        icon_class_name = first_page.get_attribute('class')
        if 'active' in icon_class_name:
            print("forward to last icon is working successfully")
        else:
            print("forward to last icon is working")
        self.driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(3)
        print("scrolled the page to top")


    def devices_dashboards_pagination(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # time.sleep(3)
        print("scrolled the page to bottom")
        operator = self.driver.find_element(By.XPATH, "(//i[@class='dropdown icon'])[3]")
        operator.click()
        time.sleep(3)
        option_locator = "(//span[normalize-space()='5'])[1]"
        option = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, option_locator)))
        option.click()
        
        time.sleep(3)
        print("entered devices per page")
        self.driver.execute_script("window.scrollTo(0, 0);")
        # time.sleep(3)
        print("scrolled the page to top")
        first_page_action_id = self.driver.find_element(By.XPATH,"(//table[@class='ui selectable table sc-kMHJlo jPaBpe'])[1]//tr[1]/td[1]")
        first_page_action_id_text=first_page_action_id.text
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # time.sleep(3)
        print("scrolled the page to bottom")


        


        self.wait_and_click("(//a[normalize-space()='2'])[1]")
        time.sleep(2)
        print("clicked on second page")
        second_page = self.driver.find_element(By.XPATH, "(//a[normalize-space()='2'])[1]")
        icon_class_name = second_page.get_attribute('class')
        if 'active' in icon_class_name:
            print("second page is coming in focus which is correct")
        else:
            print("second page is not coming in focus which is incorrect")
        try:
            self.driver.execute_script("window.scrollTo(0, 0);")
            # time.sleep(3)
            print("scrolled the page to top")
            second_page_action_id = self.driver.find_element(By.XPATH,"(//table[@class='ui selectable table sc-kMHJlo jPaBpe'])[1]//tr[1]/td[1]")
            second_page_action_id_text=second_page_action_id.text
            if int(first_page_action_id_text)>int(second_page_action_id_text):
                print("pagination moved to second page properly which is correct")
            else:
                print("pagination hasn't moved to second page properly which is incorrect")
                
        
        except NoSuchElementException as e:
            print(e)
            print('Not working as expected')
            time.sleep(5)

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # time.sleep(3)
        print("scrolled the page to bottom")
        self.wait_and_click("(//a[contains(text(),'⟩')])[1]")
        time.sleep(2)
        print("clicked on forward_one")
        third_page = self.driver.find_element(By.XPATH, "(//a[normalize-space()='3'])[1]")
        icon_class_name = third_page.get_attribute('class')
        if 'active' in icon_class_name:
            print("forward icon is working successfully")
        else:
            print("forward icon is working")
        try:
            self.driver.execute_script("window.scrollTo(0, 0);")
            # time.sleep(3)
            print("scrolled the page to top")
            third_page_action_id = self.driver.find_element(By.XPATH,"(//table[@class='ui selectable table sc-kMHJlo jPaBpe'])[1]//tr[1]/td[1]")
            third_page_action_id_text=third_page_action_id.text
            if int(second_page_action_id_text)>int(third_page_action_id_text):
                print("pagination moved to third page properly which is correct")
            else:
                print("pagination hasn't moved to third page properly which is incorrect")
                
        
        except NoSuchElementException as e:
            print(e)
            print('Not working as expected')
            time.sleep(5)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # time.sleep(3)
        print("scrolled the page to bottom")
        self.wait_and_click("(//a[normalize-space()='»'])[1]")
        time.sleep(2)
        print("clicked on forward_last")
        # fourth_page = self.driver.find_element(By.XPATH, "(//a[normalize-space()='4'])[1]")
        # icon_class_name = fourth_page.get_attribute('class')
        # if 'active' in icon_class_name:
        #     print("forward to last icon is working successfully")
        # else:
        #     print("forward to last icon is working")
        try:
            self.driver.execute_script("window.scrollTo(0, 0);")
            # time.sleep(3)
            print("scrolled the page to top")
            last_page_action_id = self.driver.find_element(By.XPATH,"(//table[@class='ui selectable table sc-kMHJlo jPaBpe'])[1]//tr[1]/td[1]")
            last_page_action_id_text=last_page_action_id.text
            if int(third_page_action_id_text)>int(last_page_action_id_text):
                print("pagination moved to last page properly which is correct")
            else:
                print("pagination hasn't moved to last page properly which is incorrect")
                
        
        except NoSuchElementException as e:
            print(e)
            print('Not working as expected')
            time.sleep(5)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # time.sleep(3)
        print("scrolled the page to bottom")
        self.wait_and_click("(//a[contains(text(),'⟨')])[1]")
        time.sleep(2)
        print("clicked on backward_one")
        # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # # time.sleep(3)
        # print("scrolled the page to bottom")
        # third_page = self.driver.find_element(By.XPATH, "(//a[normalize-space()='3'])[1]")
        # icon_class_name = third_page.get_attribute('class')
        # if 'active' in icon_class_name:
        #     print("forward to last icon is working successfully")
        # else:
        #     print("forward to last icon is working")
        try:
            self.driver.execute_script("window.scrollTo(0, 0);")
            # time.sleep(3)
            print("scrolled the page to top")
            second_last_page_action_id = self.driver.find_element(By.XPATH,"(//table[@class='ui selectable table sc-kMHJlo jPaBpe'])[1]//tr[1]/td[1]")
            second_last_page_action_id_text=second_last_page_action_id.text
            if int(last_page_action_id_text)<int(second_last_page_action_id_text):
                print("pagination moved to second last page properly which is correct")
            else:
                print("pagination hasn't moved to second last page properly which is incorrect")
                
        
        except NoSuchElementException as e:
            print(e)
            print('Not working as expected')
            time.sleep(5)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # time.sleep(3)
        print("scrolled the page to bottom")
        self.wait_and_click("(//a[normalize-space()='«'])[1]")
        time.sleep(2)
        print("clicked on backward_last")
        first_page = self.driver.find_element(By.XPATH, "(//a[normalize-space()='1'])[1]")
        icon_class_name = first_page.get_attribute('class')
        if 'active' in icon_class_name:
            print("forward to last icon is working successfully")
        else:
            print("forward to last icon is working")
        try:
            self.driver.execute_script("window.scrollTo(0, 0);")
            # time.sleep(3)
            print("scrolled the page to top")
            again_first_page_action_id = self.driver.find_element(By.XPATH,"(//table[@class='ui selectable table sc-kMHJlo jPaBpe'])[1]//tr[1]/td[1]")
            again_first_page_action_id_text=again_first_page_action_id.text
            if int(first_page_action_id_text)==int(again_first_page_action_id_text):
                print("pagination moved to first page properly which is correct")
            else:
                print("pagination hasn't moved to first page properly which is incorrect")
                
        
        except NoSuchElementException as e:
            print(e)
            print('Not working as expected')
            time.sleep(5)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # time.sleep(3)
        print("scrolled the page to bottom")
        jump_to = self.driver.find_element(By.XPATH, "(//input[@placeholder='Jump to page...'])[1]")
        jump_to.send_keys("3")
        # time.sleep()
        jump_to.send_keys(Keys.RETURN)
        time.sleep(2)
        print("clicked on jump to")
        third_page = self.driver.find_element(By.XPATH, "(//a[normalize-space()='3'])[1]")
        icon_class_name = third_page.get_attribute('class')
        if 'active' in icon_class_name:
            print("forward to last icon is working successfully")
        else:
            print("forward to last icon is working")
        try:
            self.driver.execute_script("window.scrollTo(0, 0);")
            # time.sleep(3)
            print("scrolled the page to top")
            again_third_page_action_id = self.driver.find_element(By.XPATH,"(//table[@class='ui selectable table sc-kMHJlo jPaBpe'])[1]//tr[1]/td[1]")
            again_third_page_action_id_text=again_third_page_action_id.text
            if int(third_page_action_id_text)==int(again_third_page_action_id_text):
                print("pagination moved to third page properly which is correct")
            else:
                print("pagination hasn't moved to third page properly which is incorrect")
                
        
        except NoSuchElementException as e:
            print(e)
            print('Not working as expected')
            time.sleep(5)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # time.sleep(3)
        print("scrolled the page to bottom")
        
        # self.driver.execute_script("arguments[0].value = '';", jump_to)
        jump_to = self.driver.find_element(By.XPATH, "(//input[@placeholder='Jump to page...'])[1]")
        # time.sleep(3)
        jump_to.send_keys("234567")
        # time.sleep(3)
        jump_to.send_keys(Keys.RETURN)
        time.sleep(3)
        # fourth_page = self.driver.find_element(By.XPATH, "(//a[normalize-space()='4'])[1]")
        # icon_class_name = fourth_page.get_attribute('class')
        # if 'active' in icon_class_name:
        #     print("forward to last icon is working successfully")
        # else:
        #     print("forward to last icon is working")
        try:
            self.driver.execute_script("window.scrollTo(0, 0);")
            # time.sleep(3)
            print("scrolled the page to top")
            again_last_page_action_id = self.driver.find_element(By.XPATH,"(//table[@class='ui selectable table sc-kMHJlo jPaBpe'])[1]//tr[1]/td[1]")
            again_last_page_action_id_text=again_last_page_action_id.text
            if int(again_last_page_action_id_text)==int(last_page_action_id_text):
                print("pagination moved to last page properly which is correct")
            else:
                print("pagination hasn't moved to last page properly which is incorrect")
                
        
        except NoSuchElementException as e:
            print(e)
            print('Not working as expected')
            time.sleep(5)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # time.sleep(3)
        print("scrolled the page to bottom")
        
        # self.driver.execute_script("arguments[0].value = '';", jump_to)
        jump_to = self.driver.find_element(By.XPATH, "(//input[@placeholder='Jump to page...'])[1]")
        # time.sleep(3)
        jump_to.send_keys("0")
        # time.sleep(3)
        jump_to.send_keys(Keys.RETURN)
        time.sleep(3)
        first_page = self.driver.find_element(By.XPATH, "(//a[normalize-space()='1'])[1]")
        icon_class_name = first_page.get_attribute('class')
        if 'active' in icon_class_name:
            print("forward to last icon is working successfully")
        else:
            print("forward to last icon is working")
        try:
            self.driver.execute_script("window.scrollTo(0, 0);")
            # time.sleep(3)
            print("scrolled the page to top")
            again_again_first_page_action_id = self.driver.find_element(By.XPATH,"(//table[@class='ui selectable table sc-kMHJlo jPaBpe'])[1]//tr[1]/td[1]")
            again_again_first_page_action_id_text=again_again_first_page_action_id.text
            if int(again_again_first_page_action_id_text)==int(again_first_page_action_id_text):
                print("pagination moved to first page properly which is correct")
            else:
                print("pagination hasn't moved to first page properly which is incorrect")
                
        
        except NoSuchElementException as e:
            print(e)
            print('Not working as expected')
            time.sleep(5)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # time.sleep(3)
        print("scrolled the page to bottom")
        
        # self.driver.execute_script("arguments[0].value = '';", jump_to)
        jump_to = self.driver.find_element(By.XPATH, "(//input[@placeholder='Jump to page...'])[1]")
        # time.sleep(3)
        jump_to.send_keys("-1")
        # time.sleep(3)
        jump_to.send_keys(Keys.RETURN)
        time.sleep(2)
        toast_message = self.driver.find_element(By.XPATH, "(//div[@role='status'])[1]")
        print(toast_message.text)
        # time.sleep(5)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # time.sleep(3)
        print("scrolled the page to bottom")
        self.wait_and_click("(//a[normalize-space()='»'])[1]")
        time.sleep(2)
        print("clicked on forward_last")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # time.sleep(3)
        print("scrolled the page to bottom")
        operator = self.driver.find_element(By.XPATH, "(//i[@class='dropdown icon'])[2]")
        operator.click()
        time.sleep(3)
        option_locator = "(//span[normalize-space()='10'])[1]"
        option = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, option_locator)))
        option.click()
        
        time.sleep(3)
        print("entered devices per page")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # time.sleep(3)
        print("scrolled the page to bottom")
        first_page = self.driver.find_element(By.XPATH, "(//a[normalize-space()='1'])[1]")
        icon_class_name = first_page.get_attribute('class')
        if 'active' in icon_class_name:
            print("forward to last icon is working successfully")
        else:
            print("forward to last icon is working")
        self.wait_and_click("(//a[normalize-space()='»'])[1]")
        time.sleep(2)
        print("clicked on forward_last")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # time.sleep(3)
        print("scrolled the page to bottom")
        operator = self.driver.find_element(By.XPATH, "(//i[@class='dropdown icon'])[2]")
        operator.click()
        time.sleep(3)
        option_locator = "(//span[normalize-space()='25'])[1]"
        option = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, option_locator)))
        option.click()
        
        time.sleep(3)
        print("entered devices per page")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # time.sleep(3)
        print("scrolled the page to bottom")
        first_page = self.driver.find_element(By.XPATH, "(//a[normalize-space()='1'])[1]")
        icon_class_name = first_page.get_attribute('class')
        if 'active' in icon_class_name:
            print("forward to last icon is working successfully")
        else:
            print("forward to last icon is working")
        self.wait_and_click("(//a[normalize-space()='»'])[1]")
        time.sleep(2)
        print("clicked on forward_last")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # time.sleep(3)
        print("scrolled the page to bottom")
        operator = self.driver.find_element(By.XPATH, "(//i[@class='dropdown icon'])[2]")
        operator.click()
        time.sleep(3)
        option_locator = "(//span[normalize-space()='50'])[1]"
        option = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, option_locator)))
        option.click()
        
        time.sleep(3)
        print("entered devices per page")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # time.sleep(3)
        print("scrolled the page to bottom")
        first_page = self.driver.find_element(By.XPATH, "(//a[normalize-space()='1'])[1]")
        icon_class_name = first_page.get_attribute('class')
        if 'active' in icon_class_name:
            print("forward to last icon is working successfully")
        else:
            print("forward to last icon is working")
        self.driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(3)
        print("scrolled the page to top")
        

    def create_device_dashboard(self, name):
        dash_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Dashboards"))
        )
        dash_button.click()
        print("clicked on dashboards tab")

        create_dash = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//button[normalize-space()='Create Dashboard'])[1]"))
        )
        create_dash.click()
        print("clicked on create dashboard button")

        title = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Title']"))
        )
        title.send_keys(name)
        print("entered title")

        submit_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//button[normalize-space()='Submit'])[1]"))
        )
        submit_button.click()
        print("clicked on submit button")

        select_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//button[contains(text(),'Select')])[1]"))
        )
        select_button.click()
        print("clicked on select button")
        time.sleep(3)

    def create_fleet_dashboard(self, name):
        dash_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Dashboards"))
        )
        dash_button.click()
        print("clicked on dashboards tab")

        create_dash = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//button[normalize-space()='Create Dashboard'])[1]"))
        )
        create_dash.click()
        print("clicked on create dashboard button")

        title = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//input[@type='text'])[1]"))
        )
        title.send_keys(name)
        title.send_keys(Keys.RETURN)
        print("entered title")

        submit_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//button[normalize-space()='Submit'])[1]"))
        )
        submit_button.click()
        print("clicked on submit button")
        time.sleep(3)

    def click_settings_sections(self,name):
        user_profile = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "(//div[@role='alert'])[1]"))
        )
        user_profile.click()
        print("clicked on user profile")

        settings_tab = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//span[normalize-space()='Settings'])[1]"))
        )
        settings_tab.click()
        print("clicked on settings tab")

        self.driver.execute_script("window.scrollTo(0, 0);")
        print("scrolled the page to top")

        streams_tab = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='{}']".format(name)))
        )
        streams_tab.click()
        print("clicked on streams tab")
        time.sleep(2)
    
    def wait_and_click(self, xpath):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        element.click()

    def action_type_specific(self,action_type,phased):
        self.driver.execute_script("window.scrollTo(0, 0);")
        # time.sleep(3)
        print("scrolled the page to top")
        if action_type=='update_firmware':
            if phased=='phased':
                self.wait_and_click("(//div[normalize-space()='Select Version'])[1]")
                print("clicked on version dropdown")
                self.wait_and_click("(//span[normalize-space()='new62'])[1]")
                # time.sleep(2)
                print("selected the brand as firmware")
            else:
                self.wait_and_click("(//button[normalize-space()='Click here to Upload'])[1]")
                print("clicked on dropdown")
                self.wait_and_click("(//button[normalize-space()='Submit'])[1]")
                time.sleep(2)
                print('clicked on submit button')
                name_validation = self.driver.find_element(By.XPATH, "(//div[@id='version_input-error-message'])[1]")
                print(name_validation.text)
                # time.sleep(5)
                self.wait_and_send_keys("(//input[@id='version_input'])[1]",'new62')
                name_field = self.driver.find_element(By.XPATH, "(//input[@id='version_input'])[1]")
                print("entered duplicated name")
                self.wait_and_click("(//button[normalize-space()='Submit'])[1]")
                time.sleep(2)
                name_validation = self.driver.find_element(By.XPATH, "(//div[@id='version_input-error-message'])[1]")
                print(name_validation.text)
                # time.sleep(5)
                # toast_message = self.driver.find_element(By.XPATH, "(//div[@class='toast toast-error'])[1]")
                # print(toast_message.text)
                # time.sleep(5)
                name_field = self.driver.find_element(By.XPATH, "(//input[@id='version_input'])[1]")

                self.driver.execute_script("arguments[0].value = '';", name_field)
                # time.sleep(3)
                name = "new{}".format(random.randint(10000,100000))
                self.wait_and_send_keys("(//input[@id='version_input'])[1]",name)
                print("entered name")
                self.wait_and_click("(//button[normalize-space()='Submit'])[1]")
                time.sleep(2)
                toast_message = self.driver.find_element(By.XPATH, "(//div[@role='status'])[1]")
                print(toast_message.text)
                # time.sleep(5)
                file_name = 'hello.png'
                file_path = os.path.abspath(os.path.join('Config', file_name))
                print(file_path)
                upload_button = self.driver.find_element(By.XPATH, "(//input[@id='upload_file'])[1]")
                upload_button.send_keys(file_path)
                time.sleep(2)
                print("entered the file")
                self.wait_and_click("(//button[normalize-space()='Submit'])[1]")
                time.sleep(7)
                print('clicked on submit button')

        elif action_type=='update_config':
            if phased=='phased':
                self.wait_and_click("(//div[normalize-space()='Select Version'])[1]")
                print("clicked on version dropdown")
                self.wait_and_click("(//span[normalize-space()='BRAND'])[1]")
                # time.sleep(2)
                print("selected the brand as config")
            else:
                self.wait_and_click("(//button[normalize-space()='Click here to Upload'])[1]")
                print("clicked on dropdown")
                self.wait_and_click("(//button[normalize-space()='Create'])[1]")
                time.sleep(2)
                print('clicked on create button')
                name_validation = self.driver.find_element(By.XPATH, "(//div[@id='version_name-error-message'])[1]")
                print(name_validation.text)
                # time.sleep(5)
                
                self.wait_and_send_keys("(//input[@id='version_name'])[1]","good")
                print("entered duplicated name")
                self.wait_and_click("(//button[normalize-space()='Create'])[1]")
                time.sleep(2)
                # toast_message = self.driver.find_element(By.XPATH, "(//div[@class='toast toast-error'])[1]")
                # print(toast_message.text)
                # time.sleep(5)
                
                json_field = self.driver.find_element(By.XPATH, "(//textarea[@role='textbox'])[1]")
                # Create an ActionChains object
                actions = ActionChains(self.driver)

                # Double-click on the text field
                actions.double_click(json_field).perform()
                # time.sleep(5)
                print("double clicked on the json field")
                text_to_copy = '{"test": true}'
                # pyperclip.copy(text_to_copy)
                # print('Entered  embed')
                # json_field.send_keys(Keys.COMMAND, 'v')
                # json_field.send_keys('hello')
                self.driver.execute_script("arguments[0].value = '';", json_field)

                # Set the new value
                self.driver.execute_script("arguments[0].value = arguments[1];", json_field, text_to_copy)
                
                # Trigger input event
                self.driver.execute_script("arguments[0].dispatchEvent(new Event('input', { bubbles: true }));", json_field)
                
                # Trigger change event
                self.driver.execute_script("arguments[0].dispatchEvent(new Event('change', { bubbles: true }));", json_field)
                # time.sleep(5)
                print("entered json")
                self.wait_and_click("(//button[normalize-space()='Create'])[1]")
                time.sleep(2)
                print('clicked on create button')
                name_field = self.driver.find_element(By.XPATH, "(//input[@id='version_name'])[1]")
                name_validation = self.driver.find_element(By.XPATH, "(//div[@id='version_name-error-message'])[1]")
                print(name_validation.text)
                # time.sleep(5)
                # name_field.send_keys(Keys.COMMAND, 'A')
                self.driver.execute_script("arguments[0].value = '';", name_field)
                time.sleep(3)
                name = "new{}".format(random.randint(10000,100000))
                self.wait_and_send_keys("(//input[@id='version_name'])[1]",name)
                print("entered name")
                self.wait_and_click("(//button[normalize-space()='Create'])[1]")
                time.sleep(4)
                print('clicked on create button')

        elif action_type=='send_file':
            self.wait_and_click("(//button[normalize-space()='Click here to Upload'])[1]")
            print("clicked on dropdown")
            
            upload = self.driver.find_element(By.XPATH, "(//button[normalize-space()='Done'])[1]")
            class_name=upload.get_attribute("class")
            if 'disabled' in class_name:
                print("submit button is disabled")
            else:
                print("submit button is enabled which is incorrect")
            file_name = 'hello.png'
            file_path = os.path.abspath(os.path.join('Config', file_name))
            print(file_path)
            upload_button = self.driver.find_element(By.XPATH, "(//input[@id='file'])[1]")
            upload_button.send_keys(file_path)
            # time.sleep(3)
            print("entered the file")
            self.wait_and_click("(//button[normalize-space()='Done'])[1]")
            time.sleep(2)
            print('clicked on done button')
        elif action_type=='text_payload':
            self.wait_and_click("(//button[normalize-space()='Click here to Upload'])[1]")
            print("clicked on dropdown")
            self.wait_and_click("(//button[normalize-space()='Yes'])[1]")
            time.sleep(2)
            print('clicked on yes button')
            toast_message = self.driver.find_element(By.XPATH, "(//div[@role='status'])[1]")
            print(toast_message.text)
            # time.sleep(2)

            json_field = self.driver.find_element(By.XPATH, "(//textarea[@placeholder='Text payload'])[1]")
            # Create an ActionChains object
            actions = ActionChains(self.driver)

            # Double-click on the text field
            actions.double_click(json_field).perform()
            # time.sleep(2)
            print("double clicked on the text field")
            text_to_copy = 'this is a text payload'
            json_field.send_keys(text_to_copy)
            # time.sleep(2)
            print("entered text")
            self.wait_and_click("(//button[normalize-space()='Yes'])[1]")
            print('clicked on yes button')
            time.sleep(2)
            self.wait_and_click("(//button[normalize-space()='Click here to View/Edit'])[1]")
            print("clicked on edit button")
            json_field = self.driver.find_element(By.XPATH, "(//textarea[@placeholder='Text payload'])[1]")
            # Create an ActionChains object
            actions = ActionChains(self.driver)

            # Double-click on the text field
            actions.double_click(json_field).perform()
            # time.sleep(2)
            print("double clicked on the text field")
            text_to_copy = 'this is a text payload again to check'
            json_field.send_keys(text_to_copy)
            # time.sleep(2)
            print("entered text")
            self.wait_and_click("(//button[normalize-space()='Yes'])[1]")
            time.sleep(2)
            print('clicked on yes button')
        elif action_type=='direct_config':
            self.wait_and_click("(//button[normalize-space()='Click here to Upload'])[1]")
            print("clicked on dropdown")
            self.wait_and_click("(//button[normalize-space()='Yes'])[1]")
            time.sleep(1)
            print('clicked on create button')
            toast_message = self.driver.find_element(By.XPATH, "(//div[@role='status'])[1]")
            print(toast_message.text)
            # time.sleep(2)
            
            
            json_field = self.driver.find_element(By.XPATH, "(//textarea[@role='textbox'])[1]")
            # Create an ActionChains object
            actions = ActionChains(self.driver)

            # Double-click on the text field
            actions.double_click(json_field).perform()
            # time.sleep(2)
            print("double clicked on the json field")
            text_to_copy = '{"test": true}'
            # pyperclip.copy(text_to_copy)
            # print('Entered  embed')
            # json_field.send_keys(Keys.COMMAND, 'v')
            # json_field.send_keys('hello')
            self.driver.execute_script("arguments[0].value = '';", json_field)

            # Set the new value
            self.driver.execute_script("arguments[0].value = arguments[1];", json_field, text_to_copy)
            
            # Trigger input event
            self.driver.execute_script("arguments[0].dispatchEvent(new Event('input', { bubbles: true }));", json_field)
            
            # Trigger change event
            self.driver.execute_script("arguments[0].dispatchEvent(new Event('change', { bubbles: true }));", json_field)
            # time.sleep(2)
            print("entered json")
            self.wait_and_click("(//button[normalize-space()='Yes'])[1]")
            time.sleep(2)
            print('clicked on yes button')
        elif action_type=='update_can_config':
            self.wait_and_click("(//button[normalize-space()='Click here to Upload'])[1]")
            print("clicked on dropdown")

            can_bitrate = self.driver.find_element(By.XPATH, "(//input[@id='root_can_bitrate'])[1]")
            # can_bitrate.send_keys(Keys.COMMAND, "A")
            self.driver.execute_script("arguments[0].select();", can_bitrate)
            # time.sleep(2)
            can_bitrate.send_keys("5000")
            # time.sleep(2)

            can_filter_mask = self.driver.find_element(By.XPATH, "(//input[@id='root_can_bitrate'])[1]")
            # can_filter_mask.send_keys(Keys.COMMAND, "A")
            self.driver.execute_script("arguments[0].select();", can_filter_mask)
            # time.sleep(2)
            can_filter_mask.send_keys("0x01")
            # time.sleep(2)
            self.wait_and_click("(//button[@title='Add Item'])[1]")
            print("clicked on + icon")
            self.wait_and_click("(//button[@title='Remove'])[1]")
            print("clicked on - icon")
            self.wait_and_click("(//button[@title='Add Item'])[1]")
            print("clicked on + icon")
            can_mask_one = self.driver.find_element(By.XPATH, "(//input[@id='root_data_frequencies_0_can_mask'])[1]")
            can_mask_one.send_keys("0x02")
            # time.sleep(2)
            freq_one = self.driver.find_element(By.XPATH, "(//input[@id='root_data_frequencies_0_can_mask'])[1]")
            freq_one.send_keys("100")
            # time.sleep(2)
            self.wait_and_click("(//button[@title='Add Item'])[1]")
            print("clicked on + icon")
            can_mask_one = self.driver.find_element(By.XPATH, "(//input[@id='root_data_frequencies_1_can_mask'])[1]")
            can_mask_one.send_keys("0x03")
            time.sleep(2)
            freq_one = self.driver.find_element(By.XPATH, "(//input[@id='root_data_frequencies_1_can_mask'])[1]")
            freq_one.send_keys("200")
            time.sleep(2)
            self.wait_and_click("(//button[normalize-space()='Yes'])[1]")
            time.sleep(2)
            print("clicked on yes button")
            print("clicked on yes to perform action on selected devices")
        elif action_type=='update_geofence':
            self.wait_and_click("(//div[normalize-space()='Select Version'])[1]")
            print("clicked on version dropdown")
            self.wait_and_click("(//span[normalize-space()='Bengaluru'])[1]")
            time.sleep(2)
            print("selected the bengaluru as config")
        else:
            print('no selected action type')

    def settings_createmetadatakey(self):
        print('inside settings_createmetadatakey')
        try:
            user_profile = self.driver.find_element(By.XPATH, "(//div[@role='alert'])[1]")
            print(user_profile.text)
            user_profile.click()
            print("1. clicked on user profile")
            self.button_clicks(1, "(//span[normalize-space()='Settings'])[1]")
            print("2. clicked on settings tab")
            self.button_clicks(1, "//a[normalize-space()='Metadata']")
            print("3. clicked on metadata tab")
            self.button_clicks(1, "//button[normalize-space()='Create Metadata']")
            print("4. clicked on create metadata button")
            metadataField = self.driver.find_element(By.XPATH, "//input[@type='text']")
            name = 'meta{}'.format(random.randint(1,1000))
            metadataField.send_keys(name)
            print("8. entered valid metadata")
            self.button_clicks(1, "//button[normalize-space()='Submit']")
            print("16. created metadata key")
            self.driver.refresh()
            print('17. refreshed the page')
            return name

        except Exception as e:
            print('e1. exception')
            file_name = 'settings_createmetadata.png'
            directory_path = 'Screenshots'
            if not os.path.exists(directory_path):
                os.makedirs(directory_path)
            file_path = os.path.abspath(os.path.join(directory_path, file_name))
            self.driver.get_screenshot_as_file(file_path)
            pytest.record_property("screenshot", file_path)  # Record the screenshot path in the report
            self.driver.refresh()
            print('e2. refreshed the page')            
            
            self.driver.execute_script("window.scrollTo(0, 0);")
            print("e3. scrolled the page to top")
            raise e
        
    def settings_delete_metadatakey(self,name):
        
        try:
            self.click_settings_sections('Metadata')
            chosen_value = name

            # Wait for the table to load (adjust timeout as needed)
            wait = WebDriverWait(self.driver, 10)
            table = wait.until(EC.presence_of_element_located((By.XPATH, "(//table[@class='ui celled fixed table'])[1]")))  # Replace 'table-id' with the ID of your table
            print("table located")

            # Find the row containing the chosen value
            rows = table.find_elements(By.TAG_NAME, 'tr')
            print(rows)
            i=0
            for row in rows:
                cells = row.find_elements(By.TAG_NAME, 'td')
                
                print(cells)
                for cell in cells:
                    if chosen_value in cell.text:
                        # Click on the edit icon in the same row
                        if i==0:
                            delete_icon = self.driver.find_element(By.XPATH, '/html[1]/body[1]/div[2]/div[2]/div[3]/div[1]/div[1]/div[2]/div[2]/div[1]/table[1]/tbody[1]/tr[{}]/td[2]/i[2]'.format(i+1))  # Replace 'edit-icon-class' with the class of your edit icon
                            
                            delete_icon.click()
                            print("clicked on delete icon")
                            
                            break
                        else:
                            delete_icon = self.driver.find_element(By.XPATH, '/html[1]/body[1]/div[2]/div[2]/div[3]/div[1]/div[1]/div[2]/div[2]/div[1]/table[1]/tbody[1]/tr[{}]/td[2]/i[2]'.format(i))  # Replace 'edit-icon-class' with the class of your edit icon
                            
                            delete_icon.click()
                            print("clicked on delete icon")
                           
                            break
                        
                        
                else:
                    i=i+1
                    continue
                break
        

            delete_place = self.driver.find_element(By.XPATH, "//input[@type='text']")
            delete_place.send_keys(chosen_value)
            
            self.button_clicks(1, "//button[@class='ui red button']")
            
            print("deleted the metadata key successfully")
            text = "metadata key named Testing104 got deleted successfully"
            # subprocess.call(['say', text])
            
            self.driver.execute_script("window.scrollTo(0, 0);")
            #time.sleep(3)
            print("scrolled the page to top")
            
        except Exception as e:
            file_name = 'settings_delete_metadatakey.png'
            directory_path = 'Screenshots'
            if not os.path.exists(directory_path):
                os.makedirs(directory_path)
            file_path = os.path.abspath(os.path.join(directory_path, file_name))
            self.driver.get_screenshot_as_file(file_path)
            pytest.record_property("screenshot", file_path)  # Record the screenshot path in the report
            self.driver.refresh()
            
            print('refreshed the page')
            
            
            self.driver.execute_script("window.scrollTo(0, 0);")
            
            print("scrolled the page to top")
            raise e
        
    
        


    def edit_metadata(self, metadata_key):
        # for i in range(1,11):
        #     angle_icon_locator = "(//i[@class='angle right icon'])[{}]".format(i)
        #     # try:
        #     #     angle_icon = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, angle_icon_locator)))
        #     # except NoSuchElementException:
        #     #     print("Edit icon not found")
        #     #     return
        #     try:
        #         angle_icon = self.driver.find_element(By.XPATH,"(//i[@class='angle right icon'])[{}]".format(i))
        #     except NoSuchElementException:
        #         print("Edit icon not found")
        #         return
        #     # self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center', behavior: 'smooth'});", angle_icon)
        #     location = angle_icon.location_once_scrolled_into_view
        #     print("window.scrollTo({}, {});".format(location['x'], location['y']))
        #     self.driver.execute_script("window.scrollTo({}, {});".format(location['x'], location['y']))
        #     time.sleep(2)
        #     self.driver.execute_script("arguments[0].click();", angle_icon)
        #     print("clicked on id")
        #     time.sleep(3)
            
        #     self.driver.execute_script("window.scrollTo(0, 0);")
        #     # time.sleep(3)
        #     print("scrolled the page to top")
        #     pencil_locator = "(//i[@id='{}-edit-{}'])[1]".format(i, metadata_key)
        #     # try:
        #     #     pencil = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, pencil_locator)))
        #     # except NoSuchElementException:
        #     #     print("Edit icon not found")
        #     #     return
        #     try:
        #         pencil = self.driver.find_element(By.XPATH,"(//i[@id='{}-edit-{}'])[1]".format(i, metadata_key))
        #     except NoSuchElementException:
        #         print("Edit icon not found")
        #         return
        #     actions = ActionChains(self.driver)
        #     actions.move_to_element(pencil).perform()
        #     pencil.click()
        #     time.sleep(3)
        #     print("clicked on edit icon")
            
        #     # # self.driver.execute_script("arguments[0].scrollIntoView();", pencil)
        #     # # self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center', behavior: 'smooth'});", pencil)
        #     # location = pencil.location_once_scrolled_into_view
        #     # print("window.scrollTo({}, {});".format(location['x'], location['y']))
        #     # self.driver.execute_script("window.scrollTo({}, {});".format(location['x'], location['y']))
        #     # time.sleep(2)
        #     # self.driver.execute_script("arguments[0].click();", pencil)
        #     # print("Clicked on edit icon")
        #     # time.sleep(2)
        #     input_locator = "(//input[@id='{}-input-{}'])[1]".format(i, metadata_key)
        #     # try:
        #     #     input_place = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, input_locator)))
        #     # except NoSuchElementException:
        #     #     print("Edit icon not found")
        #     #     return
        #     try:
        #         input_place = self.driver.find_element(By.XPATH,"(//input[@id='{}-input-{}'])[1]".format(i, metadata_key))
        #     except NoSuchElementException:
        #         print("Edit icon not found")
        #         return
        #     # self.driver.execute_script("arguments[0].scrollIntoView();", input_place)
        #     # self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center', behavior: 'smooth'});", input_place)
        #     location = input_place.location_once_scrolled_into_view
        #     print("window.scrollTo({}, {});".format(location['x'], location['y']))
        #     self.driver.execute_script("window.scrollTo({}, {});".format(location['x'], location['y']))
        #     time.sleep(1)
        #     if i==4 or i==5 or i==6:
        #         self.driver.execute_script("arguments[0].setAttribute('value', arguments[1]);", input_place, "Four")
        #         self.driver.save_screenshot('metaedit{}.png'.format(i))
        #         time.sleep(2)
        #     elif i==7 or i==8:
        #         self.driver.execute_script("arguments[0].setAttribute('value', arguments[1]);", input_place, "Seven")
        #         self.driver.save_screenshot('metaedit{}.png'.format(i))
        #         time.sleep(2)
        #     else:
        #         self.driver.execute_script("arguments[0].setAttribute('value', arguments[1]);", input_place, "First")
        #         self.driver.save_screenshot('metaedit{}.png'.format(i))
        #         time.sleep(2)
        #     submit_button_locator = "(//i[@id='{}-submit-{}'])[1]".format(i, metadata_key)
        #     # try:
        #     #     submit_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, submit_button_locator)))
        #     # except NoSuchElementException:
        #     #     print("Edit icon not found")
        #     #     return
        #     try:
        #         submit_button = self.driver.find_element(By.XPATH,"(//i[@id='{}-submit-{}'])[1]".format(i, metadata_key))
        #     except NoSuchElementException:
        #         print("Edit icon not found")
        #         return
        #     # self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center', behavior: 'smooth'});", submit_button)
        #     location = submit_button.location_once_scrolled_into_view
        #     print("window.scrollTo({}, {});".format(location['x'], location['y']))
        #     self.driver.execute_script("window.scrollTo({}, {});".format(location['x'], location['y']))
        #     time.sleep(2)
        #     self.driver.execute_script("arguments[0].click();", submit_button)
        #     time.sleep(2)
        #     print("edited the metadata value successfully")
        #     angle_icon_locator = "(//i[@class='angle right icon'])[{}]".format(i)
        #     # try:
        #     #     angle_icon = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, angle_icon_locator)))
        #     # except NoSuchElementException:
        #     #     print("Edit icon not found")
        #     #     return
        #     try:
        #         angle_icon = self.driver.find_element(By.XPATH,"(//i[@class='angle right icon'])[{}]".format(i))
        #     except NoSuchElementException:
        #         print("Edit icon not found")
        #         return
        #     # self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center', behavior: 'smooth'});", angle_icon)
        #     location = angle_icon.location_once_scrolled_into_view
        #     print("window.scrollTo({}, {});".format(location['x'], location['y']))
        #     self.driver.execute_script("window.scrollTo({}, {});".format(location['x'], location['y']))
        #     time.sleep(2)
        #     self.driver.execute_script("arguments[0].click();", angle_icon)
        #     print("clicked on id")
        #     self.driver.execute_script("window.scrollTo(0, 0);")
        #     # time.sleep(3)
        #     print("scrolled the page to top")
         
        # #New solution
        # self.wait_and_click("(//div[@class='ui selection dropdown'])[1]")
        # option_locator = "(//span[@class='text'][normalize-space()='{}'])[1]".format(metadata_key)
        # option = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, option_locator)))
        # option.click()
        
        # time.sleep(2)
        # print("entered filter type")
        for i in range(1,11):
            
            filter_place = self.driver.find_element(By.XPATH, "(//input[@placeholder='Find Device by...'])[1]")
            self.wait_and_send_keys("(//input[@placeholder='Find Device by...'])[1]",i)
            time.sleep(3)
            print("entered filter option")
            angle_icon = self.driver.find_element(By.XPATH,"(//i[@class='angle right icon'])[1]")
            angle_icon.click()
            time.sleep(2)
            try:
                pencil = self.driver.find_element(By.XPATH,"(//i[@id='{}-edit-{}'])[1]".format(i, metadata_key))
            except NoSuchElementException:
                print("Edit icon not found")
                return
            actions = ActionChains(self.driver)
            actions.move_to_element(pencil).perform()
            pencil.click()
            time.sleep(3)
            print("clicked on edit icon")
            
            if i==4 or i==5 or i==6:
                self.wait_and_send_keys("(//input[@id='{}-input-{}'])[1]".format(i, metadata_key),"Four")
                
                time.sleep(2)
            elif i==7 or i==8:
                self.wait_and_send_keys("(//input[@id='{}-input-{}'])[1]".format(i, metadata_key),"Seven")
                
                time.sleep(2)
            else:
                self.wait_and_send_keys("(//input[@id='{}-input-{}'])[1]".format(i, metadata_key),"First")
               
                time.sleep(2)
            
            self.wait_and_click("(//i[@id='{}-submit-{}'])[1]".format(i, metadata_key))
            time.sleep(5)
            print("edited the metadata value successfully")
            

            filter_place = self.driver.find_element(By.XPATH, "(//input[@placeholder='Find Device by...'])[1]")
            self.driver.execute_script("arguments[0].value = '';", filter_place)
            # time.sleep(3)
            self.driver.execute_script("window.scrollTo(0, 0);")
            # time.sleep(3)
            print("scrolled the page to top")


    def settings_non_phased_action(self,action_type,action_name,flag,phased, metadata_key, second_metadata_key):
        try:
            name = metadata_key
            second_name = second_metadata_key
            actions_tab = self.driver.find_element(By.LINK_TEXT, "Actions")
            actions_tab.click()
            time.sleep(3)
            print("clicked on actions tab")
            self.wait_and_click("(//i[@class='icon plus square outline'])[1]")
            print("clicked on new action")
            self.wait_and_click("(//button[normalize-space()='Trigger Action'])[1]")
            time.sleep(2)
            print("clicked on request for approval button")
            toast_message = self.driver.find_element(By.XPATH, "(//div[@role='status'])[1]")
            print(toast_message.text)
            time.sleep(2)
            input_text = self.driver.find_element(By.XPATH, "(//input[@type='text'])[1]")
            input_text.send_keys(action_name)
            input_text.send_keys(Keys.RETURN)
            time.sleep(2)
            print("selected action type")
            self.wait_and_click("(//button[normalize-space()='Trigger Action'])[1]")
            time.sleep(2)
            print("clicked on request for approval button")
            toast_message = self.driver.find_element(By.XPATH, "(//div[@role='status'])[1]")
            print(toast_message.text)
            time.sleep(2)
            self.action_type_specific(action_type,phased)
            # self.wait_and_click("(//i[@class='filter icon'])[1]")
            # print("clicked on filters option")
            # self.wait_and_click("(//div[normalize-space()='id'])[1]")
            # print("clicked on id option")
            self.wait_and_click("(//i[@class='filter icon'])[1]")
            print("clicked on filters option")
            option_locator = "(//div[normalize-space()='{}'])[1]".format('id')
            option = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, option_locator)))
            option.click()
            time.sleep(2)
            print("clicked on metadata key option")
            checkbox = self.driver.find_element(By.XPATH,"(//input[@type='checkbox'])[3]")
            self.driver.execute_script("arguments[0].click();", checkbox)
            time.sleep(2)
            print("clicked on first checkbox")
            checkbox = self.driver.find_element(By.XPATH,"(//input[@type='checkbox'])[4]")
            self.driver.execute_script("arguments[0].click();", checkbox)
            time.sleep(2)
            print("clicked on second checkbox")
            
            # self.wait_and_click("(//i[@class='filter icon'])[1]")
            # print("clicked on filters option")

            checkbox = self.driver.find_element(By.XPATH, "//tbody/tr[1]/td[1]/div[1]/input[1]")
            # self.driver.execute_script("arguments[0].checked = true;", checkbox)
            # checkbox.send_keys(Keys.SPACE)
            self.driver.execute_script("arguments[0].click();", checkbox)
            
            time.sleep(2)
            print("clicked on checkboxes")

            try:
                version=self.driver.find_element(By.XPATH,"(//div[normalize-space()='update_config'])[1]")
                print(version.text)
                # time.sleep(2)
                print("update config is coming correctly")
            except Exception as e:
                print("update config is not coming correctly")
            try:
                version=self.driver.find_element(By.XPATH,"(//div[normalize-space()='{}'])[1]".format(name))
                print(version.text)
                # time.sleep(2)
                print("version is coming correctly in summary")
            except Exception as e:
                print("version is not coming correctly in summary")
            try:
                version=self.driver.find_element(By.XPATH,"(//div[normalize-space()='Immediately'])[1]")
                print(version.text)
                # time.sleep(2)
                print("Immediately is coming correctly")
            except Exception as e:
                print("Immediately is not coming correctly")
            try:
                version=self.driver.find_element(By.XPATH,"(//td[contains(text(),'3')])[2]")
                print(version.text)
                # time.sleep(2)
                print("3 is coming correctly")
            except Exception as e:
                print("3 is not coming correctly")
            try:
                version=self.driver.find_element(By.XPATH,"(//td[normalize-space()='Immediately'])[1]")
                print(version.text)
                # time.sleep(2)
                print("Immediately is coming correctly in table")
            except Exception as e:
                print("Immediately is not coming correctly in table")
            self.button_clicks(1,"(//button[normalize-space()='Trigger Action'])[1]")
            time.sleep(3)
            print("clicked on request for approval button and finished the update firmware action successfully")

        except Exception as e:
            file_name = 'non_phased_actions.png'
            directory_path = 'Screenshots'
            if not os.path.exists(directory_path):
                os.makedirs(directory_path)
            file_path = os.path.abspath(os.path.join(directory_path, file_name))
            self.driver.get_screenshot_as_file(file_path)
            pytest.record_property("screenshot", file_path)  # Record the screenshot path in the report
            self.driver.refresh()
            
            print('refreshed the page')
            
            
            self.driver.execute_script("window.scrollTo(0, 0);")
            
            print("scrolled the page to top")
            raise e
        

        
         
    def marking_action_completed(self,action_type,action_name,flag,phased, metadata_key, second_metadata_key):
        try:
            actions_tab = self.driver.find_element(By.LINK_TEXT, "Actions")
            actions_tab.click()
            time.sleep(3)
            print("clicked on actions tab")
            self.wait_and_click("(//i[@title='More details'])[1]")
            print("clicked on eye icon")
            self.wait_and_click("(//i[@title='More details'])[1]")
            print("clicked on eye icon")
            if phased=='phased':
                self.wait_and_click("(//label[@id='sortByIncompleteActions'])[1]")
                print("clicked on sort by incomplete actions")
                try:
                    queued=self.driver.find_element(By.XPATH,"(//td[contains(text(),'Completed')])[1]")
                    # time.sleep(2)
                    print('completed text is there which is incorrect')
                except Exception as e:
                    print('completed text is not there which is correct')
                    # time.sleep(2)
                self.wait_and_click("(//button[normalize-space()='Mark All Complete'])[1]")
                print('clicked on mark all as complete button')
                confirm_disabled=self.driver.find_element(By.XPATH,"(//button[normalize-space()='Confirm'])[1]")
                class_name=confirm_disabled.get_attribute('class')
                if 'disabled' in class_name:
                    print("confirm button is in disabled mode")
                else:
                    print('confirm button is in enabled mode which is incorrect')
                self.wait_and_click("(//button[normalize-space()='Cancel'])[1]")
                print("clicked on cancel button")
            
                self.wait_and_click("(//button[normalize-space()='Mark All Complete'])[1]")
                print('clicked on mark all as complete button')
                field=self.driver.find_element(By.XPATH,"(//input[@type='text'])[1]")
                field.send_keys("Yes")
                time.sleep(2)
                print('entered the text')
                self.wait_and_click("(//button[normalize-space()='Confirm'])[1]")
                print('clicked on confirm button')
                try:
                    queued=self.driver.find_element(By.XPATH,"(//td[contains(text(),'Queued')])[1]")
                    # time.sleep(2)
                    print('queued text is there which is incorrect')
                except Exception as e:
                    print('queued text is not there which is correct')
                    # time.sleep(2)
                try:
                    queued=self.driver.find_element(By.XPATH,"(//button[normalize-space()='Mark All Complete'])[1]")
                    # time.sleep(2)
                    print('mark all complete button is there which is incorrect')
                except Exception as e:
                    print('mark all complete button is not there which is correct')
                    # time.sleep(2)
                try:
                    queued=self.driver.find_element(By.XPATH,"(//h3[normalize-space()='No actions found!'])[1]")
                    # time.sleep(2)
                    print('No actions found text is there which is correct')
                except Exception as e:
                    print('No actions found text is not there which is incorrect')
                    # time.sleep(2)
                self.wait_and_click("(//label[@id='sortByIncompleteActions'])[1]")
                print("clicked on sort by incomplete actions again to disable it")
                # Wait for the table to load (adjust timeout as needed)
                wait = WebDriverWait(self.driver, 10)
                table = wait.until(EC.presence_of_element_located((By.XPATH, "(//table[@class='ui selectable sortable table sc-fRkCxR kaRnyH'])[1]")))  # Replace 'table-id' with the ID of your table
                print("table located")

                # Find the row containing the chosen value
                rows = table.find_elements(By.TAG_NAME, 'tr')
                if len(rows)>1:
                    print("data is showing up which is correct")
                else:
                    print("data is not showing up which is incorrect")

                payload=self.driver.find_element(By.XPATH,"(//i[@title='Mark Action as completed'])[1]")
                class_name=payload.get_attribute("class")
                if 'disabled' in class_name:
                    print("mark action icon is in disabled mode")
                else:
                    print("mark action icon is in enabled mode which is incorrect")
                self.wait_and_click("(//i[@title='View Payload'])[1]")
                print("clicked on payload icon")
                self.wait_and_click("(//button[normalize-space()='OK'])[1]")
                print("clicked on ok button")
                self.driver.execute_script("window.scrollTo(0, 0);")
                # time.sleep(3)
                print("scrolled the page to top")
                self.wait_and_click("(//button[normalize-space()='Action Summary'])[1]")
                print("clicked on actions summary")
                first_page_action_id = self.driver.find_element(By.XPATH,"(//table[@class='ui selectable table sc-kMHJlo jPaBpe'])[1]//tr[1]/td[3]")
                first_page_action_id_text=first_page_action_id.text
                if first_page_action_id_text=="Completed":
                    print("Action is completed for that device which is correct")
                else:
                    print("Action is not completed for that device which is incorrect")
                first_page_action_id = self.driver.find_element(By.XPATH,"(//table[@class='ui selectable table sc-kMHJlo jPaBpe'])[1]//tr[2]/td[3]")
                first_page_action_id_text=first_page_action_id.text
                if first_page_action_id_text=="Scheduled":
                    print("Action is scheduled for that device which is correct")
                else:
                    print("Action is not scheduled for that device which is incorrect")
                self.driver.execute_script("window.scrollTo(0, 0);")
                # time.sleep(3)
                print("scrolled the page to top")
                self.wait_and_click("(//button[normalize-space()='Back'])[1]")
                print("clicked on back button")
                self.wait_and_click("(//button[normalize-space()='Add Phase'])[1]")
                print("clicked on add phase button")
                self.wait_and_click("(//button[normalize-space()='Discard'])[1]")
                print("clicked on discard button")
                self.wait_and_click("(//i[@title='More details'])[1]")
                print("clicked on eye icon")
                self.wait_and_click("(//i[@title='More details'])[2]")
                print("clicked on eye icon")
                try:
                    self.wait_and_click("(//i[@title='Mark Action as completed'])[1]")
                    print("clicked on mark action as completed")
                    
                    confirm_disabled=self.driver.find_element(By.XPATH,"(//button[normalize-space()='Confirm'])[1]")
                    class_name=confirm_disabled.get_attribute('class')
                    if 'disabled' in class_name:
                        print("confirm button is in disabled mode")
                    else:
                        print('confirm button is in enabled mode which is incorrect')
                    self.wait_and_click("(//button[normalize-space()='Cancel'])[1]")
                    print("clicked on cancel button")
                    id_element=self.driver.find_element(By.XPATH,"/html[1]/body[1]/div[2]/div[2]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[1]")
                    id=id_element.text
                    # time.sleep(3)
                    self.wait_and_click("(//i[@title='Mark Action as completed'])[1]")
                    print("clicked on mark action as completed")
                    
                    field=self.driver.find_element(By.XPATH,"(//input[@type='text'])[1]")
                    field.send_keys(id)
                    time.sleep(2)
                    print('entered the text')
                    self.wait_and_click("(//button[normalize-space()='Confirm'])[1]")
                    print('clicked on confirm button')
                    self.driver.execute_script("window.scrollTo(0, 0);")
                    # time.sleep(3)
                    print("scrolled the page to top")
                    self.wait_and_click("(//button[normalize-space()='Action Summary'])[1]")
                    print("clicked on actions summary")
                    self.wait_and_click("(//button[normalize-space()='Back'])[1]")
                    print("clicked on back button")
                    self.driver.execute_script("window.scrollTo(0, 0);")
                    # time.sleep(3)
                    print("scrolled the page to top")
                    add_phase_disabled = self.driver.find_element(By.XPATH,"(//button[normalize-space()='Add Phase'])[1]")
                    class_name = add_phase_disabled.get_attribute('class')
                    if 'disabled' in class_name:
                        print('add phase is coming as disabled after completing the action which is correct')
                    else:
                        print('add phase is not coming as disabled after completing the action which is incorrect')
                except Exception as e:
                    print("it's already become completed by default")

        

            else:
                self.driver.execute_script("window.scrollTo(0, 0);")
                # time.sleep(3)
                print("scrolled the page to top")
                self.wait_and_click("(//button[normalize-space()='Action Summary'])[1]")
                print("clicked on actions summary")
                self.wait_and_click("(//button[normalize-space()='Back'])[1]")
                print("clicked on back button")
                self.driver.execute_script("window.scrollTo(0, 0);")
                # time.sleep(3)
                print("scrolled the page to top")
                self.wait_and_click("(//button[normalize-space()='Add Phase'])[1]")
                print("clicked on add phase button")
                self.wait_and_click("(//button[normalize-space()='Discard'])[1]")
                print("clicked on discard button")

                try:
                    self.wait_and_click("(//div[@title='More Options'])[1]")
                    print("clicked on 3 dots")
                    self.wait_and_click("(//div[@title='Mark Action as completed'][normalize-space()='Mark Action as completed'])[1]")
                    print("clicked on mark action as completed")
                    
                    confirm_disabled=self.driver.find_element(By.XPATH,"(//button[normalize-space()='Confirm'])[1]")
                    class_name=confirm_disabled.get_attribute('class')
                    if 'disabled' in class_name:
                        print("confirm button is in disabled mode")
                    else:
                        print('confirm button is in enabled mode which is incorrect')
                    self.wait_and_click("(//button[normalize-space()='Cancel'])[1]")
                    print("clicked on cancel button")
                    id_element=self.driver.find_element(By.XPATH,"/html[1]/body[1]/div[2]/div[2]/div[3]/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[1]")
                    id=id_element.text
                    # time.sleep(3)
                    self.wait_and_click("(//i[@title='Mark Action as completed'])[1]")
                    print("clicked on mark action as completed")
                    
                    field=self.driver.find_element(By.XPATH,"(//input[@type='text'])[1]")
                    field.send_keys(id)
                    time.sleep(2)
                    print('entered the text')
                    self.wait_and_click("(//button[normalize-space()='Confirm'])[1]")
                    print('clicked on confirm button')
                except Exception as e:
                    self.wait_and_click("(//div[@title='More Options'])[1]")
                    print("clicked on 3 dots")
                    # time.sleep(2)
                    print("it's already become completed by default")
                self.driver.execute_script("window.scrollTo(0, 0);")
                # time.sleep(3)
                print("scrolled the page to top")
                add_phase_disabled = self.driver.find_element(By.XPATH,"(//button[normalize-space()='Add Phase'])[1]")
                class_name = add_phase_disabled.get_attribute('class')
                if 'disabled' in class_name:
                    print('add phase is coming as disabled after completing the action which is correct')
                else:
                    print('add phase is not coming as disabled after completing the action which is incorrect')
                try:
                    queued=self.driver.find_element(By.XPATH,"(//div[@class='ui progress completed'])[1]")
                    print("the progress bar is completed only")
                    # time.sleep(2)
                except Exception as e:
                    print("the progress bar is not completed")

        except Exception as e:
            file_name = 'marking_action_completed.png'
            directory_path = 'Screenshots'
            if not os.path.exists(directory_path):
                os.makedirs(directory_path)
            file_path = os.path.abspath(os.path.join(directory_path, file_name))
            self.driver.get_screenshot_as_file(file_path)
            pytest.record_property("screenshot", file_path)  # Record the screenshot path in the report
            self.driver.refresh()
            
            print('refreshed the page')
            
            
            self.driver.execute_script("window.scrollTo(0, 0);")
            
            print("scrolled the page to top")
            raise e
         
    def device_mgmnt_operations(self,action_type,action_name,flag,phased, metadata_key, second_metadata_key):
        try:
            actions_tab = self.driver.find_element(By.LINK_TEXT, "Actions")
            actions_tab.click()
            time.sleep(3)
            print("clicked on actions tab")
            self.wait_and_click("(//button[normalize-space()='View Details'])[1]")
            print('clicked on view details button')
            self.wait_and_click("(//button[normalize-space()='Back'])[1]")
            print('clicked on back button')
            self.wait_and_click("(//button[normalize-space()='View Details'])[1]")
            print('clicked on view details button')

            try:
                chart=self.driver.find_element(By.XPATH,"(//*[name()='rect'][@class='nsewdrag drag cursor-pointer'])[1]")
                print("the chart is coming correctly")
                # time.sleep(2)
            except Exception as e:
                print("the chart is not coming which is incorrect")
            self.wait_and_click("(//button[normalize-space()='More Info'])[1]")
            print('clicked on more info button')
            try:
                queued=self.driver.find_element(By.XPATH,"(//span[normalize-space()='Action Type'])[1]")
                print("the action type is coming correctly")
                # time.sleep(2)
            except Exception as e:
                print("the action type is not coming which is incorrect")

            try:
                queued=self.driver.find_element(By.XPATH,"(//span[normalize-space()='Action ID'])[1]")
                print("the action ID is coming correctly")
                # time.sleep(2)
            except Exception as e:
                print("the action ID is not coming which is incorrect")

            try:
                queued=self.driver.find_element(By.XPATH,"(//span[normalize-space()='Created At'])[1]")
                print("the created at is coming correctly")
                # time.sleep(2)
            except Exception as e:
                print("the created at is not coming which is incorrect")
            if phased=='phased':
                self.wait_and_click("(//button[normalize-space()='Phase I'])[1]")
                print('clicked on phase 1 button')
                self.wait_and_click("(//button[normalize-space()='More Info'])[1]")
                print('clicked on more info button')
                try:
                    queued=self.driver.find_element(By.XPATH,"(//span[normalize-space()='Action Type'])[1]")
                    print("the action type is coming correctly")
                    # time.sleep(2)
                except Exception as e:
                    print("the action type is not coming which is incorrect")

                try:
                    queued=self.driver.find_element(By.XPATH,"(//span[normalize-space()='Action ID'])[1]")
                    print("the action ID is coming correctly")
                    # time.sleep(2)
                except Exception as e:
                    print("the action ID is not coming which is incorrect")

                try:
                    queued=self.driver.find_element(By.XPATH,"(//span[normalize-space()='Created At'])[1]")
                    print("the created at is coming correctly")
                    # time.sleep(2)
                except Exception as e:
                    print("the created at is not coming which is incorrect")

                try:
                    queued=self.driver.find_element(By.XPATH,"(//span[normalize-space()='Scheduled At'])[1]")
                    print("the scheduled at is coming correctly")
                    # time.sleep(2)
                except Exception as e:
                    print("the scheduled at is not coming which is incorrect")
                self.wait_and_click("(//button[normalize-space()='All Phases'])[1]")
                print('clicked on all phases button')
            self.wait_and_click("(//i[@title='More details'])[1]")
            print("clicked on eye icon")
            self.wait_and_click("(//button[normalize-space()='Action Summary'])[1]")
            print("clicked on actions summary")

            self.wait_and_click("(//i[@title='More details'])[1]")
            print("clicked on eye icon")
            self.wait_and_click("(//span[normalize-space()='Download Config'])[1]")
            print("clicked on download config")
            
            self.driver.execute_script("window.scrollTo(0, 0);")
            time.sleep(2)
            print("scrolled the page to top")
            # config_version = self.driver.find_element(By.XPATH, "(//span[contains(text(),'Config Version')])[4]")
            # config_version.click()
            # time.sleep(3)
            # print("clicked on config version")
            # close_button = self.driver.find_element(By.XPATH, "(//button[normalize-space()='Close'])[1]")
            # close_button.click()
            # time.sleep(3)
            # print("clicked on close button")
            self.wait_and_click("(//span[normalize-space()='Streams'])[1]")
            print("clicked on show streams button")
            self.wait_and_click("//div[normalize-space()='device_shadow']")
            print("clicked on device shadow")
            # # pagination
            # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # time.sleep(3)
            # print("scrolled the page to bottom")
            # second_page = self.driver.find_element(By.XPATH, "(//a[normalize-space()='2'])[1]")
            # second_page.click()
            # time.sleep(5)
            # print("clicked on second page")
            # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # time.sleep(3)
            # print("scrolled the page to bottom")
            # forward_one = self.driver.find_element(By.XPATH, "(//a[contains(text(),'⟩')])[1]")
            # forward_one.click()
            # time.sleep(5)
            # print("clicked on forward_one")
            
            # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # time.sleep(3)
            # print("scrolled the page to bottom")
            # forward_last = self.driver.find_element(By.XPATH, "(//a[normalize-space()='»'])[1]")
            # forward_last.click()
            # time.sleep(5)
            # print("clicked on forward_last")
            # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # time.sleep(3)
            # print("scrolled the page to bottom")
            # backward_one = self.driver.find_element(By.XPATH, "(//a[contains(text(),'⟨')])[1]")
            # backward_one.click()
            # time.sleep(5)
            # print("clicked on backward_one")
            # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # time.sleep(3)
            # print("scrolled the page to bottom")
            # backward_last = self.driver.find_element(By.XPATH, "(//a[normalize-space()='«'])[1]")
            # backward_last.click()
            # time.sleep(5)
            # print("clicked on backward_last")
            # first_page = self.driver.find_element(By.XPATH, "(//a[normalize-space()='1'])[1]")
            # icon_class_name = first_page.get_attribute('class')
            # if 'active' in icon_class_name:
            #     print("forward to last icon is working successfully")
            # else:
            #     print("forward to last icon is working")
            # self.driver.execute_script("window.scrollTo(0, 0);")
            # time.sleep(3)
            # print("scrolled the page to top")

            # #custom time range
            # self.button_clicks(1, "(//i[@class='angle right icon'])[1]")
            # time.sleep(5)
            # print("clicked on angle right icon")
            # try:
            #     no_data=self.driver.find_element(By.XPATH,"(//i[@class='info circle big icon'])[1]")
            #     print("no data is there which is correct")

            # except Exception as e:
            #     print("some data is coming")
            # time_right_text = self.driver.find_element(By.XPATH, "(//div[@class='ui button selection dropdown'])[1]")
            # print(time_right_text.text)
            # time.sleep(4)
            # print("captured time right text")
            # # extracting date and time
            

            # # Sample date string
            # date_string = time_right_text.text

            # # Split the string based on 'to'
            # date_parts = date_string.split(' to ')

            # # Remove any invalid text from each part
            # cleaned_date_parts = [part.strip() for part in date_parts]

            # # Convert date strings to datetime objects
            # aleft_date_1_before = datetime.strptime(cleaned_date_parts[0], "%y-%m-%d %H:%M:%S")
            # aleft_date_2_before = datetime.strptime(cleaned_date_parts[1], "%y-%m-%d %H:%M:%S")

            # self.button_clicks(1, "(//i[@class='angle right icon'])[1]")
            # time.sleep(5)
            # print("clicked on angle right icon")
            
            # time_right_text = self.driver.find_element(By.XPATH, "(//div[@class='ui button selection dropdown'])[1]")
            # print(time_right_text.text)
            # time.sleep(4)
            # print("captured time right text")
            # # Sample date string
            # date_string = time_right_text.text

            # # Split the string based on 'to'
            # date_parts = date_string.split(' to ')

            # # Remove any invalid text from each part
            # cleaned_date_parts = [part.strip() for part in date_parts]

            # # Convert date strings to datetime objects
            # aleft_date_1_after = datetime.strptime(cleaned_date_parts[0], "%y-%m-%d %H:%M:%S")
            # aleft_date_2_after = datetime.strptime(cleaned_date_parts[1], "%y-%m-%d %H:%M:%S")
            

            # # Compare the dates
            # if aleft_date_1_before < aleft_date_1_after and aleft_date_2_before < aleft_date_2_after:
            #     print("working as expected")
            # else:
            #     print("Not working as expected")

            # self.button_clicks(1, "(//i[@class='zoom in icon'])[1]")
            # time.sleep(5)
            # print("clicked on zoom in icon")
            # time_zoom_in_text = self.driver.find_element(By.XPATH, "(//div[@class='ui button selection dropdown'])[1]")
            # print(time_zoom_in_text.text)
            # time.sleep(4)
            # print("captured time zoom in text")
            # # Sample date string
            # date_string = time_zoom_in_text.text

            # # Split the string based on 'to'
            # date_parts = date_string.split(' to ')

            # # Remove any invalid text from each part
            # cleaned_date_parts = [part.strip() for part in date_parts]

            # # Convert date strings to datetime objects
            # azoomin_date_1_after = datetime.strptime(cleaned_date_parts[0], "%y-%m-%d %H:%M:%S")
            # azoomin_date_2_after = datetime.strptime(cleaned_date_parts[1], "%y-%m-%d %H:%M:%S")
            

            # # Compare the dates
            # if aleft_date_1_after < azoomin_date_1_after and azoomin_date_2_after < aleft_date_2_after:
            #     print("working as expected")
            # else:
            #     print("Not working as expected")
            # self.button_clicks(1, "(//i[@class='zoom out icon'])[1]")
            # time.sleep(5)
            # print("clicked on zoom out icon")
            # time_zoom_out_text = self.driver.find_element(By.XPATH, "(//div[@class='ui button selection dropdown'])[1]")
            # print(time_zoom_out_text.text)
            # time.sleep(4)
            # print("captured time zoom out text")
            # # Sample date string
            # date_string = time_zoom_out_text.text

            # # Split the string based on 'to'
            # date_parts = date_string.split(' to ')

            # # Remove any invalid text from each part
            # cleaned_date_parts = [part.strip() for part in date_parts]

            # # Convert date strings to datetime objects
            # azoomout_date_1_after = datetime.strptime(cleaned_date_parts[0], "%y-%m-%d %H:%M:%S")
            # azoomout_date_2_after = datetime.strptime(cleaned_date_parts[1], "%y-%m-%d %H:%M:%S")
            

            # # Compare the dates
            # if azoomout_date_1_after < azoomin_date_1_after and azoomin_date_2_after < azoomout_date_2_after:
            #     print("working as expected")
            # else:
            #     print("Not working as expected")
            # self.button_clicks(1, "(//i[@class='angle left icon'])[1]")
            # time.sleep(5)
            # print("clicked on angle left icon")
            # time_left_text = self.driver.find_element(By.XPATH, "(//div[@class='ui button selection dropdown'])[1]")
            # print(time_left_text.text)
            # time.sleep(4)
            # print("captured time left text")
            # # Sample date string
            # date_string = time_left_text.text

            # # Split the string based on 'to'
            # date_parts = date_string.split(' to ')

            # # Remove any invalid text from each part
            # cleaned_date_parts = [part.strip() for part in date_parts]

            # # Convert date strings to datetime objects
            # aright_date_1_after = datetime.strptime(cleaned_date_parts[0], "%y-%m-%d %H:%M:%S")
            # aright_date_2_after = datetime.strptime(cleaned_date_parts[1], "%y-%m-%d %H:%M:%S")
            

            # # Compare the dates
            # if aright_date_1_after < azoomout_date_1_after and aright_date_2_after < azoomout_date_2_after:
            #     print("working as expected")
            # else:
            #     print("Not working as expected")
            # if time_right_text.text!=time_left_text.text or time_zoom_in_text.text!=time_zoom_out_text.text:
            #     print("working as expected and the icons are working properly")
            # else:
            #     print('icons are not working properly')
            # last_five = self.driver.find_element(By.XPATH, "(//div[@class='ui button selection dropdown'])[1]")
            # last_five.click()
            # time.sleep(4)
            # print("clicked on last five minutes")
            # custom_time = self.driver.find_element(By.XPATH, "(//span[normalize-space()='Custom Time Range'])[1]")
            # custom_time.click()
            # time.sleep(4)
            # print("clicked on custom_time")
            # cancel = self.driver.find_element(By.XPATH, "(//button[normalize-space()='Cancel'])[1]")
            # cancel.click()
            # time.sleep(4)
            # print("clicked on cancel button")
            # last_five = self.driver.find_element(By.XPATH, "(//div[@class='ui button selection dropdown'])[1]")
            # last_five.click()
            # time.sleep(4)
            # print("clicked on last five minutes")
            # custom_time = self.driver.find_element(By.XPATH, "(//span[normalize-space()='Custom Time Range'])[1]")
            # custom_time.click()
            # time.sleep(4)
            # print("clicked on custom_time")

            # first_forward = self.driver.find_element(By.XPATH, "(//i[@class='chevron right fitted icon'])[1]")
            # first_forward.click()
            # time.sleep(4)
            # print("clicked on first_forward")
            # first_backward = self.driver.find_element(By.XPATH, "(//i[@class='chevron left fitted icon'])[1]")
            # first_backward.click()
            # time.sleep(4)
            # print("clicked on first_backward")
            # second_forward = self.driver.find_element(By.XPATH, "(//i[@class='chevron right fitted icon'])[2]")
            # second_forward.click()
            # time.sleep(4)
            # print("clicked on second_forward")
            # second_backward = self.driver.find_element(By.XPATH, "(//i[@class='chevron left fitted icon'])[2]")
            # second_backward.click()
            # time.sleep(4)
            # print("clicked on second_backward")

            

            # minutes_ago = self.driver.find_element(By.XPATH, "(//div[@id='from_dropdown'])[1]")
            # minutes_ago.click()
            # time.sleep(4)
            # print("clicked on minutes_ago")
            
            # thirty_minutes_ago = self.driver.find_element(By.XPATH, "(//span[@class='text'][normalize-space()='30 minutes ago'])[1]")
            # thirty_minutes_ago.click()
            # time.sleep(4)
            # print("clicked on 30 minutes_ago")
            
            # input_box = self.driver.find_element(By.XPATH, "(//input[@value='30'])[1]")
            # # input_box.send_keys(Keys.COMMAND, "A")
            # self.driver.execute_script("arguments[0].value = '';", input_box)
            # input_box.send_keys('45')
            # time.sleep(3)
            # print("entered on input_box")

            # seconds_ago = self.driver.find_element(By.XPATH, "(//div[@id='to_dropdown'])[1]")
            # seconds_ago.click()
            # time.sleep(4)
            # print("clicked on seconds_ago")
            
            # ten_minutes_ago = self.driver.find_element(By.XPATH, "(//span[@class='text'][normalize-space()='10 minutes ago'])[2]")
            # ten_minutes_ago.click()
            # time.sleep(4)
            # print("clicked on 10 minutes_ago")
            
            # input_box = self.driver.find_element(By.XPATH, "(//input[@value='10'])[1]")
            # # input_box.send_keys(Keys.COMMAND, "A")
            # self.driver.execute_script("arguments[0].value = '';", input_box)
            # input_box.send_keys('12')
            # time.sleep(3)
            # print("entered on input_box")

            # toggle = self.driver.find_element(By.XPATH, "(//label[@for='showSaveCustomTimeRangeToggle'])[1]")
            # toggle.click()
            # time.sleep(3)
            # print("clicked on toggle")
            # custom_box = self.driver.find_element(By.XPATH, "(//input[@placeholder='Custom Time Range Label'])[1]")
            # custom_name = '45 to 12 for {}'.format(random.randint(1,100))
            # custom_box.send_keys(custom_name)
            # time.sleep(3)
            # print("entered on custom_box")
            # apply_button = self.driver.find_element(By.XPATH, "(//button[normalize-space()='Apply'])[1]")
            # apply_button.click()
            # time.sleep(5)
            # print("clicked on apply_button")
            
            # last_five = self.driver.find_element(By.XPATH, "(//div[@class='ui button selection dropdown'])[1]")
            # last_five.click()
            # time.sleep(4)
            # print("clicked on last five minutes")
            # custom_time = self.driver.find_element(By.XPATH, "(//span[normalize-space()='Custom Time Range'])[1]")
            # custom_time.click()
            # time.sleep(4)
            # print("clicked on custom_time")
            
            # # nine_text = self.driver.find_element(By.XPATH, "(//span[contains(text(),'9')])[1]")
            # # nine_text.click()
            # # time.sleep(3)
            # # print("clicked on nine_text")

            
            # # wait = WebDriverWait(self.driver, 10)
            
            # # wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[contains(text(),'9')])[1]"))).click()
            # # time.sleep(2)
            # # print("clicked on nine_text")

            # #new addition
            # # Wait for the table to load (adjust timeout as needed)
            # wait = WebDriverWait(self.driver, 10)
            # table = wait.until(EC.presence_of_element_located((By.XPATH, "(//table[@class='ui celled unstackable center aligned table'])[1]")))  # Replace 'table-id' with the ID of your table
            # print("table located")

            # # Find the row containing the chosen value
            # rows = table.find_elements(By.TAG_NAME, 'tr')
            
            # for row in rows:
            #     cells = row.find_elements(By.TAG_NAME, 'td')
                
            #     print(cells)
            #     for cell in cells:
            #         print(cell.text)
            #         if cell.text=="14":
                        
                            
                            
            #                 span_element = cell.find_element(By.TAG_NAME, 'span')
            #                 span_element.click()
            #                 print("clicked on cell")
            #                 time.sleep(5)
            #                 break
            #         else:
            #                 continue
                        
                        
            #     else:
            #         continue
            #     break


            


            
            # nine_o_text = self.driver.find_element(By.XPATH, "(//span[normalize-space()='09:00'])[1]")
            # nine_o_text.click()
            # time.sleep(3)
            # print("clicked on nine_o_text")
            
            # nine_o_text = self.driver.find_element(By.XPATH, "(//span[normalize-space()='09:00'])[1]")
            # nine_o_text.click()
            # time.sleep(3)
            # print("clicked on nine_o_text")

            # from_input=self.driver.find_element(By.XPATH,"(//input[@id='from_input'])[1]")
            # value=from_input.get_attribute('value')
            # print(value)
            # self.driver.execute_script("arguments[0].value = '';", from_input)
            # time.sleep(2)
            # from_input.send_keys('18-01-24 09:00:00')
            # time.sleep(3)
            # print('edited the from input')

            
            # # twenty_eight_text = self.driver.find_element(By.XPATH, "(//span[contains(text(),'28')])[2]")
            # # twenty_eight_text.click()
            # # time.sleep(3)
            # # print("clicked on twenty_eight_text")

            # #new addition
            # # Wait for the table to load (adjust timeout as needed)
            # wait = WebDriverWait(self.driver, 10)
            # table = wait.until(EC.presence_of_element_located((By.XPATH, "(//table[@class='ui celled unstackable center aligned table'])[2]")))  # Replace 'table-id' with the ID of your table
            # print("table located")

            # # Find the row containing the chosen value
            # rows = table.find_elements(By.TAG_NAME, 'tr')
            
            # for row in rows:
            #     cells = row.find_elements(By.TAG_NAME, 'td')
                
            #     print(cells)
            #     for cell in cells:
            #         print(cell.text)
            #         if cell.text=="18":
                        
                            
                            
            #                 span_element = cell.find_element(By.TAG_NAME, 'span')
            #                 span_element.click()
            #                 print("clicked on cell")
            #                 time.sleep(5)
            #                 break
            #         else:
            #                 continue
                        
                        
            #     else:
            #         continue
            #     break


            

            
            # fourteen_text = self.driver.find_element(By.XPATH, "(//span[normalize-space()='14:00'])[1]")
            # fourteen_text.click()
            # time.sleep(3)
            # print("clicked on fourteen_text")
            
            # fourteen_text = self.driver.find_element(By.XPATH, "(//span[normalize-space()='14:00'])[1]")
            # fourteen_text.click()
            # time.sleep(3)
            # print("clicked on fourteen_text")

            # to_input=self.driver.find_element(By.XPATH,"(//input[@id='to_input'])[1]")
            # value=to_input.get_attribute('value')
            # print(value)
            # self.driver.execute_script("arguments[0].value = '';", to_input)
            # time.sleep(2)
            # to_input.send_keys('23-01-24 14:00:00')
            # time.sleep(3)
            # print('edited the to input')

            # toggle = self.driver.find_element(By.XPATH, "(//label[@for='showSaveCustomTimeRangeToggle'])[1]")
            # toggle.click()
            # time.sleep(3)
            # print("clicked on toggle")
            # apply_button = self.driver.find_element(By.XPATH, "(//button[normalize-space()='Apply'])[1]")
            # apply_button.click()
            # time.sleep(2)
            # print("clicked on apply_button")
            # toast_message = self.driver.find_element(By.XPATH, "(//div[@class='toast toast-error'])[1]")
            # print(toast_message.text)
            # time.sleep(5)
            # custom_box = self.driver.find_element(By.XPATH, "(//input[@placeholder='Custom Time Range Label'])[1]")
            # custom_name = 'new_custom{}'.format(random.randint(1,100))
            # custom_box.send_keys(custom_name)
            # time.sleep(3)
            # print("entered on custom_box")
            # apply_button = self.driver.find_element(By.XPATH, "(//button[normalize-space()='Apply'])[1]")
            # apply_button.click()
            # time.sleep(5)
            # print("clicked on apply_button")

            # last_five = self.driver.find_element(By.XPATH, "(//div[@class='ui button selection dropdown'])[1]")
            # last_five.click()
            # time.sleep(4)
            # print("clicked on last five minutes")
            # custom_time = self.driver.find_element(By.XPATH, "(//span[normalize-space()='Custom Time Range'])[1]")
            # custom_time.click()
            # time.sleep(4)
            # print("clicked on custom_time")
            # toggle = self.driver.find_element(By.XPATH, "(//label[@for='showSaveCustomTimeRangeToggle'])[1]")
            # toggle.click()
            # time.sleep(3)
            # print("clicked on toggle")
            # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # time.sleep(3)
            # print("scrolled the page to bottom")
            # delete_custom_name = custom_name+'_delete'
            # print(delete_custom_name)
            # close_icon = self.driver.find_element(By.XPATH, "(//i[@id='{}'])[1]".format(delete_custom_name))
            # close_icon.click()
            # time.sleep(3)
            # print("clicked on close_icon")
            # cancel_custom_name = custom_name+'_cancel'

            # second_close_icon = self.driver.find_element(By.XPATH, "(//i[@id='{}'])[1]".format(cancel_custom_name))
            # second_close_icon.click()
            # time.sleep(3)
            # print("clicked on second_close_icon")

            # delete_custom_name = custom_name+'_delete'
            # close_icon = self.driver.find_element(By.XPATH, "(//i[@id='{}'])[1]".format(delete_custom_name))
            # close_icon.click()
            # time.sleep(3)
            # print("clicked on close_icon")

            # confirm_custom_name = custom_name+'_confirm'

            # second_close_icon = self.driver.find_element(By.XPATH, "(//i[@id='{}'])[1]".format(confirm_custom_name))
            # second_close_icon.click()
            # time.sleep(3)
            # print("clicked on second_close_icon")
            # self.button_clicks(1, "(//button[normalize-space()='Cancel'])[1]")
            # time.sleep(5)
            # print("clicked on cancel")
            self.wait_and_click("(//button[@type='submit'])[1]")
            print("clicked on download button")
            self.wait_and_click("(//button[normalize-space()='Refresh'])[1]")
            print("clicked on refresh button")
            self.wait_and_click("(//button[normalize-space()='Back'])[1]")
            print("clicked on back button")
            self.wait_and_click("(//button[normalize-space()='Close'])[1]")
            print("clicked on close button")
            self.wait_and_click("(//span[normalize-space()='Streams'])[1]")
            print("clicked on show streams button")
            try:
                
                self.wait_and_click("(//div[normalize-space()='uplink_serializer_metrics'])[1]")
                print("clicked on streams bool")
                try:
                    no_data=self.driver.find_element(By.XPATH,"(//i[@class='info circle big icon'])[1]")
                    print("no data is there which is correct")

                except Exception as e:
                    print("some data is coming")
                
            except Exception as e:
                print("that stream is not present")
            self.wait_and_click("(//button[normalize-space()='Close'])[1]")
            print("clicked on close button")
            self.wait_and_click("(//span[normalize-space()='Device Dashboards'])[1]")
            print("clicked on device dashboards button")
            self.wait_and_click("(//button[normalize-space()='Close'])[1]")
            print("clicked on close button")
            self.wait_and_click("(//span[normalize-space()='Device Dashboards'])[1]")
            print("clicked on device dashboards button")
            # dev_dash = self.driver.find_element(By.XPATH, "(//label[normalize-space()='Vehicle Dashboard'])[1]")
            # dev_dash.click()
            # time.sleep(15)
            # print("selected dashboard")
            self.wait_and_click("(//button[normalize-space()='Close'])[1]")
            print("clicked on close button")
            # title_dash=self.driver.find_element(By.XPATH,"(//span[@class='dashboard-title'])[1]")
            # print(title_dash.text)
            # if "Vehicle Dashboard" in title_dash.text:
            #     print("working correctly")
            # else:
            #     print("not working correctly")
            if flag=='rbac':
                try:
                    self.wait_and_click("(//span[normalize-space()='Logs'])[1]")
                    print('clicked on logs button which is incorrect')
                except Exception as e:
                    print("logs button is not available which is correct")
            else:

                self.wait_and_click("(//span[normalize-space()='Logs'])[1]")
                print('clicked on logs button')
            try:
                queued=self.driver.find_element(By.XPATH,"(//td[contains(text(),'Queued')])[1]")
                # time.sleep(2)
                print('queued text is there')
            except Exception as e:
                print('queued text is not there')
                # time.sleep(2)
            if flag=='rbac':
                print("no remote shell option which is correct for rbac")
            else:
                self.wait_and_click("(//span[normalize-space()='Remote Shell'])[1]")
                print("clicked on remote shell")
                # self.button_clicks(1,"(//i[@class='blue expand link icon'])[1]")
                # time.sleep(3)
                # print("clicked on expand to full screen icon")
                # self.button_clicks(1,"(//i[@class='yellow compress link icon'])[1]")
                # time.sleep(3)
                # print("clicked on minimize icon")
                self.wait_and_click("(//button[normalize-space()='Cancel'])[1]")
                print("clicked on cancel button")
            

            


            self.wait_and_click("(//span[normalize-space()='Deactivate'])[1]")
            print('clicked on deactivate button')
            self.wait_and_click("(//button[normalize-space()='Cancel'])[1]")
            print('clicked on cancel button')

            self.wait_and_click("(//span[normalize-space()='Deactivate'])[1]")
            print('clicked on deactivate button')
            self.wait_and_click("(//button[normalize-space()='Deactivate Device'])[1]")
            print('clicked on deactivate device button')

            self.wait_and_click("(//span[normalize-space()='Activate'])[1]")
            print('clicked on activate button')
            self.wait_and_click("(//button[normalize-space()='Cancel'])[1]")
            print('clicked on cancel button')
            self.wait_and_click("(//span[normalize-space()='Activate'])[1]")
            print('clicked on activate button')
            self.wait_and_click("(//button[normalize-space()='Activate Device'])[1]")
            print('clicked on activate device button')
            

            self.driver.execute_script("window.scrollTo(0, 0);")
            # time.sleep(3)
            print("scrolled the page to top")
            self.wait_and_click("(//button[normalize-space()='Action Summary'])[1]")
            print("clicked on actions summary")


            # pagination
            
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # time.sleep(2)
            print("scrolled the page to bottom")
            forward_one = self.driver.find_element(By.LINK_TEXT, "⟩")
            forward_one.click()
            time.sleep(2)
            print("clicked on forward_one")
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # time.sleep(2)
            print("scrolled the page to bottom")
            forward_last = self.driver.find_element(By.LINK_TEXT, "»")
            forward_last.click()
            time.sleep(2)
            print("clicked on forward_last")
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # time.sleep(2)
            print("scrolled the page to bottom")
            backward_one = self.driver.find_element(By.LINK_TEXT, "⟨")
            backward_one.click()
            time.sleep(2)
            print("clicked on backward_one")
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # time.sleep(2)
            print("scrolled the page to bottom")
            backward_last = self.driver.find_element(By.LINK_TEXT, "«")
            backward_last.click()
            time.sleep(2)
            print("clicked on backward_last")
            self.driver.execute_script("window.scrollTo(0, 0);")
            # time.sleep(2)
            print("scrolled the page to top")

            jump_to = self.driver.find_element(By.XPATH, "(//input[@placeholder='Jump to page...'])[1]")
            jump_to.send_keys("7")
            # time.sleep(2)
            jump_to.send_keys(Keys.RETURN)
            time.sleep(2)
            print("clicked on jump to")
            
            # self.driver.execute_script("arguments[0].value = '';", jump_to)
            # time.sleep(3)
            
            # self.driver.execute_script("arguments[0].value = '';", jump_to)
            # time.sleep(3)
            jump_to = self.driver.find_element(By.XPATH, "(//input[@placeholder='Jump to page...'])[1]")
            jump_to.send_keys("23456")
            # time.sleep(2)
            jump_to.send_keys(Keys.RETURN)
            time.sleep(2)
            # self.driver.execute_script("arguments[0].value = '';", jump_to)
            # time.sleep(3)
            # self.driver.refresh()
            # time.sleep(3)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # time.sleep(2)
            print("scrolled the page to bottom")
            jump_to = self.driver.find_element(By.XPATH, "(//input[@placeholder='Jump to page...'])[1]")
            jump_to.send_keys("0")
            # time.sleep(2)
            jump_to.send_keys(Keys.RETURN)
            time.sleep(2)
            try:

                first_page = self.driver.find_element(By.XPATH, "(//a[normalize-space()='1'])[1]")
                icon_class_name = first_page.get_attribute('class')
                if 'active' in icon_class_name:
                    print("moved to first page successfully")
                else:
                    print("Not moved to first page")
            except Exception as e:
                print("not showing the first page which is incorrect")

            jump_to = self.driver.find_element(By.XPATH, "(//input[@placeholder='Jump to page...'])[1]")
            jump_to.send_keys("-1")
            # time.sleep(2)
            jump_to.send_keys(Keys.RETURN)
            time.sleep(2)
            toast_message = self.driver.find_element(By.XPATH, "(//div[@role='status'])[1]")
            print(toast_message.text)
            # time.sleep(2)



            operator = self.driver.find_element(By.XPATH, "(//i[@class='dropdown icon'])[2]")
            operator.click()
            time.sleep(2)
            option_locator = "(//span[normalize-space()='25'])[1]"
            option = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, option_locator)))
            option.click()
            
            time.sleep(2)
            print("entered devices per page")
            self.driver.execute_script("window.scrollTo(0, 0);")
            # time.sleep(2)
            print("scrolled the page to top")
        except Exception as e:
            file_name = 'device_mgmnt_operations.png'
            directory_path = 'Screenshots'
            if not os.path.exists(directory_path):
                os.makedirs(directory_path)
            file_path = os.path.abspath(os.path.join(directory_path, file_name))
            self.driver.get_screenshot_as_file(file_path)
            pytest.record_property("screenshot", file_path)  # Record the screenshot path in the report
            self.driver.refresh()
            
            print('refreshed the page')
            
            
            self.driver.execute_script("window.scrollTo(0, 0);")
            
            print("scrolled the page to top")
            raise e
    
    def action_details_operations(self,action_type,action_name,flag,phased, metadata_key, second_metadata_key):
        try:
            #check in actions details
            few_seconds=self.driver.find_element(By.XPATH,"(//div[normalize-space()='A few seconds ago'])[1]")
            print(few_seconds.text)
            time.sleep(2)
            print("few seconds ago is coming correctly")
            self.wait_and_click("(//i[@title='More details'])[1]")
            print("clicked on eye icon")
            try:
                pending=self.driver.find_element(By.XPATH,"(//td[contains(text(),'PendingApproval')])[1]")
                # time.sleep(2)
                print("pending approval is there")
            except Exception as e:
                print("pending approval is not there")

            if action_type=='update_firmware' and phased=='phased':
                # Wait for the table to load (adjust timeout as needed)
                wait = WebDriverWait(self.driver, 10)
                table = wait.until(EC.presence_of_element_located((By.XPATH, "(//table[@class='ui selectable table sc-kMHJlo jPaBpe'])[1]")))  # Replace 'table-id' with the ID of your table
                print("table located")

                # Find the row containing the chosen value
                rows = table.find_elements(By.TAG_NAME, 'tr')
                print(len(rows))
                if len(rows)==9:
                    print("all phases is showing all the devices correctly which is correct")
                else:
                    print("all phases is not showing all the devices correctly which is incorrect")
                self.driver.execute_script("window.scrollTo(0, 0);")
                time.sleep(3)
                print("scrolled the page to top")
                self.wait_and_click("(//button[normalize-space()='Phase V'])[1]")
                print("clicked on phase 5")
                # Wait for the table to load (adjust timeout as needed)
                wait = WebDriverWait(self.driver, 10)
                table = wait.until(EC.presence_of_element_located((By.XPATH, "(//table[@class='ui selectable table sc-kMHJlo jPaBpe'])[1]")))  # Replace 'table-id' with the ID of your table
                print("table located")

                # Find the row containing the chosen value
                rows = table.find_elements(By.TAG_NAME, 'tr')
                print(len(rows))
                if len(rows)==5:
                    print("phase 5 is showing all the devices correctly which is correct")
                else:
                    print("phase 5 is not showing all the devices correctly which is incorrect")

                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                # time.sleep(3)
                print("scrolled the page to bottom")
                try:
                    jump_to = self.driver.find_element(By.XPATH,"(//input[@placeholder='Jump to page...'])[1]")
                    print("jump to option is there which is correct")
                    first_page = self.driver.find_element(By.XPATH, "(//a[normalize-space()='1'])[1]")
                    icon_class_name = first_page.get_attribute('class')
                    if 'active' in icon_class_name:
                        print("first page is coming in focus which is correct")
                    else:
                        print("first page is not coming in focus which is incorrect")
                except Exception as e:
                    print("no pagination is there which is incorrect")


                self.driver.execute_script("window.scrollTo(0, 0);")
                time.sleep(3)
                print("scrolled the page to top")

                self.wait_and_click("(//button[normalize-space()='Phase I'])[1]")
                print("clicked on phase 1")
                try:
                    no_devices = self.driver.find_element(By.XPATH, "(//b[normalize-space()='No devices'])[1]")
                    print("no devices is showing up in phase 1 which is correct")
                except Exception as e:
                    print("no devices is not showing up in phase 1 which is incorrect")
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                # time.sleep(3)
                print("scrolled the page to bottom")
                try:
                    no_devices = self.driver.find_element(By.XPATH, "(//h4[normalize-space()='No Devices Found!'])[1]")
                    print("no devices is showing up in the table in phase 1 which is correct")
                except Exception as e:
                    print("no devices is not showing up in the table in phase 1 which is incorrect")
                self.wait_and_click("(//button[normalize-space()='Filters'])[1]")
                print("clicked on filters button")
                checkbox = self.driver.find_element(By.XPATH, "(//input[@id='0'])[1]")
                self.driver.execute_script("arguments[0].click();", checkbox)
                time.sleep(2)
                print("clicked on pending approval checkbox")
                self.wait_and_click("(//button[normalize-space()='Filters'])[1]")
                print("clicked on filters button again to close the dropdown")
                try:
                    no_devices = self.driver.find_element(By.XPATH, "(//h4[normalize-space()='No Devices Found!'])[1]")
                    print("no devices is showing up in the table for pending approval filter which is correct")
                except Exception as e:
                    print("no devices is not showing up in the table for pending approval filter which is incorrect")
                self.wait_and_click("(//i[@id='device-list-add-filters-button'])[1]")
                print("clicked on + icon")
                checkbox = self.driver.find_element(By.XPATH, "(//input[@id='1'])[1]")
                self.driver.execute_script("arguments[0].click();", checkbox)
                time.sleep(2)
                print("clicked on scheduled checkbox")
                self.wait_and_click("(//button[normalize-space()='Filters'])[1]")
                print("clicked on filters button")
                self.wait_and_click("(//button[normalize-space()='Filters'])[1]")
                print("clicked on filters button")
                # Wait for the table to load (adjust timeout as needed)
                wait = WebDriverWait(self.driver, 10)
                table = wait.until(EC.presence_of_element_located((By.XPATH, "(//table[@class='ui selectable table sc-kMHJlo jPaBpe'])[1]")))  # Replace 'table-id' with the ID of your table
                print("table located")

                # Find the row containing the chosen value
                rows = table.find_elements(By.TAG_NAME, 'tr')
                if len(rows)==9:
                    print("all phases is showing all the devices correctly which is correct")
                else:
                    print("all phases is not showing all the devices correctly which is incorrect")
                self.wait_and_click("(//i[@class='close icon'])[2]")
                print("clicked on close icon")
                time.sleep(2)
                try:
                    no_devices = self.driver.find_element(By.XPATH, "(//h4[normalize-space()='No Devices Found!'])[1]")
                    print("no devices is showing up in the table for pending approval filter which is correct")
                except Exception as e:
                    print("no devices is not showing up in the table for pending approval filter which is incorrect")
                try:
                    jump_to = self.driver.find_element(By.XPATH,"(//input[@placeholder='Jump to page...'])[1]")
                    print("jump to option is there which is incorrect")
                    first_page = self.driver.find_element(By.XPATH, "(//a[normalize-space()='1'])[1]")
                    icon_class_name = first_page.get_attribute('class')
                    if 'active' in icon_class_name:
                        print("first page is coming in focus which is correct")
                    else:
                        print("first page is not coming in focus which is incorrect")
                except Exception as e:
                    print("no pagination is there which is correct")
                self.wait_and_click("(//i[@class='close icon'])[1]")
                print("clicked on close icon")
                time.sleep(2)
                # Wait for the table to load (adjust timeout as needed)
                wait = WebDriverWait(self.driver, 10)
                table = wait.until(EC.presence_of_element_located((By.XPATH, "(//table[@class='ui selectable table sc-kMHJlo jPaBpe'])[1]")))  # Replace 'table-id' with the ID of your table
                print("table located")

                # Find the row containing the chosen value
                rows = table.find_elements(By.TAG_NAME, 'tr')
                if len(rows)==9:
                    print("all phases is showing all the devices correctly which is correct")
                else:
                    print("all phases is not showing all the devices correctly which is incorrect")
                self.wait_and_click("(//button[normalize-space()='Filters'])[1]")
                print("clicked on filters button")
                checkbox = self.driver.find_element(By.XPATH, "(//input[@id='0'])[1]")
                self.driver.execute_script("arguments[0].click();", checkbox)
                time.sleep(2)
                print("clicked on pending approval checkbox")
                self.wait_and_click("(//button[normalize-space()='Filters'])[1]")
                print("clicked on filters button")
                self.wait_and_click("(//i[@id='device-list-add-filters-button'])[1]")
                print("clicked on + icon")
                checkbox = self.driver.find_element(By.XPATH, "(//input[@id='1'])[1]")
                self.driver.execute_script("arguments[0].click();", checkbox)
                time.sleep(2)
                print("clicked on pending approval checkbox")
                self.wait_and_click("(//button[normalize-space()='Filters'])[1]")
                print("clicked on filters button")
                self.wait_and_click("(//button[normalize-space()='Filters'])[1]")
                print("clicked on filters button")
                self.wait_and_click("(//h3[normalize-space()='Clear All'])[1]")
                print("clicked on clear all hyperlink")
                time.sleep(2)
                # Wait for the table to load (adjust timeout as needed)
                wait = WebDriverWait(self.driver, 10)
                table = wait.until(EC.presence_of_element_located((By.XPATH, "(//table[@class='ui selectable table sc-kMHJlo jPaBpe'])[1]")))  # Replace 'table-id' with the ID of your table
                print("table located")

                # Find the row containing the chosen value
                rows = table.find_elements(By.TAG_NAME, 'tr')
                if len(rows)==9:
                    print("all phases is showing all the devices correctly which is correct")
                else:
                    print("all phases is not showing all the devices correctly which is incorrect")
                self.wait_and_click("(//button[normalize-space()='Filters'])[1]")
                print("clicked on filters button")
                checkbox = self.driver.find_element(By.XPATH, "(//input[@id='0'])[1]")
                self.driver.execute_script("arguments[0].click();", checkbox)
                time.sleep(2)
                print("clicked on pending approval checkbox")
                self.wait_and_click("(//button[normalize-space()='Filters'])[1]")
                print("clicked on filters button again")
                self.wait_and_click("(//i[@id='device-list-add-filters-button'])[1]")
                print("clicked on + icon")
                checkbox = self.driver.find_element(By.XPATH, "(//input[@id='0'])[1]")
                self.driver.execute_script("arguments[0].click();", checkbox)
                time.sleep(2)
                print("clicked on pending approval checkbox again to deselect")
                self.wait_and_click("(//button[normalize-space()='Filters'])[1]")
                print("clicked on filters button")
                self.wait_and_click("(//button[normalize-space()='Filters'])[1]")
                print("clicked on filters button")
                time.sleep(2)
                # Wait for the table to load (adjust timeout as needed)
                wait = WebDriverWait(self.driver, 10)
                table = wait.until(EC.presence_of_element_located((By.XPATH, "(//table[@class='ui selectable table sc-kMHJlo jPaBpe'])[1]")))  # Replace 'table-id' with the ID of your table
                print("table located")

                # Find the row containing the chosen value
                rows = table.find_elements(By.TAG_NAME, 'tr')
                if len(rows)==9:
                    print("all phases is showing all the devices correctly which is correct")
                else:
                    print("all phases is not showing all the devices correctly which is incorrect")



                

                
                




                

            self.driver.execute_script("window.scrollTo(0, 0);")
            time.sleep(3)
            print("scrolled the page to top")
            self.wait_and_click("(//button[normalize-space()='Back'])[1]")
            print("clicked on back button")
            if phased=='phased':
                self.wait_and_click("(//div[@title='More Options'])[1]")
                print("clicked on 3 dots")
                self.wait_and_click("(//div[@title='Release Notes'][normalize-space()='Release Notes'])[1]")
                print("clicked on release notes icon")
                self.wait_and_click("(//button[normalize-space()='Close'])[1]")
                print("clicked on close button")
            else:
                self.wait_and_click("(//div[@title='More Options'])[1]")
                print("clicked on 3 dots")
                payload=self.driver.find_element(By.XPATH,"(//div[@title='Release Notes'][normalize-space()='Release Notes'])[1]")
                class_name=payload.get_attribute("class")
                if 'disabled' in class_name:
                    print("release notes is in disabled mode")
                else:
                    print("release notes is in enabled mode which is incorrect")
                self.wait_and_click("(//div[@title='More Options'])[1]")
                print("clicked on 3 dots")

            if flag=='rbac' or phased=='non_phased':
                try:
                    self.wait_and_click("(//div[@title='More Options'])[1]")
                    print("clicked on 3 dots")
                    approve_action=self.driver.find_element(By.XPATH,"(//div[@title='Approve Action'][normalize-space()='Approve Action'])[1]")
                    class_name=payload.get_attribute("class")
                    if 'disabled' in class_name:
                        print("approve action is in disabled mode which is correct")
                    else:
                        print("approve action is in enabled mode which is incorrect")
                    # time.sleep(2)
                    print("clicked on approve action which is incorrect")
                    self.wait_and_click("(//div[@title='More Options'])[1]")
                    print("clicked on 3 dots")
                except Exception as e:
                    self.wait_and_click("(//div[@title='More Options'])[1]")
                    print("clicked on 3 dots")
                    # time.sleep(2)
                    print("no approve icon which is correct")
            else:
                
                try:
                    self.wait_and_click("(//div[@title='More Options'])[1]")
                    print("clicked on 3 dots")
                    self.wait_and_click("(//div[@title='Approve Action'][normalize-space()='Approve Action'])[1]")
                    print("clicked on approve action which is incorrect")
                    queued=self.driver.find_element(By.XPATH,"(//div[@class='ui active indicating progress scheduled'])[1]")
                    print("the progress bar is scheduled only")
                    self.wait_and_click("(//div[@title='More Options'])[1]")
                    print("clicked on 3 dots")
                    # time.sleep(2)
                except Exception as e:
                    self.wait_and_click("(//div[@title='More Options'])[1]")
                    print("clicked on 3 dots")
                    print("the progress bar is not scheduled")


            

            
            if action_type=='normal_type':
                self.wait_and_click("(//div[@title='More Options'])[1]")
                print("clicked on 3 dots")
                payload=self.driver.find_element(By.XPATH,"(//div[@title='View Payload'][normalize-space()='View Payload'])[1]")
                class_name=payload.get_attribute("class")
                if 'disabled' in class_name:
                    print("view payload is in disabled mode")
                else:
                    print("view payload is in enabled mode which is incorrect")
                self.wait_and_click("(//div[@title='More Options'])[1]")
                print("clicked on 3 dots")
            else:
                self.wait_and_click("(//div[@title='More Options'])[1]")
                print("clicked on 3 dots")
                self.wait_and_click("(//div[@title='View Payload'][normalize-space()='View Payload'])[1]")
                print("clicked on payload icon")
                self.wait_and_click("(//button[normalize-space()='OK'])[1]")
                print("clicked on ok button")
            
            

            try:
                chart=self.driver.find_element(By.XPATH,"(//*[name()='rect'][@class='nsewdrag drag cursor-pointer'])[1]")
                print("the chart is coming correctly")
                # time.sleep(2)
            except Exception as e:
                print("the chart is not coming which is incorrect")
            if flag=='actionsv3' or flag=='rbac':
                self.wait_and_click("(//button[normalize-space()='More Info'])[1]")
                print('clicked on more info button')
                try:
                    queued=self.driver.find_element(By.XPATH,"(//span[normalize-space()='Action Type'])[1]")
                    print("the action type is coming correctly")
                    # time.sleep(2)
                except Exception as e:
                    print("the action type is not coming which is incorrect")

                try:
                    queued=self.driver.find_element(By.XPATH,"(//span[normalize-space()='Action ID'])[1]")
                    print("the action ID is coming correctly")
                    # time.sleep(2)
                except Exception as e:
                    print("the action ID is not coming which is incorrect")

                try:
                    queued=self.driver.find_element(By.XPATH,"(//span[normalize-space()='Created At'])[1]")
                    print("the created at is coming correctly")
                    # time.sleep(2)
                except Exception as e:
                    print("the created at is not coming which is incorrect")
                if phased=='phased':
                    self.wait_and_click("(//button[normalize-space()='Phase I'])[1]")
                    print('clicked on phase 1 button')
                    self.wait_and_click("(//button[normalize-space()='More Info'])[1]")
                    print('clicked on more info button')
                    try:
                        queued=self.driver.find_element(By.XPATH,"(//span[normalize-space()='Action Type'])[1]")
                        print("the action type is coming correctly")
                        # time.sleep(2)
                    except Exception as e:
                        print("the action type is not coming which is incorrect")

                    try:
                        queued=self.driver.find_element(By.XPATH,"(//span[normalize-space()='Action ID'])[1]")
                        print("the action ID is coming correctly")
                        # time.sleep(2)
                    except Exception as e:
                        print("the action ID is not coming which is incorrect")

                    try:
                        queued=self.driver.find_element(By.XPATH,"(//span[normalize-space()='Created At'])[1]")
                        print("the created at is coming correctly")
                        # time.sleep(2)
                    except Exception as e:
                        print("the created at is not coming which is incorrect")

                    try:
                        queued=self.driver.find_element(By.XPATH,"(//span[normalize-space()='Scheduled At'])[1]")
                        print("the scheduled at is coming correctly")
                        # time.sleep(2)
                    except Exception as e:
                        print("the scheduled at is not coming which is incorrect")

        except Exception as e:
            file_name = 'action_details_operations.png'
            directory_path = 'Screenshots'
            if not os.path.exists(directory_path):
                os.makedirs(directory_path)
            file_path = os.path.abspath(os.path.join(directory_path, file_name))
            self.driver.get_screenshot_as_file(file_path)
            pytest.record_property("screenshot", file_path)  # Record the screenshot path in the report
            self.driver.refresh()
            
            print('refreshed the page')
            
            
            self.driver.execute_script("window.scrollTo(0, 0);")
            
            print("scrolled the page to top")
            raise e

            
             
         
         







    

    def settings_phased_action(self,action_type,action_name,flag,phased, metadata_key, second_metadata_key):
        try:
            #phased rollout action
            name = metadata_key
            second_name = second_metadata_key
            actions_tab = self.driver.find_element(By.LINK_TEXT, "Actions")
            actions_tab.click()
            time.sleep(3)
            print("clicked on actions tab")
            self.wait_and_click("(//i[@class='icon plus square outline'])[1]")
            print("clicked on new action")
            self.wait_and_click("(//button[normalize-space()='Trigger Action'])[1]")
            time.sleep(2)
            print("clicked on request for approval button")
            toast_message = self.driver.find_element(By.XPATH, "(//div[@role='status'])[1]")
            print(toast_message.text)
            time.sleep(2)
            input_text = self.driver.find_element(By.XPATH, "(//input[@type='text'])[1]")
            input_text.send_keys(action_name)
            input_text.send_keys(Keys.RETURN)
            time.sleep(2)
            print("selected action type")
            self.wait_and_click("(//button[normalize-space()='Trigger Action'])[1]")
            time.sleep(2)
            print("clicked on request for approval button")
            toast_message = self.driver.find_element(By.XPATH, "(//div[@role='status'])[1]")
            print(toast_message.text)
            time.sleep(2)
            self.action_type_specific(action_type,phased)
            # if phased=='phased':
            
            
            self.wait_and_click("(//label[@id='action-toggle'])[1]")
            print('clicked on phased rollout toggle')

            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            print("scrolled the page to bottom")

            try:
                version=self.driver.find_element(By.XPATH,"(//td[normalize-space()='Phase I'])[1]")
                print(version.text)
                # time.sleep(2)
                print("phase 1 is coming correctly in the summary")
            except Exception as e:
                print("phase 1 is not coming in summary")

            try:
                version=self.driver.find_element(By.XPATH,"(//td[contains(text(),'No devices selected')])[1]")
                print(version.text)
                # time.sleep(2)
                print("no devices selected is coming correctly in the summary")
            except Exception as e:
                print("no devices selected is not coming in summary")
            

            self.driver.execute_script("window.scrollTo(0, 0);")
            time.sleep(2)
            print("scrolled the page to top")
            
            # self.wait_and_click("(//i[@class='filter icon'])[1]")
            # print("clicked on filters option")
            # self.wait_and_click("(//div[normalize-space()='{}'])[1]".format(name))
            # time.sleep(2)
            # print("clicked on city option")
            # self.wait_and_click("(//i[@class='filter icon'])[1]")
            # print("clicked on filters option")
            # time.sleep(2)
            # elements=self.driver.find_elements(By.XPATH, "(//div[@id='dropdown-wrapper'])[1]")
            # elements[-1].click()
            # # option_locator = "(//span[@class='text'][normalize-space()='{}'])[1]".format(name)
            # # option = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, option_locator)))
            # # option.click()
            # time.sleep(2)
            # print("clicked on metadata key option")
            # if flag=='rbac':
            #     checkbox = self.driver.find_element(By.XPATH,"(//label[@for='0'])[1]")
            #     # checkbox.click()
            #     self.driver.execute_script("arguments[0].click();", checkbox)
            #     time.sleep(2)
            #     print("clicked on first checkbox")
            # else:
            #     checkbox = self.driver.find_element(By.XPATH,"(//label[@for='0'])[1]")
            #     # checkbox.click()
            #     self.driver.execute_script("arguments[0].click();", checkbox)
            #     time.sleep(2)
            #     print("clicked on first checkbox")
            

            # try:
            #     icon=self.driver.find_element(By.XPATH,"(//i[@class='file icon'])[1]")
            #     print("icon is there")
            #     info_icon=self.driver.find_element(By.XPATH,"(//i[@class='info circle icon'])[1]")
            #     print("icon is there")
            #     # time.sleep(2)
            # except Exception as e:
            #     # time.sleep(2)
            #     print("icons are not found which is incorrect")
            # self.wait_and_click("(//i[@class='close icon'])[1]")
            # print("clicked on cross icon")

            

            # # id_field = self.driver.find_element(By.XPATH, "(//input[@type='text'])[2]")
            # # id_field.send_keys("2")
            # # id_field.send_keys(Keys.RETURN)
            # # time.sleep(3)
            # # id_field.send_keys("3")
            # # id_field.send_keys(Keys.RETURN)
            # # time.sleep(3)

            

            checkbox = self.driver.find_element(By.XPATH, "//body[1]/div[2]/div[2]/div[3]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[3]/div[3]/table[1]/tbody[1]/tr[1]/td[1]/div[1]/input[1]")
            # self.driver.execute_script("arguments[0].checked = true;", checkbox)
            # checkbox.send_keys(Keys.SPACE)
            self.driver.execute_script("arguments[0].click();", checkbox)
            
            time.sleep(2)
            print("clicked on checkboxes")

            checkbox = self.driver.find_element(By.XPATH, "//body[1]/div[2]/div[2]/div[3]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[3]/div[3]/table[1]/tbody[1]/tr[2]/td[1]/div[1]/input[1]")
            # self.driver.execute_script("arguments[0].checked = true;", checkbox)
            # checkbox.send_keys(Keys.SPACE)
            self.driver.execute_script("arguments[0].click();", checkbox)
            
            time.sleep(2)
            print("clicked on checkboxes")
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            print("scrolled the page to bottom")
            try:
                version=self.driver.find_element(By.XPATH,"(//td[normalize-space()='Phase I'])[1]")
                print(version.text)
                # time.sleep(2)
                print("phase 1 is coming correctly in the summary")
            except Exception as e:
                print("phase 1 is not coming in summary")

            try:
                version=self.driver.find_element(By.XPATH,"(//strong[normalize-space()='Id:'])[1]")
                print(version.text)
                # time.sleep(2)
                print("IDs are coming correctly in the summary")
            except Exception as e:
                print("IDs are not coming in summary")

            self.driver.execute_script("window.scrollTo(0, 0);")
            time.sleep(2)
            print("scrolled the page to top")

            # #clear all functionality
            # clear_all=self.driver.find_element(By.XPATH,"clear")
            # clear_all.click()
            # time.sleep(5)
            # print("clicked on the clear all")
            # try:
            #     icon=self.driver.find_element(By.XPATH,"(//i[@class='file icon'])[3]")
            #     print("icon is there which is incorrect")
            #     info_icon=self.driver.find_element(By.XPATH,"(//i[@class='info circle icon'])[3]")
            #     print("icon is there which is incorrect")
            #     time.sleep(3)
            # except Exception as e:
            #     time.sleep(3)
            #     print("icons are not found which is correct")
            # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # time.sleep(3)
            # print("scrolled the page to bottom")

            # try:
            #     version=self.driver.find_element(By.XPATH,"(//td[contains(text(),'No devices selected')])[1]")
            #     print(version.text)
            #     time.sleep(2)
            #     print("no devices selected is coming correctly in the summary")
            # except Exception as e:
            #     print("no devices selected is not coming in summary")




            self.wait_and_click("(//i[@class='icon plus'])[1]")
            time.sleep(2)
            print('clicked on plus icon')
            
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            print("scrolled the page to bottom")

            try:
                version=self.driver.find_element(By.XPATH,"(//td[normalize-space()='Phase II'])[1]")
                print(version.text)
                # time.sleep(2)
                print("phase 1 is coming correctly in the summary")
            except Exception as e:
                print("phase 1 is not coming in summary")

            try:
                version=self.driver.find_element(By.XPATH,"(//td[contains(text(),'No devices selected')])[1]")
                print(version.text)
                # time.sleep(2)
                print("no devices selected is coming correctly in the summary")
            except Exception as e:
                print("no devices selected is not coming in summary")

            self.driver.execute_script("window.scrollTo(0, 0);")
            time.sleep(2)
            print("scrolled the page to top")
            checkbox = self.driver.find_element(By.XPATH, "//body[1]/div[2]/div[2]/div[3]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[4]/div[3]/table[1]/tbody[1]/tr[3]/td[1]/div[1]/input[1]")
            # self.driver.execute_script("arguments[0].checked = true;", checkbox)
            # checkbox.send_keys(Keys.SPACE)
            self.driver.execute_script("arguments[0].click();", checkbox)
            
            time.sleep(2)
            print("clicked on checkboxes")

            checkbox = self.driver.find_element(By.XPATH, "//body[1]/div[2]/div[2]/div[3]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[4]/div[3]/table[1]/tbody[1]/tr[4]/td[1]/div[1]/input[1]")
            # self.driver.execute_script("arguments[0].checked = true;", checkbox)
            # checkbox.send_keys(Keys.SPACE)
            self.driver.execute_script("arguments[0].click();", checkbox)
            
            time.sleep(2)
            print("clicked on checkboxes")
            checkbox = self.driver.find_element(By.XPATH, "//body[1]/div[2]/div[2]/div[3]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[4]/div[3]/table[1]/tbody[1]/tr[5]/td[1]/div[1]/input[1]")
            # self.driver.execute_script("arguments[0].checked = true;", checkbox)
            # checkbox.send_keys(Keys.SPACE)
            self.driver.execute_script("arguments[0].click();", checkbox)
            
            time.sleep(2)
            print("clicked on checkboxes")
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            print("scrolled the page to bottom")
            try:
                version=self.driver.find_element(By.XPATH,"(//td[normalize-space()='Phase II'])[1]")
                print(version.text)
                # time.sleep(2)
                print("phase 1 is coming correctly in the summary")
            except Exception as e:
                print("phase 1 is not coming in summary")

            try:
                version=self.driver.find_element(By.XPATH,"(//strong[normalize-space()='Id:'])[2]")
                print(version.text)
                # time.sleep(2)
                print("IDs are coming correctly in the summary")
            except Exception as e:
                print("IDs are not coming in summary")

            self.driver.execute_script("window.scrollTo(0, 0);")
            time.sleep(2)
            print("scrolled the page to top")

            self.wait_and_click("(//i[@class='icon plus'])[1]")
            time.sleep(2)
            print('clicked on plus icon')

            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            print("scrolled the page to bottom")

            try:
                version=self.driver.find_element(By.XPATH,"(//td[normalize-space()='Phase III'])[1]")
                print(version.text)
                # time.sleep(2)
                print("phase 1 is coming correctly in the summary")
            except Exception as e:
                print("phase 1 is not coming in summary")

            try:
                version=self.driver.find_element(By.XPATH,"(//td[contains(text(),'No devices selected')])[1]")
                print(version.text)
                # time.sleep(2)
                print("no devices selected is coming correctly in the summary")
            except Exception as e:
                print("no devices selected is not coming in summary")

            self.driver.execute_script("window.scrollTo(0, 0);")
            time.sleep(2)
            print("scrolled the page to top")

            

            
            
            
            try:
                icon=self.driver.find_element(By.XPATH,"(//i[@class='file icon'])[3]")
                print("icon is there which is incorrect")
                info_icon=self.driver.find_element(By.XPATH,"(//i[@class='info circle icon'])[3]")
                print("icon is there which is incorrect")
                # time.sleep(2)
            except Exception as e:
                # time.sleep(2)
                print("icons are not found which is correct")

            if action_type == "update_firmware" and phased=='phased':
                self.wait_and_click("(//i[@class='filter icon'])[3]")
                print("clicked on filters option")
                time.sleep(2)
                self.wait_and_send_keys("(//input[@id='search-action-filters-input'])[1]",name)
                self.wait_and_click("(//div[@id='metadata-name-{}-0'])[1]".format(name))
                # # elements=self.driver.find_elements(By.XPATH, "(//div[@id='dropdown-wrapper'])[1]")
                
                # # elements[-1].click()
                # option_locator = "(//div[normalize-space()='{}'])[1]".format(name)
                # option = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, option_locator)))
                # option.click()
                # time.sleep(2)
                # print("clicked on metadata key option")

                # # self.wait_and_click("(//i[@class='filter icon'])[3]")
                # # print("clicked on filters option")
                
                # # self.wait_and_click("(//div[normalize-space()='{}'])[1]".format(name))
                # # time.sleep(2)
                checkbox = self.driver.find_element(By.XPATH,"(//label[@for='metadata-dropdown-value-1'])[1]")
                # checkbox.click()
                self.driver.execute_script("arguments[0].click();", checkbox)
                time.sleep(2)
                print("clicked on first checkbox")
                self.wait_and_click("(//i[@id='action-add-filters-button-2'])[1]")
                self.wait_and_send_keys("(//input[@id='search-action-filters-input'])[1]",second_name)
                self.wait_and_click("(//div[@id='metadata-name-{}-0'])[1]".format(second_name))
                checkbox = self.driver.find_element(By.XPATH,"(//label[@for='metadata-dropdown-value-0'])[1]")
                # checkbox.click()
                self.driver.execute_script("arguments[0].click();", checkbox)
                time.sleep(2)
                print("clicked on first checkbox")
                self.wait_and_click("(//i[@class='close icon'])[2]")
                print("clicked on cross icon")
                try:
                    icon=self.driver.find_element(By.XPATH,"(//i[@class='file icon'])[2]")
                    print("icon is there which is incorrect")
                    info_icon=self.driver.find_element(By.XPATH,"(//i[@class='info circle icon'])[2]")
                    print("icon is there which is incorrect")
                    # time.sleep(2)
                except Exception as e:
                    # time.sleep(2)
                    print("icons are not found which is correct")
                self.wait_and_click("(//i[@id='action-add-filters-button-2'])[1]")
                self.wait_and_send_keys("(//input[@id='search-action-filters-input'])[1]",second_name)
                self.wait_and_click("(//div[@id='metadata-name-{}-0'])[1]".format(second_name))
                checkbox = self.driver.find_element(By.XPATH,"(//label[@for='metadata-dropdown-value-0'])[1]")
                # checkbox.click()
                self.driver.execute_script("arguments[0].click();", checkbox)
                time.sleep(2)
                print("clicked on first checkbox")
                self.wait_and_click("(//h3[normalize-space()='Clear All'])[1]")
                print("clicked on clear all hyperlink")
                time.sleep(3)
                first_page_action_id = self.driver.find_element(By.XPATH,"(//table[@class='ui celled selectable table'])[3]//tr[1]/td[2]")
                first_page_action_id_text=first_page_action_id.text
                print(first_page_action_id_text)
                first_page_action_id_text_int=int(first_page_action_id_text)
                print(first_page_action_id_text_int)
                if first_page_action_id_text_int!=4:
                    print("clear all hyperlink is functioning properly which is correct")
                else:
                    print("clear all hyperlink is not functioning properly which is incorrect")

                    
                    
            self.wait_and_click("(//i[@class='filter icon'])[3]")
            print("clicked on filters option")
            time.sleep(2)
            self.wait_and_send_keys("(//input[@id='search-action-filters-input'])[1]",name)
            self.wait_and_click("(//div[@id='metadata-name-{}-0'])[1]".format(name))
            # # elements=self.driver.find_elements(By.XPATH, "(//div[@id='dropdown-wrapper'])[1]")
            
            # # elements[-1].click()
            # option_locator = "(//div[normalize-space()='{}'])[1]".format(name)
            # option = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, option_locator)))
            # option.click()
            # time.sleep(2)
            # print("clicked on metadata key option")

            # # self.wait_and_click("(//i[@class='filter icon'])[3]")
            # # print("clicked on filters option")
            
            # # self.wait_and_click("(//div[normalize-space()='{}'])[1]".format(name))
            # # time.sleep(2)
            checkbox = self.driver.find_element(By.XPATH,"(//label[@for='metadata-dropdown-value-1'])[1]")
            # checkbox.click()
            self.driver.execute_script("arguments[0].click();", checkbox)
            time.sleep(2)
            print("clicked on first checkbox")
            self.wait_and_click("(//i[@id='action-add-filters-button-2'])[1]")
            self.wait_and_send_keys("(//input[@id='search-action-filters-input'])[1]",second_name)
            self.wait_and_click("(//div[@id='metadata-name-{}-0'])[1]".format(second_name))
            checkbox = self.driver.find_element(By.XPATH,"(//label[@for='metadata-dropdown-value-0'])[1]")
            # checkbox.click()
            self.driver.execute_script("arguments[0].click();", checkbox)
            time.sleep(2)
            print("clicked on first checkbox")
            percentages=self.driver.find_element(By.XPATH,"(//input[@placeholder='Enter Percentage'])[3]")
            self.driver.execute_script("arguments[0].value = '';", percentages)
            time.sleep(2)
            percentages.send_keys('40')
            time.sleep(2)
            print("entered 40 as the percentage")
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
            print("scrolled the page to bottom")
            try:
                version=self.driver.find_element(By.XPATH,"(//td[normalize-space()='Phase III'])[1]")
                print(version.text)
                # time.sleep(2)
                print("phase 1 is coming correctly in the summary")
            except Exception as e:
                print("phase 1 is not coming in summary")

            try:
                version=self.driver.find_element(By.XPATH,"(//strong[normalize-space()='{}:'])[1]".format(name))
                print(version.text)
                # time.sleep(2)
                print("IDs are coming correctly in the summary")
            except Exception as e:
                print("IDs are not coming in summary")

            self.driver.execute_script("window.scrollTo(0, 0);")
            time.sleep(2)
            print("scrolled the page to top")
            self.wait_and_click("(//i[@class='icon plus'])[1]")
            print('clicked on plus icon')
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            print("scrolled the page to bottom")

            try:
                version=self.driver.find_element(By.XPATH,"(//td[normalize-space()='Phase IV'])[1]")
                print(version.text)
                # time.sleep(2)
                print("phase 1 is coming correctly in the summary")
            except Exception as e:
                print("phase 1 is not coming in summary")

            try:
                version=self.driver.find_element(By.XPATH,"(//td[contains(text(),'No devices selected')])[1]")
                print(version.text)
                # time.sleep(2)
                print("no devices selected is coming correctly in the summary")
            except Exception as e:
                print("no devices selected is not coming in summary")

            self.driver.execute_script("window.scrollTo(0, 0);")
            time.sleep(2)
            print("scrolled the page to top")
            # self.wait_and_click("(//i[@class='filter icon'])[4]")
            # print("clicked on filters option")
            # self.wait_and_click("(//div[normalize-space()='{}'])[1]".format(name))
            # time.sleep(2)
            # print("clicked on city option")
            self.wait_and_click("(//i[@class='filter icon'])[4]")
            print("clicked on filters option")
            time.sleep(2)
            self.wait_and_send_keys("(//input[@id='search-action-filters-input'])[1]",name)
            self.wait_and_click("(//div[@id='metadata-name-{}-0'])[1]".format(name))
            # # elements=self.driver.find_elements(By.XPATH, "(//div[@id='dropdown-wrapper'])[1]")
            
            # # elements[-1].click()
            # option_locator = "(//div[normalize-space()='{}'])[1]".format(name)
            # option = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, option_locator)))
            # option.click()
            # time.sleep(2)
            # print("clicked on metadata key option")

            # # self.wait_and_click("(//i[@class='filter icon'])[3]")
            # # print("clicked on filters option")
            
            # # self.wait_and_click("(//div[normalize-space()='{}'])[1]".format(name))
            # # time.sleep(2)
            checkbox = self.driver.find_element(By.XPATH,"(//label[@for='metadata-dropdown-value-1'])[1]")
            # checkbox.click()
            self.driver.execute_script("arguments[0].click();", checkbox)
            time.sleep(2)
            print("clicked on first checkbox")
            self.wait_and_click("(//i[@id='action-add-filters-button-2'])[1]")
            self.wait_and_send_keys("(//input[@id='search-action-filters-input'])[1]",second_name)
            self.wait_and_click("(//div[@id='metadata-name-{}-0'])[1]".format(second_name))
            checkbox = self.driver.find_element(By.XPATH,"(//label[@for='metadata-dropdown-value-0'])[1]")
            # checkbox.click()
            self.driver.execute_script("arguments[0].click();", checkbox)
            time.sleep(2)
            print("clicked on first checkbox")
            
            try:
                icon=self.driver.find_element(By.XPATH,"(//i[@class='file icon'])[4]")
                print("icon is there")
                info_icon=self.driver.find_element(By.XPATH,"(//i[@class='info circle icon'])[4]")
                print("icon is there")
                # time.sleep(2)
            except Exception as e:
                # time.sleep(2)
                print("icons are not found which is incorrect")
            percentages=self.driver.find_element(By.XPATH,"(//input[@placeholder='Enter Percentage'])[4]")
            self.driver.execute_script("arguments[0].value = '';", percentages)
            time.sleep(2)
            percentages.send_keys('20')
            time.sleep(2)
            print("entered 40 as the percentage")
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            print("scrolled the page to bottom")
            try:
                version=self.driver.find_element(By.XPATH,"(//td[normalize-space()='Phase IV'])[1]")
                print(version.text)
                # time.sleep(2)
                print("phase 1 is coming correctly in the summary")
            except Exception as e:
                print("phase 1 is not coming in summary")

            try:
                version=self.driver.find_element(By.XPATH,"(//strong[normalize-space()='{}:'])[2]".format(name))
                print(version.text)
                # time.sleep(2)
                print("IDs are coming correctly in the summary")
            except Exception as e:
                print("IDs are not coming in summary")

            self.driver.execute_script("window.scrollTo(0, 0);")
            time.sleep(2)
            print("scrolled the page to top")
            self.wait_and_click("(//i[@class='icon plus'])[1]")
            print('clicked on plus icon')
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            print("scrolled the page to bottom")

            try:
                version=self.driver.find_element(By.XPATH,"(//td[normalize-space()='Phase V'])[1]")
                print(version.text)
                # time.sleep(2)
                print("phase 1 is coming correctly in the summary")
            except Exception as e:
                print("phase 1 is not coming in summary")

            try:
                version=self.driver.find_element(By.XPATH,"(//td[contains(text(),'No devices selected')])[1]")
                print(version.text)
                # time.sleep(2)
                print("no devices selected is coming correctly in the summary")
            except Exception as e:
                print("no devices selected is not coming in summary")

            self.driver.execute_script("window.scrollTo(0, 0);")
            time.sleep(2)
            print("scrolled the page to top")
            # self.wait_and_click("(//i[@class='filter icon'])[5]")
            # print("clicked on filters option")
            # self.wait_and_click("(//div[normalize-space()='{}'])[1]".format(name))
            # time.sleep(2)
            # print("clicked on city option")
            self.wait_and_click("(//i[@class='filter icon'])[5]")
            print("clicked on filters option")
            time.sleep(2)
            self.wait_and_send_keys("(//input[@id='search-action-filters-input'])[1]",name)
            self.wait_and_click("(//div[@id='metadata-name-{}-0'])[1]".format(name))
            checkbox = self.driver.find_element(By.XPATH,"(//label[@for='metadata-dropdown-value-0'])[1]")
            # checkbox.click()
            self.driver.execute_script("arguments[0].click();", checkbox)
            time.sleep(2)
            print("clicked on first checkbox")
            
            
            try:
                icon=self.driver.find_element(By.XPATH,"(//i[@class='file icon'])[5]")
                print("icon is there")
                info_icon=self.driver.find_element(By.XPATH,"(//i[@class='info circle icon'])[5]")
                print("icon is there")
                time.sleep(2)
            except Exception as e:
                time.sleep(2)
                print("icons are not found which is incorrect")
            percentages=self.driver.find_element(By.XPATH,"(//input[@placeholder='Enter Percentage'])[5]")
            self.driver.execute_script("arguments[0].value = '';", percentages)
            time.sleep(2)
            percentages.send_keys('60')
            time.sleep(2)
            print("entered 60 as the percentage")
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            print("scrolled the page to bottom")
            try:
                version=self.driver.find_element(By.XPATH,"(//td[normalize-space()='Phase V'])[1]")
                print(version.text)
                # time.sleep(2)
                print("phase 1 is coming correctly in the summary")
            except Exception as e:
                print("phase 1 is not coming in summary")

            try:
                version=self.driver.find_element(By.XPATH,"(//strong[normalize-space()='{}:'])[1]".format(name))
                print(version.text)
                # time.sleep(2)
                print("IDs are coming correctly in the summary")
            except Exception as e:
                print("IDs are not coming in summary")

            self.driver.execute_script("window.scrollTo(0, 0);")
            time.sleep(2)
            print("scrolled the page to top")
            self.wait_and_click("(//i[@class='icon plus'])[1]")
            print('clicked on plus icon')
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            print("scrolled the page to bottom")

            try:
                version=self.driver.find_element(By.XPATH,"(//td[normalize-space()='Phase VI'])[1]")
                print(version.text)
                # time.sleep(2)
                print("phase 1 is coming correctly in the summary")
            except Exception as e:
                print("phase 1 is not coming in summary")

            try:
                version=self.driver.find_element(By.XPATH,"(//td[contains(text(),'No devices selected')])[1]")
                print(version.text)
                # time.sleep(2)
                print("no devices selected is coming correctly in the summary")
            except Exception as e:
                print("no devices selected is not coming in summary")

            self.driver.execute_script("window.scrollTo(0, 0);")
            time.sleep(2)
            print("scrolled the page to top")
            # self.wait_and_click("(//i[@class='filter icon'])[6]")
            # print("clicked on filters option")
            # self.wait_and_click("(//div[normalize-space()='{}'])[1]".format(name))
            # time.sleep(2)
            # print("clicked on city option")
            self.wait_and_click("(//i[@class='filter icon'])[6]")
            print("clicked on filters option")
            time.sleep(2)
            self.wait_and_send_keys("(//input[@id='search-action-filters-input'])[1]",name)
            self.wait_and_click("(//div[@id='metadata-name-{}-0'])[1]".format(name))
            checkbox = self.driver.find_element(By.XPATH,"(//label[@for='metadata-dropdown-value-2'])[1]")
            # checkbox.click()
            self.driver.execute_script("arguments[0].click();", checkbox)
            time.sleep(2)
            print("clicked on first checkbox")
            try:
                icon=self.driver.find_element(By.XPATH,"(//i[@class='file icon'])[6]")
                print("icon is there")
                info_icon=self.driver.find_element(By.XPATH,"(//i[@class='info circle icon'])[6]")
                print("icon is there")
                # time.sleep(2)
            except Exception as e:
                # time.sleep(2)
                print("icons are not found which is incorrect")
            
            
            
            

            checkbox = self.driver.find_element(By.XPATH, "//body[1]/div[2]/div[2]/div[3]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[8]/div[4]/table[1]/tbody[1]/tr[1]/td[1]/div[1]/input[1]")
            # self.driver.execute_script("arguments[0].checked = true;", checkbox)
            # checkbox.send_keys(Keys.SPACE)
            self.driver.execute_script("arguments[0].click();", checkbox)
            
            time.sleep(2)
            print("clicked on checkboxes")
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            print("scrolled the page to bottom")
            try:
                percentage=self.driver.find_element(By.XPATH,"(//input[@placeholder='Enter Percentage'])[6]")
                # time.sleep(2)
                print("percentage is not there which is correct")
            except Exception as e:
                # time.sleep(2)
                print("percentage is there which is incorrect")
            self.driver.execute_script("window.scrollTo(0, 0);")
            time.sleep(2)
            print("scrolled the page to top")
            self.wait_and_click("(//i[@class='desktop icon'])[6]")
            print("clicked on display option")
            self.button_clicks(1,"(//h3[normalize-space()='{}'])[1]".format(name))
            time.sleep(5)
            print("clicked on owner option")
            forward_one = self.driver.find_element(By.LINK_TEXT, "⟩")
            forward_one.click()
            time.sleep(2)
            print("clicked on forward_one")
            backward_one = self.driver.find_element(By.LINK_TEXT, "⟨")
            backward_one.click()
            time.sleep(2)
            print("clicked on backward_one")
            try:
                owner=self.driver.find_element(By.XPATH,"(//th[contains(text(),'{}')])[6]".format(name))
                # time.sleep(2)
                print("owner option is coming which is correct")
            except Exception as e:
                # time.sleep(2)
                print("owner option isn't coming which is incorrect")
            self.wait_and_click("(//i[@class='desktop icon'])[6]")
            print("clicked on display option")
            self.button_clicks(1,"(//h3[normalize-space()='{}'])[1]".format(name))
            time.sleep(2)
            print("clicked on owner option")
            forward_one = self.driver.find_element(By.LINK_TEXT, "⟩")
            forward_one.click()
            time.sleep(2)
            print("clicked on forward_one")
            backward_one = self.driver.find_element(By.LINK_TEXT, "⟨")
            backward_one.click()
            time.sleep(2)
            print("clicked on backward_one")
            try:
                owner=self.driver.find_element(By.XPATH,"(//th[contains(text(),'{}')])[6]".format(name))
                # time.sleep(2)
                print("owner option is coming which is incorrect")
            except Exception as e:
                # time.sleep(2)
                print("owner option isn't coming which is correct")
            try:
                version=self.driver.find_element(By.XPATH,"(//td[normalize-space()='Phase VI'])[1]")
                print(version.text)
                # time.sleep(2)
                print("phase 1 is coming correctly in the summary")
            except Exception as e:
                print("phase 1 is not coming in summary")

            try:
                version=self.driver.find_element(By.XPATH,"(//strong[normalize-space()='{}:'])[2]".format(name))
                print(version.text)
                # time.sleep(2)
                print("IDs are coming correctly in the summary")
            except Exception as e:
                print("IDs are not coming in summary")

            self.driver.execute_script("window.scrollTo(0, 0);")
            time.sleep(2)
            print("scrolled the page to top")

            

            #advanced
            self.wait_and_click("(//label[@id='action-toggle'])[2]")
            print('clicked on advanced toggle')
            self.wait_and_click("(//label[@id='action-toggle'])[3]")
            print("clicked on auto retry toggle")
            self.wait_and_click("(//div[@class='ui selection dropdown'])[1]")
            print('clicked on select period')
            self.wait_and_click("(//span[normalize-space()='12 hours'])[1]")
            print('clicked on 12 hours option')
            try:
                # release_notes=self.driver.find_element(By.XPATH,"(//textarea[@role='textbox'])[1]")
                # release_notes.send_keys("this is just to check")
                # time.sleep(2)
                self.wait_and_send_keys("(//textarea[@role='textbox'])[1]","this is just to check")
                print("entered the release notes text")
            except Exception as e:
                print("release notes is not there")





            try:
                version=self.driver.find_element(By.XPATH,"(//div[normalize-space()='update_can_config'])[1]")
                print(version.text)
                # time.sleep(2)
                print("update config is coming correctly")
            except Exception as e:
                print("update config is not coming correctly")
            
            try:
                version=self.driver.find_element(By.XPATH,"(//div[normalize-space()='Immediately'])[1]")
                print(version.text)
                # time.sleep(2)
                print("Immediately is coming correctly")
            except Exception as e:
                print("Immediately is not coming correctly")
            # try:
            #     version=self.driver.find_element(By.XPATH,"(//td[contains(text(),'3')])[2]")
            #     print(version.text)
            #     time.sleep(2)
            #     print("3 is coming correctly")
            # except Exception as e:
            #     print("3 is not coming correctly")
            # try:
            #     version=self.driver.find_element(By.XPATH,"(//td[normalize-space()='Immediately'])[1]")
            #     print(version.text)
            #     time.sleep(2)
            #     print("Immediately is coming correctly in table")
            # except Exception as e:
            #     print("Immediately is not coming correctly in table")
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # time.sleep(2)
            print("scrolled the page to bottom")
            self.wait_and_click("(//button[normalize-space()='Trigger Action'])[1]")
            time.sleep(2)
            print("clicked on request for approval button")
            toast_message = self.driver.find_element(By.XPATH, "(//div[@role='status'])[1]")
            print(toast_message.text)
            # time.sleep(2)
            self.driver.execute_script("window.scrollTo(0, 0);")
            # time.sleep(2)
            print("scrolled the page to top")
            self.wait_and_click("(//div[@id='Phase IV'])[1]")
            print("clicked on phase 4")
            percentages=self.driver.find_element(By.XPATH,"(//input[@placeholder='Enter Percentage'])[4]")
            self.driver.execute_script("arguments[0].value = '';", percentages)
            time.sleep(2)
            percentages.send_keys('60')
            time.sleep(2)
            print("entered 60 as the percentage")
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # time.sleep(2)
            print("scrolled the page to bottom")
            self.wait_and_click("(//button[normalize-space()='Trigger Action'])[1]")
            # time.sleep(2)
            print("clicked on request for approval button")
            toast_message = self.driver.find_element(By.XPATH, "(//div[@role='status'])[1]")
            print(toast_message.text)
            # time.sleep(2)
            self.driver.execute_script("window.scrollTo(0, 0);")
            # time.sleep(2)
            print("scrolled the page to top")
            self.wait_and_click("(//div[@id='Phase V'])[1]")
            print("clicked on phase 5")
            percentages=self.driver.find_element(By.XPATH,"(//input[@placeholder='Enter Percentage'])[5]")
            self.driver.execute_script("arguments[0].value = '';", percentages)
            time.sleep(2)
            percentages.send_keys('100')
            time.sleep(2)
            print("entered 100 as the percentage")
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # time.sleep(2)
            print("scrolled the page to bottom")
            self.wait_and_click("(//button[normalize-space()='Trigger Action'])[1]")
            time.sleep(7)
            print("clicked on request for approval button")
            print("clicked on request for approval button and finished the update config action successfully")
            # else:
            #     # self.wait_and_click("(//i[@class='filter icon'])[1]")
            #     # print("clicked on filters option")
            #     # self.wait_and_click("(//div[normalize-space()='id'])[1]")
            #     # print("clicked on id option")
            #     self.wait_and_click("(//i[@class='filter icon'])[1]")
            #     print("clicked on filters option")
            #     option_locator = "(//div[normalize-space()='{}'])[1]".format('id')
            #     option = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, option_locator)))
            #     option.click()
            #     time.sleep(2)
            #     print("clicked on metadata key option")
            #     checkbox = self.driver.find_element(By.XPATH,"(//input[@type='checkbox'])[3]")
            #     self.driver.execute_script("arguments[0].click();", checkbox)
            #     time.sleep(2)
            #     print("clicked on first checkbox")
            #     checkbox = self.driver.find_element(By.XPATH,"(//input[@type='checkbox'])[4]")
            #     self.driver.execute_script("arguments[0].click();", checkbox)
            #     time.sleep(2)
            #     print("clicked on second checkbox")
                
            #     # self.wait_and_click("(//i[@class='filter icon'])[1]")
            #     # print("clicked on filters option")

            #     checkbox = self.driver.find_element(By.XPATH, "//tbody/tr[1]/td[1]/div[1]/input[1]")
            #     # self.driver.execute_script("arguments[0].checked = true;", checkbox)
            #     # checkbox.send_keys(Keys.SPACE)
            #     self.driver.execute_script("arguments[0].click();", checkbox)
                
            #     time.sleep(2)
            #     print("clicked on checkboxes")

            #     try:
            #         version=self.driver.find_element(By.XPATH,"(//div[normalize-space()='update_config'])[1]")
            #         print(version.text)
            #         # time.sleep(2)
            #         print("update config is coming correctly")
            #     except Exception as e:
            #         print("update config is not coming correctly")
            #     try:
            #         version=self.driver.find_element(By.XPATH,"(//div[normalize-space()='{}'])[1]".format(name))
            #         print(version.text)
            #         # time.sleep(2)
            #         print("version is coming correctly in summary")
            #     except Exception as e:
            #         print("version is not coming correctly in summary")
            #     try:
            #         version=self.driver.find_element(By.XPATH,"(//div[normalize-space()='Immediately'])[1]")
            #         print(version.text)
            #         # time.sleep(2)
            #         print("Immediately is coming correctly")
            #     except Exception as e:
            #         print("Immediately is not coming correctly")
            #     try:
            #         version=self.driver.find_element(By.XPATH,"(//td[contains(text(),'3')])[2]")
            #         print(version.text)
            #         # time.sleep(2)
            #         print("3 is coming correctly")
            #     except Exception as e:
            #         print("3 is not coming correctly")
            #     try:
            #         version=self.driver.find_element(By.XPATH,"(//td[normalize-space()='Immediately'])[1]")
            #         print(version.text)
            #         # time.sleep(2)
            #         print("Immediately is coming correctly in table")
            #     except Exception as e:
            #         print("Immediately is not coming correctly in table")
            #     self.button_clicks(1,"(//button[normalize-space()='Trigger Action'])[1]")
            #     time.sleep(3)
            #     print("clicked on request for approval button and finished the update firmware action successfully")


            # #check in actions details
            # few_seconds=self.driver.find_element(By.XPATH,"(//div[normalize-space()='A few seconds ago'])[1]")
            # print(few_seconds.text)
            # time.sleep(2)
            # print("few seconds ago is coming correctly")
            # self.wait_and_click("(//i[@title='More details'])[1]")
            # print("clicked on eye icon")
            # try:
            #     pending=self.driver.find_element(By.XPATH,"(//td[contains(text(),'PendingApproval')])[1]")
            #     # time.sleep(2)
            #     print("pending approval is there")
            # except Exception as e:
            #     print("pending approval is not there")

            # if action_type=='update_firmware' and phased=='phased':
            #     # Wait for the table to load (adjust timeout as needed)
            #     wait = WebDriverWait(self.driver, 10)
            #     table = wait.until(EC.presence_of_element_located((By.XPATH, "(//table[@class='ui selectable table sc-kMHJlo jPaBpe'])[1]")))  # Replace 'table-id' with the ID of your table
            #     print("table located")

            #     # Find the row containing the chosen value
            #     rows = table.find_elements(By.TAG_NAME, 'tr')
            #     print(len(rows))
            #     if len(rows)==9:
            #         print("all phases is showing all the devices correctly which is correct")
            #     else:
            #         print("all phases is not showing all the devices correctly which is incorrect")
            #     self.driver.execute_script("window.scrollTo(0, 0);")
            #     time.sleep(3)
            #     print("scrolled the page to top")
            #     self.wait_and_click("(//button[normalize-space()='Phase V'])[1]")
            #     print("clicked on phase 5")
            #     # Wait for the table to load (adjust timeout as needed)
            #     wait = WebDriverWait(self.driver, 10)
            #     table = wait.until(EC.presence_of_element_located((By.XPATH, "(//table[@class='ui selectable table sc-kMHJlo jPaBpe'])[1]")))  # Replace 'table-id' with the ID of your table
            #     print("table located")

            #     # Find the row containing the chosen value
            #     rows = table.find_elements(By.TAG_NAME, 'tr')
            #     print(len(rows))
            #     if len(rows)==5:
            #         print("phase 5 is showing all the devices correctly which is correct")
            #     else:
            #         print("phase 5 is not showing all the devices correctly which is incorrect")

            #     self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            #     # time.sleep(3)
            #     print("scrolled the page to bottom")
            #     try:
            #         jump_to = self.driver.find_element(By.XPATH,"(//input[@placeholder='Jump to page...'])[1]")
            #         print("jump to option is there which is correct")
            #         first_page = self.driver.find_element(By.XPATH, "(//a[normalize-space()='1'])[1]")
            #         icon_class_name = first_page.get_attribute('class')
            #         if 'active' in icon_class_name:
            #             print("first page is coming in focus which is correct")
            #         else:
            #             print("first page is not coming in focus which is incorrect")
            #     except Exception as e:
            #         print("no pagination is there which is incorrect")


            #     self.driver.execute_script("window.scrollTo(0, 0);")
            #     time.sleep(3)
            #     print("scrolled the page to top")

            #     self.wait_and_click("(//button[normalize-space()='Phase I'])[1]")
            #     print("clicked on phase 1")
            #     try:
            #         no_devices = self.driver.find_element(By.XPATH, "(//b[normalize-space()='No devices'])[1]")
            #         print("no devices is showing up in phase 1 which is correct")
            #     except Exception as e:
            #         print("no devices is not showing up in phase 1 which is incorrect")
            #     self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            #     # time.sleep(3)
            #     print("scrolled the page to bottom")
            #     try:
            #         no_devices = self.driver.find_element(By.XPATH, "(//h4[normalize-space()='No Devices Found!'])[1]")
            #         print("no devices is showing up in the table in phase 1 which is correct")
            #     except Exception as e:
            #         print("no devices is not showing up in the table in phase 1 which is incorrect")
            #     self.wait_and_click("(//button[normalize-space()='Filters'])[1]")
            #     print("clicked on filters button")
            #     checkbox = self.driver.find_element(By.XPATH, "(//input[@id='0'])[1]")
            #     self.driver.execute_script("arguments[0].click();", checkbox)
            #     time.sleep(2)
            #     print("clicked on pending approval checkbox")
            #     self.wait_and_click("(//button[normalize-space()='Filters'])[1]")
            #     print("clicked on filters button again to close the dropdown")
            #     try:
            #         no_devices = self.driver.find_element(By.XPATH, "(//h4[normalize-space()='No Devices Found!'])[1]")
            #         print("no devices is showing up in the table for pending approval filter which is correct")
            #     except Exception as e:
            #         print("no devices is not showing up in the table for pending approval filter which is incorrect")
            #     self.wait_and_click("(//i[@id='device-list-add-filters-button'])[1]")
            #     print("clicked on + icon")
            #     checkbox = self.driver.find_element(By.XPATH, "(//input[@id='1'])[1]")
            #     self.driver.execute_script("arguments[0].click();", checkbox)
            #     time.sleep(2)
            #     print("clicked on scheduled checkbox")
            #     self.wait_and_click("(//button[normalize-space()='Filters'])[1]")
            #     print("clicked on filters button")
            #     self.wait_and_click("(//button[normalize-space()='Filters'])[1]")
            #     print("clicked on filters button")
            #     # Wait for the table to load (adjust timeout as needed)
            #     wait = WebDriverWait(self.driver, 10)
            #     table = wait.until(EC.presence_of_element_located((By.XPATH, "(//table[@class='ui selectable table sc-kMHJlo jPaBpe'])[1]")))  # Replace 'table-id' with the ID of your table
            #     print("table located")

            #     # Find the row containing the chosen value
            #     rows = table.find_elements(By.TAG_NAME, 'tr')
            #     if len(rows)==9:
            #         print("all phases is showing all the devices correctly which is correct")
            #     else:
            #         print("all phases is not showing all the devices correctly which is incorrect")
            #     self.wait_and_click("(//i[@class='close icon'])[2]")
            #     print("clicked on close icon")
            #     time.sleep(2)
            #     try:
            #         no_devices = self.driver.find_element(By.XPATH, "(//h4[normalize-space()='No Devices Found!'])[1]")
            #         print("no devices is showing up in the table for pending approval filter which is correct")
            #     except Exception as e:
            #         print("no devices is not showing up in the table for pending approval filter which is incorrect")
            #     try:
            #         jump_to = self.driver.find_element(By.XPATH,"(//input[@placeholder='Jump to page...'])[1]")
            #         print("jump to option is there which is incorrect")
            #         first_page = self.driver.find_element(By.XPATH, "(//a[normalize-space()='1'])[1]")
            #         icon_class_name = first_page.get_attribute('class')
            #         if 'active' in icon_class_name:
            #             print("first page is coming in focus which is correct")
            #         else:
            #             print("first page is not coming in focus which is incorrect")
            #     except Exception as e:
            #         print("no pagination is there which is correct")
            #     self.wait_and_click("(//i[@class='close icon'])[1]")
            #     print("clicked on close icon")
            #     time.sleep(2)
            #     # Wait for the table to load (adjust timeout as needed)
            #     wait = WebDriverWait(self.driver, 10)
            #     table = wait.until(EC.presence_of_element_located((By.XPATH, "(//table[@class='ui selectable table sc-kMHJlo jPaBpe'])[1]")))  # Replace 'table-id' with the ID of your table
            #     print("table located")

            #     # Find the row containing the chosen value
            #     rows = table.find_elements(By.TAG_NAME, 'tr')
            #     if len(rows)==9:
            #         print("all phases is showing all the devices correctly which is correct")
            #     else:
            #         print("all phases is not showing all the devices correctly which is incorrect")
            #     self.wait_and_click("(//button[normalize-space()='Filters'])[1]")
            #     print("clicked on filters button")
            #     checkbox = self.driver.find_element(By.XPATH, "(//input[@id='0'])[1]")
            #     self.driver.execute_script("arguments[0].click();", checkbox)
            #     time.sleep(2)
            #     print("clicked on pending approval checkbox")
            #     self.wait_and_click("(//button[normalize-space()='Filters'])[1]")
            #     print("clicked on filters button")
            #     self.wait_and_click("(//i[@id='device-list-add-filters-button'])[1]")
            #     print("clicked on + icon")
            #     checkbox = self.driver.find_element(By.XPATH, "(//input[@id='1'])[1]")
            #     self.driver.execute_script("arguments[0].click();", checkbox)
            #     time.sleep(2)
            #     print("clicked on pending approval checkbox")
            #     self.wait_and_click("(//button[normalize-space()='Filters'])[1]")
            #     print("clicked on filters button")
            #     self.wait_and_click("(//button[normalize-space()='Filters'])[1]")
            #     print("clicked on filters button")
            #     self.wait_and_click("(//h3[normalize-space()='Clear All'])[1]")
            #     print("clicked on clear all hyperlink")
            #     time.sleep(2)
            #     # Wait for the table to load (adjust timeout as needed)
            #     wait = WebDriverWait(self.driver, 10)
            #     table = wait.until(EC.presence_of_element_located((By.XPATH, "(//table[@class='ui selectable table sc-kMHJlo jPaBpe'])[1]")))  # Replace 'table-id' with the ID of your table
            #     print("table located")

            #     # Find the row containing the chosen value
            #     rows = table.find_elements(By.TAG_NAME, 'tr')
            #     if len(rows)==9:
            #         print("all phases is showing all the devices correctly which is correct")
            #     else:
            #         print("all phases is not showing all the devices correctly which is incorrect")
            #     self.wait_and_click("(//button[normalize-space()='Filters'])[1]")
            #     print("clicked on filters button")
            #     checkbox = self.driver.find_element(By.XPATH, "(//input[@id='0'])[1]")
            #     self.driver.execute_script("arguments[0].click();", checkbox)
            #     time.sleep(2)
            #     print("clicked on pending approval checkbox")
            #     self.wait_and_click("(//button[normalize-space()='Filters'])[1]")
            #     print("clicked on filters button again")
            #     self.wait_and_click("(//i[@id='device-list-add-filters-button'])[1]")
            #     print("clicked on + icon")
            #     checkbox = self.driver.find_element(By.XPATH, "(//input[@id='0'])[1]")
            #     self.driver.execute_script("arguments[0].click();", checkbox)
            #     time.sleep(2)
            #     print("clicked on pending approval checkbox again to deselect")
            #     self.wait_and_click("(//button[normalize-space()='Filters'])[1]")
            #     print("clicked on filters button")
            #     self.wait_and_click("(//button[normalize-space()='Filters'])[1]")
            #     print("clicked on filters button")
            #     time.sleep(2)
            #     # Wait for the table to load (adjust timeout as needed)
            #     wait = WebDriverWait(self.driver, 10)
            #     table = wait.until(EC.presence_of_element_located((By.XPATH, "(//table[@class='ui selectable table sc-kMHJlo jPaBpe'])[1]")))  # Replace 'table-id' with the ID of your table
            #     print("table located")

            #     # Find the row containing the chosen value
            #     rows = table.find_elements(By.TAG_NAME, 'tr')
            #     if len(rows)==9:
            #         print("all phases is showing all the devices correctly which is correct")
            #     else:
            #         print("all phases is not showing all the devices correctly which is incorrect")



                

                
                




                

            # self.driver.execute_script("window.scrollTo(0, 0);")
            # time.sleep(3)
            # print("scrolled the page to top")
            # self.wait_and_click("(//button[normalize-space()='Back'])[1]")
            # print("clicked on back button")
            # if phased=='phased':
            #     self.wait_and_click("(//div[@title='More Options'])[1]")
            #     print("clicked on 3 dots")
            #     self.wait_and_click("(//div[@title='Release Notes'][normalize-space()='Release Notes'])[1]")
            #     print("clicked on release notes icon")
            #     self.wait_and_click("(//button[normalize-space()='Close'])[1]")
            #     print("clicked on close button")
            # else:
            #     self.wait_and_click("(//div[@title='More Options'])[1]")
            #     print("clicked on 3 dots")
            #     payload=self.driver.find_element(By.XPATH,"(//div[@title='Release Notes'][normalize-space()='Release Notes'])[1]")
            #     class_name=payload.get_attribute("class")
            #     if 'disabled' in class_name:
            #         print("release notes is in disabled mode")
            #     else:
            #         print("release notes is in enabled mode which is incorrect")
            #     self.wait_and_click("(//div[@title='More Options'])[1]")
            #     print("clicked on 3 dots")

            # if flag=='rbac' or phased=='non_phased':
            #     try:
            #         self.wait_and_click("(//div[@title='More Options'])[1]")
            #         print("clicked on 3 dots")
            #         approve_action=self.driver.find_element(By.XPATH,"(//div[@title='Approve Action'][normalize-space()='Approve Action'])[1]")
            #         class_name=payload.get_attribute("class")
            #         if 'disabled' in class_name:
            #             print("approve action is in disabled mode which is correct")
            #         else:
            #             print("approve action is in enabled mode which is incorrect")
            #         # time.sleep(2)
            #         print("clicked on approve action which is incorrect")
            #         self.wait_and_click("(//div[@title='More Options'])[1]")
            #         print("clicked on 3 dots")
            #     except Exception as e:
            #         self.wait_and_click("(//div[@title='More Options'])[1]")
            #         print("clicked on 3 dots")
            #         # time.sleep(2)
            #         print("no approve icon which is correct")
            # else:
                
            #     try:
            #         self.wait_and_click("(//div[@title='More Options'])[1]")
            #         print("clicked on 3 dots")
            #         self.wait_and_click("(//div[@title='Approve Action'][normalize-space()='Approve Action'])[1]")
            #         print("clicked on approve action which is incorrect")
            #         queued=self.driver.find_element(By.XPATH,"(//div[@class='ui active indicating progress scheduled'])[1]")
            #         print("the progress bar is scheduled only")
            #         self.wait_and_click("(//div[@title='More Options'])[1]")
            #         print("clicked on 3 dots")
            #         # time.sleep(2)
            #     except Exception as e:
            #         self.wait_and_click("(//div[@title='More Options'])[1]")
            #         print("clicked on 3 dots")
            #         print("the progress bar is not scheduled")


            

            
            # if action_type=='normal_type':
            #     self.wait_and_click("(//div[@title='More Options'])[1]")
            #     print("clicked on 3 dots")
            #     payload=self.driver.find_element(By.XPATH,"(//div[@title='View Payload'][normalize-space()='View Payload'])[1]")
            #     class_name=payload.get_attribute("class")
            #     if 'disabled' in class_name:
            #         print("view payload is in disabled mode")
            #     else:
            #         print("view payload is in enabled mode which is incorrect")
            #     self.wait_and_click("(//div[@title='More Options'])[1]")
            #     print("clicked on 3 dots")
            # else:
            #     self.wait_and_click("(//div[@title='More Options'])[1]")
            #     print("clicked on 3 dots")
            #     self.wait_and_click("(//div[@title='View Payload'][normalize-space()='View Payload'])[1]")
            #     print("clicked on payload icon")
            #     self.wait_and_click("(//button[normalize-space()='OK'])[1]")
            #     print("clicked on ok button")
            
            

            # try:
            #     chart=self.driver.find_element(By.XPATH,"(//*[name()='rect'][@class='nsewdrag drag cursor-pointer'])[1]")
            #     print("the chart is coming correctly")
            #     # time.sleep(2)
            # except Exception as e:
            #     print("the chart is not coming which is incorrect")
            # if flag=='actionsv3' or flag=='rbac':
            #     self.wait_and_click("(//button[normalize-space()='More Info'])[1]")
            #     print('clicked on more info button')
            #     try:
            #         queued=self.driver.find_element(By.XPATH,"(//span[normalize-space()='Action Type'])[1]")
            #         print("the action type is coming correctly")
            #         # time.sleep(2)
            #     except Exception as e:
            #         print("the action type is not coming which is incorrect")

            #     try:
            #         queued=self.driver.find_element(By.XPATH,"(//span[normalize-space()='Action ID'])[1]")
            #         print("the action ID is coming correctly")
            #         # time.sleep(2)
            #     except Exception as e:
            #         print("the action ID is not coming which is incorrect")

            #     try:
            #         queued=self.driver.find_element(By.XPATH,"(//span[normalize-space()='Created At'])[1]")
            #         print("the created at is coming correctly")
            #         # time.sleep(2)
            #     except Exception as e:
            #         print("the created at is not coming which is incorrect")
            #     if phased=='phased':
            #         self.wait_and_click("(//button[normalize-space()='Phase I'])[1]")
            #         print('clicked on phase 1 button')
            #         self.wait_and_click("(//button[normalize-space()='More Info'])[1]")
            #         print('clicked on more info button')
            #         try:
            #             queued=self.driver.find_element(By.XPATH,"(//span[normalize-space()='Action Type'])[1]")
            #             print("the action type is coming correctly")
            #             # time.sleep(2)
            #         except Exception as e:
            #             print("the action type is not coming which is incorrect")

            #         try:
            #             queued=self.driver.find_element(By.XPATH,"(//span[normalize-space()='Action ID'])[1]")
            #             print("the action ID is coming correctly")
            #             # time.sleep(2)
            #         except Exception as e:
            #             print("the action ID is not coming which is incorrect")

            #         try:
            #             queued=self.driver.find_element(By.XPATH,"(//span[normalize-space()='Created At'])[1]")
            #             print("the created at is coming correctly")
            #             # time.sleep(2)
            #         except Exception as e:
            #             print("the created at is not coming which is incorrect")

            #         try:
            #             queued=self.driver.find_element(By.XPATH,"(//span[normalize-space()='Scheduled At'])[1]")
            #             print("the scheduled at is coming correctly")
            #             # time.sleep(2)
            #         except Exception as e:
            #             print("the scheduled at is not coming which is incorrect")
            #     self.wait_and_click("(//button[normalize-space()='View Details'])[1]")
            #     print('clicked on view details button')
            #     self.wait_and_click("(//button[normalize-space()='Back'])[1]")
            #     print('clicked on back button')
            #     self.wait_and_click("(//button[normalize-space()='View Details'])[1]")
            #     print('clicked on view details button')

            #     try:
            #         chart=self.driver.find_element(By.XPATH,"(//*[name()='rect'][@class='nsewdrag drag cursor-pointer'])[1]")
            #         print("the chart is coming correctly")
            #         # time.sleep(2)
            #     except Exception as e:
            #         print("the chart is not coming which is incorrect")
            #     self.wait_and_click("(//button[normalize-space()='More Info'])[1]")
            #     print('clicked on more info button')
            #     try:
            #         queued=self.driver.find_element(By.XPATH,"(//span[normalize-space()='Action Type'])[1]")
            #         print("the action type is coming correctly")
            #         # time.sleep(2)
            #     except Exception as e:
            #         print("the action type is not coming which is incorrect")

            #     try:
            #         queued=self.driver.find_element(By.XPATH,"(//span[normalize-space()='Action ID'])[1]")
            #         print("the action ID is coming correctly")
            #         # time.sleep(2)
            #     except Exception as e:
            #         print("the action ID is not coming which is incorrect")

            #     try:
            #         queued=self.driver.find_element(By.XPATH,"(//span[normalize-space()='Created At'])[1]")
            #         print("the created at is coming correctly")
            #         # time.sleep(2)
            #     except Exception as e:
            #         print("the created at is not coming which is incorrect")
            #     if phased=='phased':
            #         self.wait_and_click("(//button[normalize-space()='Phase I'])[1]")
            #         print('clicked on phase 1 button')
            #         self.wait_and_click("(//button[normalize-space()='More Info'])[1]")
            #         print('clicked on more info button')
            #         try:
            #             queued=self.driver.find_element(By.XPATH,"(//span[normalize-space()='Action Type'])[1]")
            #             print("the action type is coming correctly")
            #             # time.sleep(2)
            #         except Exception as e:
            #             print("the action type is not coming which is incorrect")

            #         try:
            #             queued=self.driver.find_element(By.XPATH,"(//span[normalize-space()='Action ID'])[1]")
            #             print("the action ID is coming correctly")
            #             # time.sleep(2)
            #         except Exception as e:
            #             print("the action ID is not coming which is incorrect")

            #         try:
            #             queued=self.driver.find_element(By.XPATH,"(//span[normalize-space()='Created At'])[1]")
            #             print("the created at is coming correctly")
            #             # time.sleep(2)
            #         except Exception as e:
            #             print("the created at is not coming which is incorrect")

            #         try:
            #             queued=self.driver.find_element(By.XPATH,"(//span[normalize-space()='Scheduled At'])[1]")
            #             print("the scheduled at is coming correctly")
            #             # time.sleep(2)
            #         except Exception as e:
            #             print("the scheduled at is not coming which is incorrect")
            #         self.wait_and_click("(//button[normalize-space()='All Phases'])[1]")
            #         print('clicked on all phases button')
            #     self.wait_and_click("(//i[@title='More details'])[1]")
            #     print("clicked on eye icon")
            #     self.wait_and_click("(//button[normalize-space()='Action Summary'])[1]")
            #     print("clicked on actions summary")

            #     self.wait_and_click("(//i[@title='More details'])[1]")
            #     print("clicked on eye icon")
            #     self.wait_and_click("(//span[normalize-space()='Download Config'])[1]")
            #     print("clicked on download config")
                
            #     self.driver.execute_script("window.scrollTo(0, 0);")
            #     time.sleep(2)
            #     print("scrolled the page to top")
            #     # config_version = self.driver.find_element(By.XPATH, "(//span[contains(text(),'Config Version')])[4]")
            #     # config_version.click()
            #     # time.sleep(3)
            #     # print("clicked on config version")
            #     # close_button = self.driver.find_element(By.XPATH, "(//button[normalize-space()='Close'])[1]")
            #     # close_button.click()
            #     # time.sleep(3)
            #     # print("clicked on close button")
            #     self.wait_and_click("(//span[normalize-space()='Streams'])[1]")
            #     print("clicked on show streams button")
            #     self.wait_and_click("//div[normalize-space()='device_shadow']")
            #     print("clicked on device shadow")
            #     # # pagination
            #     # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            #     # time.sleep(3)
            #     # print("scrolled the page to bottom")
            #     # second_page = self.driver.find_element(By.XPATH, "(//a[normalize-space()='2'])[1]")
            #     # second_page.click()
            #     # time.sleep(5)
            #     # print("clicked on second page")
            #     # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            #     # time.sleep(3)
            #     # print("scrolled the page to bottom")
            #     # forward_one = self.driver.find_element(By.XPATH, "(//a[contains(text(),'⟩')])[1]")
            #     # forward_one.click()
            #     # time.sleep(5)
            #     # print("clicked on forward_one")
                
            #     # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            #     # time.sleep(3)
            #     # print("scrolled the page to bottom")
            #     # forward_last = self.driver.find_element(By.XPATH, "(//a[normalize-space()='»'])[1]")
            #     # forward_last.click()
            #     # time.sleep(5)
            #     # print("clicked on forward_last")
            #     # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            #     # time.sleep(3)
            #     # print("scrolled the page to bottom")
            #     # backward_one = self.driver.find_element(By.XPATH, "(//a[contains(text(),'⟨')])[1]")
            #     # backward_one.click()
            #     # time.sleep(5)
            #     # print("clicked on backward_one")
            #     # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            #     # time.sleep(3)
            #     # print("scrolled the page to bottom")
            #     # backward_last = self.driver.find_element(By.XPATH, "(//a[normalize-space()='«'])[1]")
            #     # backward_last.click()
            #     # time.sleep(5)
            #     # print("clicked on backward_last")
            #     # first_page = self.driver.find_element(By.XPATH, "(//a[normalize-space()='1'])[1]")
            #     # icon_class_name = first_page.get_attribute('class')
            #     # if 'active' in icon_class_name:
            #     #     print("forward to last icon is working successfully")
            #     # else:
            #     #     print("forward to last icon is working")
            #     # self.driver.execute_script("window.scrollTo(0, 0);")
            #     # time.sleep(3)
            #     # print("scrolled the page to top")

            #     # #custom time range
            #     # self.button_clicks(1, "(//i[@class='angle right icon'])[1]")
            #     # time.sleep(5)
            #     # print("clicked on angle right icon")
            #     # try:
            #     #     no_data=self.driver.find_element(By.XPATH,"(//i[@class='info circle big icon'])[1]")
            #     #     print("no data is there which is correct")

            #     # except Exception as e:
            #     #     print("some data is coming")
            #     # time_right_text = self.driver.find_element(By.XPATH, "(//div[@class='ui button selection dropdown'])[1]")
            #     # print(time_right_text.text)
            #     # time.sleep(4)
            #     # print("captured time right text")
            #     # # extracting date and time
                

            #     # # Sample date string
            #     # date_string = time_right_text.text

            #     # # Split the string based on 'to'
            #     # date_parts = date_string.split(' to ')

            #     # # Remove any invalid text from each part
            #     # cleaned_date_parts = [part.strip() for part in date_parts]

            #     # # Convert date strings to datetime objects
            #     # aleft_date_1_before = datetime.strptime(cleaned_date_parts[0], "%y-%m-%d %H:%M:%S")
            #     # aleft_date_2_before = datetime.strptime(cleaned_date_parts[1], "%y-%m-%d %H:%M:%S")

            #     # self.button_clicks(1, "(//i[@class='angle right icon'])[1]")
            #     # time.sleep(5)
            #     # print("clicked on angle right icon")
                
            #     # time_right_text = self.driver.find_element(By.XPATH, "(//div[@class='ui button selection dropdown'])[1]")
            #     # print(time_right_text.text)
            #     # time.sleep(4)
            #     # print("captured time right text")
            #     # # Sample date string
            #     # date_string = time_right_text.text

            #     # # Split the string based on 'to'
            #     # date_parts = date_string.split(' to ')

            #     # # Remove any invalid text from each part
            #     # cleaned_date_parts = [part.strip() for part in date_parts]

            #     # # Convert date strings to datetime objects
            #     # aleft_date_1_after = datetime.strptime(cleaned_date_parts[0], "%y-%m-%d %H:%M:%S")
            #     # aleft_date_2_after = datetime.strptime(cleaned_date_parts[1], "%y-%m-%d %H:%M:%S")
                

            #     # # Compare the dates
            #     # if aleft_date_1_before < aleft_date_1_after and aleft_date_2_before < aleft_date_2_after:
            #     #     print("working as expected")
            #     # else:
            #     #     print("Not working as expected")

            #     # self.button_clicks(1, "(//i[@class='zoom in icon'])[1]")
            #     # time.sleep(5)
            #     # print("clicked on zoom in icon")
            #     # time_zoom_in_text = self.driver.find_element(By.XPATH, "(//div[@class='ui button selection dropdown'])[1]")
            #     # print(time_zoom_in_text.text)
            #     # time.sleep(4)
            #     # print("captured time zoom in text")
            #     # # Sample date string
            #     # date_string = time_zoom_in_text.text

            #     # # Split the string based on 'to'
            #     # date_parts = date_string.split(' to ')

            #     # # Remove any invalid text from each part
            #     # cleaned_date_parts = [part.strip() for part in date_parts]

            #     # # Convert date strings to datetime objects
            #     # azoomin_date_1_after = datetime.strptime(cleaned_date_parts[0], "%y-%m-%d %H:%M:%S")
            #     # azoomin_date_2_after = datetime.strptime(cleaned_date_parts[1], "%y-%m-%d %H:%M:%S")
                

            #     # # Compare the dates
            #     # if aleft_date_1_after < azoomin_date_1_after and azoomin_date_2_after < aleft_date_2_after:
            #     #     print("working as expected")
            #     # else:
            #     #     print("Not working as expected")
            #     # self.button_clicks(1, "(//i[@class='zoom out icon'])[1]")
            #     # time.sleep(5)
            #     # print("clicked on zoom out icon")
            #     # time_zoom_out_text = self.driver.find_element(By.XPATH, "(//div[@class='ui button selection dropdown'])[1]")
            #     # print(time_zoom_out_text.text)
            #     # time.sleep(4)
            #     # print("captured time zoom out text")
            #     # # Sample date string
            #     # date_string = time_zoom_out_text.text

            #     # # Split the string based on 'to'
            #     # date_parts = date_string.split(' to ')

            #     # # Remove any invalid text from each part
            #     # cleaned_date_parts = [part.strip() for part in date_parts]

            #     # # Convert date strings to datetime objects
            #     # azoomout_date_1_after = datetime.strptime(cleaned_date_parts[0], "%y-%m-%d %H:%M:%S")
            #     # azoomout_date_2_after = datetime.strptime(cleaned_date_parts[1], "%y-%m-%d %H:%M:%S")
                

            #     # # Compare the dates
            #     # if azoomout_date_1_after < azoomin_date_1_after and azoomin_date_2_after < azoomout_date_2_after:
            #     #     print("working as expected")
            #     # else:
            #     #     print("Not working as expected")
            #     # self.button_clicks(1, "(//i[@class='angle left icon'])[1]")
            #     # time.sleep(5)
            #     # print("clicked on angle left icon")
            #     # time_left_text = self.driver.find_element(By.XPATH, "(//div[@class='ui button selection dropdown'])[1]")
            #     # print(time_left_text.text)
            #     # time.sleep(4)
            #     # print("captured time left text")
            #     # # Sample date string
            #     # date_string = time_left_text.text

            #     # # Split the string based on 'to'
            #     # date_parts = date_string.split(' to ')

            #     # # Remove any invalid text from each part
            #     # cleaned_date_parts = [part.strip() for part in date_parts]

            #     # # Convert date strings to datetime objects
            #     # aright_date_1_after = datetime.strptime(cleaned_date_parts[0], "%y-%m-%d %H:%M:%S")
            #     # aright_date_2_after = datetime.strptime(cleaned_date_parts[1], "%y-%m-%d %H:%M:%S")
                

            #     # # Compare the dates
            #     # if aright_date_1_after < azoomout_date_1_after and aright_date_2_after < azoomout_date_2_after:
            #     #     print("working as expected")
            #     # else:
            #     #     print("Not working as expected")
            #     # if time_right_text.text!=time_left_text.text or time_zoom_in_text.text!=time_zoom_out_text.text:
            #     #     print("working as expected and the icons are working properly")
            #     # else:
            #     #     print('icons are not working properly')
            #     # last_five = self.driver.find_element(By.XPATH, "(//div[@class='ui button selection dropdown'])[1]")
            #     # last_five.click()
            #     # time.sleep(4)
            #     # print("clicked on last five minutes")
            #     # custom_time = self.driver.find_element(By.XPATH, "(//span[normalize-space()='Custom Time Range'])[1]")
            #     # custom_time.click()
            #     # time.sleep(4)
            #     # print("clicked on custom_time")
            #     # cancel = self.driver.find_element(By.XPATH, "(//button[normalize-space()='Cancel'])[1]")
            #     # cancel.click()
            #     # time.sleep(4)
            #     # print("clicked on cancel button")
            #     # last_five = self.driver.find_element(By.XPATH, "(//div[@class='ui button selection dropdown'])[1]")
            #     # last_five.click()
            #     # time.sleep(4)
            #     # print("clicked on last five minutes")
            #     # custom_time = self.driver.find_element(By.XPATH, "(//span[normalize-space()='Custom Time Range'])[1]")
            #     # custom_time.click()
            #     # time.sleep(4)
            #     # print("clicked on custom_time")

            #     # first_forward = self.driver.find_element(By.XPATH, "(//i[@class='chevron right fitted icon'])[1]")
            #     # first_forward.click()
            #     # time.sleep(4)
            #     # print("clicked on first_forward")
            #     # first_backward = self.driver.find_element(By.XPATH, "(//i[@class='chevron left fitted icon'])[1]")
            #     # first_backward.click()
            #     # time.sleep(4)
            #     # print("clicked on first_backward")
            #     # second_forward = self.driver.find_element(By.XPATH, "(//i[@class='chevron right fitted icon'])[2]")
            #     # second_forward.click()
            #     # time.sleep(4)
            #     # print("clicked on second_forward")
            #     # second_backward = self.driver.find_element(By.XPATH, "(//i[@class='chevron left fitted icon'])[2]")
            #     # second_backward.click()
            #     # time.sleep(4)
            #     # print("clicked on second_backward")

                

            #     # minutes_ago = self.driver.find_element(By.XPATH, "(//div[@id='from_dropdown'])[1]")
            #     # minutes_ago.click()
            #     # time.sleep(4)
            #     # print("clicked on minutes_ago")
                
            #     # thirty_minutes_ago = self.driver.find_element(By.XPATH, "(//span[@class='text'][normalize-space()='30 minutes ago'])[1]")
            #     # thirty_minutes_ago.click()
            #     # time.sleep(4)
            #     # print("clicked on 30 minutes_ago")
                
            #     # input_box = self.driver.find_element(By.XPATH, "(//input[@value='30'])[1]")
            #     # # input_box.send_keys(Keys.COMMAND, "A")
            #     # self.driver.execute_script("arguments[0].value = '';", input_box)
            #     # input_box.send_keys('45')
            #     # time.sleep(3)
            #     # print("entered on input_box")

            #     # seconds_ago = self.driver.find_element(By.XPATH, "(//div[@id='to_dropdown'])[1]")
            #     # seconds_ago.click()
            #     # time.sleep(4)
            #     # print("clicked on seconds_ago")
                
            #     # ten_minutes_ago = self.driver.find_element(By.XPATH, "(//span[@class='text'][normalize-space()='10 minutes ago'])[2]")
            #     # ten_minutes_ago.click()
            #     # time.sleep(4)
            #     # print("clicked on 10 minutes_ago")
                
            #     # input_box = self.driver.find_element(By.XPATH, "(//input[@value='10'])[1]")
            #     # # input_box.send_keys(Keys.COMMAND, "A")
            #     # self.driver.execute_script("arguments[0].value = '';", input_box)
            #     # input_box.send_keys('12')
            #     # time.sleep(3)
            #     # print("entered on input_box")

            #     # toggle = self.driver.find_element(By.XPATH, "(//label[@for='showSaveCustomTimeRangeToggle'])[1]")
            #     # toggle.click()
            #     # time.sleep(3)
            #     # print("clicked on toggle")
            #     # custom_box = self.driver.find_element(By.XPATH, "(//input[@placeholder='Custom Time Range Label'])[1]")
            #     # custom_name = '45 to 12 for {}'.format(random.randint(1,100))
            #     # custom_box.send_keys(custom_name)
            #     # time.sleep(3)
            #     # print("entered on custom_box")
            #     # apply_button = self.driver.find_element(By.XPATH, "(//button[normalize-space()='Apply'])[1]")
            #     # apply_button.click()
            #     # time.sleep(5)
            #     # print("clicked on apply_button")
                
            #     # last_five = self.driver.find_element(By.XPATH, "(//div[@class='ui button selection dropdown'])[1]")
            #     # last_five.click()
            #     # time.sleep(4)
            #     # print("clicked on last five minutes")
            #     # custom_time = self.driver.find_element(By.XPATH, "(//span[normalize-space()='Custom Time Range'])[1]")
            #     # custom_time.click()
            #     # time.sleep(4)
            #     # print("clicked on custom_time")
                
            #     # # nine_text = self.driver.find_element(By.XPATH, "(//span[contains(text(),'9')])[1]")
            #     # # nine_text.click()
            #     # # time.sleep(3)
            #     # # print("clicked on nine_text")

                
            #     # # wait = WebDriverWait(self.driver, 10)
                
            #     # # wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[contains(text(),'9')])[1]"))).click()
            #     # # time.sleep(2)
            #     # # print("clicked on nine_text")

            #     # #new addition
            #     # # Wait for the table to load (adjust timeout as needed)
            #     # wait = WebDriverWait(self.driver, 10)
            #     # table = wait.until(EC.presence_of_element_located((By.XPATH, "(//table[@class='ui celled unstackable center aligned table'])[1]")))  # Replace 'table-id' with the ID of your table
            #     # print("table located")

            #     # # Find the row containing the chosen value
            #     # rows = table.find_elements(By.TAG_NAME, 'tr')
                
            #     # for row in rows:
            #     #     cells = row.find_elements(By.TAG_NAME, 'td')
                    
            #     #     print(cells)
            #     #     for cell in cells:
            #     #         print(cell.text)
            #     #         if cell.text=="14":
                            
                                
                                
            #     #                 span_element = cell.find_element(By.TAG_NAME, 'span')
            #     #                 span_element.click()
            #     #                 print("clicked on cell")
            #     #                 time.sleep(5)
            #     #                 break
            #     #         else:
            #     #                 continue
                            
                            
            #     #     else:
            #     #         continue
            #     #     break


                


                
            #     # nine_o_text = self.driver.find_element(By.XPATH, "(//span[normalize-space()='09:00'])[1]")
            #     # nine_o_text.click()
            #     # time.sleep(3)
            #     # print("clicked on nine_o_text")
                
            #     # nine_o_text = self.driver.find_element(By.XPATH, "(//span[normalize-space()='09:00'])[1]")
            #     # nine_o_text.click()
            #     # time.sleep(3)
            #     # print("clicked on nine_o_text")

            #     # from_input=self.driver.find_element(By.XPATH,"(//input[@id='from_input'])[1]")
            #     # value=from_input.get_attribute('value')
            #     # print(value)
            #     # self.driver.execute_script("arguments[0].value = '';", from_input)
            #     # time.sleep(2)
            #     # from_input.send_keys('18-01-24 09:00:00')
            #     # time.sleep(3)
            #     # print('edited the from input')

                
            #     # # twenty_eight_text = self.driver.find_element(By.XPATH, "(//span[contains(text(),'28')])[2]")
            #     # # twenty_eight_text.click()
            #     # # time.sleep(3)
            #     # # print("clicked on twenty_eight_text")

            #     # #new addition
            #     # # Wait for the table to load (adjust timeout as needed)
            #     # wait = WebDriverWait(self.driver, 10)
            #     # table = wait.until(EC.presence_of_element_located((By.XPATH, "(//table[@class='ui celled unstackable center aligned table'])[2]")))  # Replace 'table-id' with the ID of your table
            #     # print("table located")

            #     # # Find the row containing the chosen value
            #     # rows = table.find_elements(By.TAG_NAME, 'tr')
                
            #     # for row in rows:
            #     #     cells = row.find_elements(By.TAG_NAME, 'td')
                    
            #     #     print(cells)
            #     #     for cell in cells:
            #     #         print(cell.text)
            #     #         if cell.text=="18":
                            
                                
                                
            #     #                 span_element = cell.find_element(By.TAG_NAME, 'span')
            #     #                 span_element.click()
            #     #                 print("clicked on cell")
            #     #                 time.sleep(5)
            #     #                 break
            #     #         else:
            #     #                 continue
                            
                            
            #     #     else:
            #     #         continue
            #     #     break


                

                
            #     # fourteen_text = self.driver.find_element(By.XPATH, "(//span[normalize-space()='14:00'])[1]")
            #     # fourteen_text.click()
            #     # time.sleep(3)
            #     # print("clicked on fourteen_text")
                
            #     # fourteen_text = self.driver.find_element(By.XPATH, "(//span[normalize-space()='14:00'])[1]")
            #     # fourteen_text.click()
            #     # time.sleep(3)
            #     # print("clicked on fourteen_text")

            #     # to_input=self.driver.find_element(By.XPATH,"(//input[@id='to_input'])[1]")
            #     # value=to_input.get_attribute('value')
            #     # print(value)
            #     # self.driver.execute_script("arguments[0].value = '';", to_input)
            #     # time.sleep(2)
            #     # to_input.send_keys('23-01-24 14:00:00')
            #     # time.sleep(3)
            #     # print('edited the to input')

            #     # toggle = self.driver.find_element(By.XPATH, "(//label[@for='showSaveCustomTimeRangeToggle'])[1]")
            #     # toggle.click()
            #     # time.sleep(3)
            #     # print("clicked on toggle")
            #     # apply_button = self.driver.find_element(By.XPATH, "(//button[normalize-space()='Apply'])[1]")
            #     # apply_button.click()
            #     # time.sleep(2)
            #     # print("clicked on apply_button")
            #     # toast_message = self.driver.find_element(By.XPATH, "(//div[@class='toast toast-error'])[1]")
            #     # print(toast_message.text)
            #     # time.sleep(5)
            #     # custom_box = self.driver.find_element(By.XPATH, "(//input[@placeholder='Custom Time Range Label'])[1]")
            #     # custom_name = 'new_custom{}'.format(random.randint(1,100))
            #     # custom_box.send_keys(custom_name)
            #     # time.sleep(3)
            #     # print("entered on custom_box")
            #     # apply_button = self.driver.find_element(By.XPATH, "(//button[normalize-space()='Apply'])[1]")
            #     # apply_button.click()
            #     # time.sleep(5)
            #     # print("clicked on apply_button")

            #     # last_five = self.driver.find_element(By.XPATH, "(//div[@class='ui button selection dropdown'])[1]")
            #     # last_five.click()
            #     # time.sleep(4)
            #     # print("clicked on last five minutes")
            #     # custom_time = self.driver.find_element(By.XPATH, "(//span[normalize-space()='Custom Time Range'])[1]")
            #     # custom_time.click()
            #     # time.sleep(4)
            #     # print("clicked on custom_time")
            #     # toggle = self.driver.find_element(By.XPATH, "(//label[@for='showSaveCustomTimeRangeToggle'])[1]")
            #     # toggle.click()
            #     # time.sleep(3)
            #     # print("clicked on toggle")
            #     # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            #     # time.sleep(3)
            #     # print("scrolled the page to bottom")
            #     # delete_custom_name = custom_name+'_delete'
            #     # print(delete_custom_name)
            #     # close_icon = self.driver.find_element(By.XPATH, "(//i[@id='{}'])[1]".format(delete_custom_name))
            #     # close_icon.click()
            #     # time.sleep(3)
            #     # print("clicked on close_icon")
            #     # cancel_custom_name = custom_name+'_cancel'

            #     # second_close_icon = self.driver.find_element(By.XPATH, "(//i[@id='{}'])[1]".format(cancel_custom_name))
            #     # second_close_icon.click()
            #     # time.sleep(3)
            #     # print("clicked on second_close_icon")

            #     # delete_custom_name = custom_name+'_delete'
            #     # close_icon = self.driver.find_element(By.XPATH, "(//i[@id='{}'])[1]".format(delete_custom_name))
            #     # close_icon.click()
            #     # time.sleep(3)
            #     # print("clicked on close_icon")

            #     # confirm_custom_name = custom_name+'_confirm'

            #     # second_close_icon = self.driver.find_element(By.XPATH, "(//i[@id='{}'])[1]".format(confirm_custom_name))
            #     # second_close_icon.click()
            #     # time.sleep(3)
            #     # print("clicked on second_close_icon")
            #     # self.button_clicks(1, "(//button[normalize-space()='Cancel'])[1]")
            #     # time.sleep(5)
            #     # print("clicked on cancel")
            #     self.wait_and_click("(//button[@type='submit'])[1]")
            #     print("clicked on download button")
            #     self.wait_and_click("(//button[normalize-space()='Refresh'])[1]")
            #     print("clicked on refresh button")
            #     self.wait_and_click("(//button[normalize-space()='Back'])[1]")
            #     print("clicked on back button")
            #     self.wait_and_click("(//button[normalize-space()='Close'])[1]")
            #     print("clicked on close button")
            #     self.wait_and_click("(//span[normalize-space()='Streams'])[1]")
            #     print("clicked on show streams button")
            #     try:
                    
            #         self.wait_and_click("(//div[normalize-space()='uplink_serializer_metrics'])[1]")
            #         print("clicked on streams bool")
            #         try:
            #             no_data=self.driver.find_element(By.XPATH,"(//i[@class='info circle big icon'])[1]")
            #             print("no data is there which is correct")

            #         except Exception as e:
            #             print("some data is coming")
                    
            #     except Exception as e:
            #         print("that stream is not present")
            #     self.wait_and_click("(//button[normalize-space()='Close'])[1]")
            #     print("clicked on close button")
            #     self.wait_and_click("(//span[normalize-space()='Device Dashboards'])[1]")
            #     print("clicked on device dashboards button")
            #     self.wait_and_click("(//button[normalize-space()='Close'])[1]")
            #     print("clicked on close button")
            #     self.wait_and_click("(//span[normalize-space()='Device Dashboards'])[1]")
            #     print("clicked on device dashboards button")
            #     # dev_dash = self.driver.find_element(By.XPATH, "(//label[normalize-space()='Vehicle Dashboard'])[1]")
            #     # dev_dash.click()
            #     # time.sleep(15)
            #     # print("selected dashboard")
            #     self.wait_and_click("(//button[normalize-space()='Close'])[1]")
            #     print("clicked on close button")
            #     # title_dash=self.driver.find_element(By.XPATH,"(//span[@class='dashboard-title'])[1]")
            #     # print(title_dash.text)
            #     # if "Vehicle Dashboard" in title_dash.text:
            #     #     print("working correctly")
            #     # else:
            #     #     print("not working correctly")
            #     if flag=='rbac':
            #         try:
            #             self.wait_and_click("(//span[normalize-space()='Logs'])[1]")
            #             print('clicked on logs button which is incorrect')
            #         except Exception as e:
            #             print("logs button is not available which is correct")
            #     else:

            #         self.wait_and_click("(//span[normalize-space()='Logs'])[1]")
            #         print('clicked on logs button')
            #     try:
            #         queued=self.driver.find_element(By.XPATH,"(//td[contains(text(),'Queued')])[1]")
            #         # time.sleep(2)
            #         print('queued text is there')
            #     except Exception as e:
            #         print('queued text is not there')
            #         # time.sleep(2)
            #     if phased=='phased':
            #         self.wait_and_click("(//label[@id='sortByIncompleteActions'])[1]")
            #         print("clicked on sort by incomplete actions")
            #         try:
            #             queued=self.driver.find_element(By.XPATH,"(//td[contains(text(),'Completed')])[1]")
            #             # time.sleep(2)
            #             print('completed text is there which is incorrect')
            #         except Exception as e:
            #             print('completed text is not there which is correct')
            #             # time.sleep(2)
            #         self.wait_and_click("(//button[normalize-space()='Mark All Complete'])[1]")
            #         print('clicked on mark all as complete button')
            #         confirm_disabled=self.driver.find_element(By.XPATH,"(//button[normalize-space()='Confirm'])[1]")
            #         class_name=confirm_disabled.get_attribute('class')
            #         if 'disabled' in class_name:
            #             print("confirm button is in disabled mode")
            #         else:
            #             print('confirm button is in enabled mode which is incorrect')
            #         self.wait_and_click("(//button[normalize-space()='Cancel'])[1]")
            #         print("clicked on cancel button")
                
            #         self.wait_and_click("(//button[normalize-space()='Mark All Complete'])[1]")
            #         print('clicked on mark all as complete button')
            #         field=self.driver.find_element(By.XPATH,"(//input[@type='text'])[1]")
            #         field.send_keys("Yes")
            #         time.sleep(2)
            #         print('entered the text')
            #         self.wait_and_click("(//button[normalize-space()='Confirm'])[1]")
            #         print('clicked on confirm button')
            #         try:
            #             queued=self.driver.find_element(By.XPATH,"(//td[contains(text(),'Queued')])[1]")
            #             # time.sleep(2)
            #             print('queued text is there which is incorrect')
            #         except Exception as e:
            #             print('queued text is not there which is correct')
            #             # time.sleep(2)
            #         try:
            #             queued=self.driver.find_element(By.XPATH,"(//button[normalize-space()='Mark All Complete'])[1]")
            #             # time.sleep(2)
            #             print('mark all complete button is there which is incorrect')
            #         except Exception as e:
            #             print('mark all complete button is not there which is correct')
            #             # time.sleep(2)
            #         try:
            #             queued=self.driver.find_element(By.XPATH,"(//h3[normalize-space()='No actions found!'])[1]")
            #             # time.sleep(2)
            #             print('No actions found text is there which is correct')
            #         except Exception as e:
            #             print('No actions found text is not there which is incorrect')
            #             # time.sleep(2)
            #         self.wait_and_click("(//label[@id='sortByIncompleteActions'])[1]")
            #         print("clicked on sort by incomplete actions again to disable it")
            #         # Wait for the table to load (adjust timeout as needed)
            #         wait = WebDriverWait(self.driver, 10)
            #         table = wait.until(EC.presence_of_element_located((By.XPATH, "(//table[@class='ui selectable sortable table sc-fRkCxR kaRnyH'])[1]")))  # Replace 'table-id' with the ID of your table
            #         print("table located")

            #         # Find the row containing the chosen value
            #         rows = table.find_elements(By.TAG_NAME, 'tr')
            #         if len(rows)>1:
            #             print("data is showing up which is correct")
            #         else:
            #             print("data is not showing up which is incorrect")

            #         payload=self.driver.find_element(By.XPATH,"(//i[@title='Mark Action as completed'])[1]")
            #         class_name=payload.get_attribute("class")
            #         if 'disabled' in class_name:
            #             print("mark action icon is in disabled mode")
            #         else:
            #             print("mark action icon is in enabled mode which is incorrect")
            #         self.wait_and_click("(//i[@title='View Payload'])[1]")
            #         print("clicked on payload icon")
            #         self.wait_and_click("(//button[normalize-space()='OK'])[1]")
            #         print("clicked on ok button")
            #         self.driver.execute_script("window.scrollTo(0, 0);")
            #         # time.sleep(3)
            #         print("scrolled the page to top")
            #         self.wait_and_click("(//button[normalize-space()='Action Summary'])[1]")
            #         print("clicked on actions summary")
            #         first_page_action_id = self.driver.find_element(By.XPATH,"(//table[@class='ui selectable table sc-kMHJlo jPaBpe'])[1]//tr[1]/td[3]")
            #         first_page_action_id_text=first_page_action_id.text
            #         if first_page_action_id_text=="Completed":
            #             print("Action is completed for that device which is correct")
            #         else:
            #             print("Action is not completed for that device which is incorrect")
            #         first_page_action_id = self.driver.find_element(By.XPATH,"(//table[@class='ui selectable table sc-kMHJlo jPaBpe'])[1]//tr[2]/td[3]")
            #         first_page_action_id_text=first_page_action_id.text
            #         if first_page_action_id_text=="Scheduled":
            #             print("Action is scheduled for that device which is correct")
            #         else:
            #             print("Action is not scheduled for that device which is incorrect")
            #         self.wait_and_click("(//i[@title='More details'])[2]")
            #         print("clicked on eye icon")
            #         try:
            #             self.wait_and_click("(//i[@title='Mark Action as completed'])[1]")
            #             print("clicked on mark action as completed")
                        
            #             confirm_disabled=self.driver.find_element(By.XPATH,"(//button[normalize-space()='Confirm'])[1]")
            #             class_name=confirm_disabled.get_attribute('class')
            #             if 'disabled' in class_name:
            #                 print("confirm button is in disabled mode")
            #             else:
            #                 print('confirm button is in enabled mode which is incorrect')
            #             self.wait_and_click("(//button[normalize-space()='Cancel'])[1]")
            #             print("clicked on cancel button")
            #             id_element=self.driver.find_element(By.XPATH,"/html[1]/body[1]/div[2]/div[2]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[1]")
            #             id=id_element.text
            #             # time.sleep(3)
            #             self.wait_and_click("(//i[@title='Mark Action as completed'])[1]")
            #             print("clicked on mark action as completed")
                        
            #             field=self.driver.find_element(By.XPATH,"(//input[@type='text'])[1]")
            #             field.send_keys(id)
            #             time.sleep(2)
            #             print('entered the text')
            #             self.wait_and_click("(//button[normalize-space()='Confirm'])[1]")
            #             print('clicked on confirm button')
            #         except Exception as e:
            #             print("it's already become completed by default")

                

                
            #     self.driver.execute_script("window.scrollTo(0, 0);")
            #     # time.sleep(3)
            #     print("scrolled the page to top")
            #     self.wait_and_click("(//button[normalize-space()='Action Summary'])[1]")
            #     print("clicked on actions summary")
            #     self.wait_and_click("(//button[normalize-space()='Back'])[1]")
            #     print("clicked on back button")

            #     try:
            #         self.wait_and_click("(//div[@title='More Options'])[1]")
            #         print("clicked on 3 dots")
            #         self.wait_and_click("(//div[@title='Mark Action as completed'][normalize-space()='Mark Action as completed'])[1]")
            #         print("clicked on mark action as completed")
                    
            #         confirm_disabled=self.driver.find_element(By.XPATH,"(//button[normalize-space()='Confirm'])[1]")
            #         class_name=confirm_disabled.get_attribute('class')
            #         if 'disabled' in class_name:
            #             print("confirm button is in disabled mode")
            #         else:
            #             print('confirm button is in enabled mode which is incorrect')
            #         self.wait_and_click("(//button[normalize-space()='Cancel'])[1]")
            #         print("clicked on cancel button")
            #         id_element=self.driver.find_element(By.XPATH,"/html[1]/body[1]/div[2]/div[2]/div[3]/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[1]")
            #         id=id_element.text
            #         # time.sleep(3)
            #         self.wait_and_click("(//i[@title='Mark Action as completed'])[1]")
            #         print("clicked on mark action as completed")
                    
            #         field=self.driver.find_element(By.XPATH,"(//input[@type='text'])[1]")
            #         field.send_keys(id)
            #         time.sleep(2)
            #         print('entered the text')
            #         self.wait_and_click("(//button[normalize-space()='Confirm'])[1]")
            #         print('clicked on confirm button')
            #     except Exception as e:
            #         self.wait_and_click("(//div[@title='More Options'])[1]")
            #         print("clicked on 3 dots")
            #         # time.sleep(2)
            #         print("it's already become completed by default")
            #     try:
            #         queued=self.driver.find_element(By.XPATH,"(//div[@class='ui progress completed'])[1]")
            #         print("the progress bar is completed only")
            #         # time.sleep(2)
            #     except Exception as e:
            #         print("the progress bar is not completed")

            #     self.wait_and_click("(//i[@title='More details'])[1]")
            #     print("clicked on eye icon")
            #     self.wait_and_click("(//i[@title='More details'])[1]")
            #     print("clicked on eye icon")

            #     if flag=='rbac':
            #         print("no remote shell option which is correct for rbac")
            #     else:
            #         self.wait_and_click("(//span[normalize-space()='Remote Shell'])[1]")
            #         print("clicked on remote shell")
            #         # self.button_clicks(1,"(//i[@class='blue expand link icon'])[1]")
            #         # time.sleep(3)
            #         # print("clicked on expand to full screen icon")
            #         # self.button_clicks(1,"(//i[@class='yellow compress link icon'])[1]")
            #         # time.sleep(3)
            #         # print("clicked on minimize icon")
            #         self.wait_and_click("(//button[normalize-space()='Cancel'])[1]")
            #         print("clicked on cancel button")
                

                


            #     self.wait_and_click("(//span[normalize-space()='Deactivate'])[1]")
            #     print('clicked on deactivate button')
            #     self.wait_and_click("(//button[normalize-space()='Cancel'])[1]")
            #     print('clicked on cancel button')

            #     self.wait_and_click("(//span[normalize-space()='Deactivate'])[1]")
            #     print('clicked on deactivate button')
            #     self.wait_and_click("(//button[normalize-space()='Deactivate Device'])[1]")
            #     print('clicked on deactivate device button')

            #     self.wait_and_click("(//span[normalize-space()='Activate'])[1]")
            #     print('clicked on activate button')
            #     self.wait_and_click("(//button[normalize-space()='Cancel'])[1]")
            #     print('clicked on cancel button')
            #     self.wait_and_click("(//span[normalize-space()='Activate'])[1]")
            #     print('clicked on activate button')
            #     self.wait_and_click("(//button[normalize-space()='Activate Device'])[1]")
            #     print('clicked on activate device button')
                

            #     self.driver.execute_script("window.scrollTo(0, 0);")
            #     # time.sleep(3)
            #     print("scrolled the page to top")
            #     self.wait_and_click("(//button[normalize-space()='Action Summary'])[1]")
            #     print("clicked on actions summary")


            #     # pagination
                
            #     self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            #     # time.sleep(2)
            #     print("scrolled the page to bottom")
            #     forward_one = self.driver.find_element(By.LINK_TEXT, "⟩")
            #     forward_one.click()
            #     time.sleep(2)
            #     print("clicked on forward_one")
            #     self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            #     # time.sleep(2)
            #     print("scrolled the page to bottom")
            #     forward_last = self.driver.find_element(By.LINK_TEXT, "»")
            #     forward_last.click()
            #     time.sleep(2)
            #     print("clicked on forward_last")
            #     self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            #     # time.sleep(2)
            #     print("scrolled the page to bottom")
            #     backward_one = self.driver.find_element(By.LINK_TEXT, "⟨")
            #     backward_one.click()
            #     time.sleep(2)
            #     print("clicked on backward_one")
            #     self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            #     # time.sleep(2)
            #     print("scrolled the page to bottom")
            #     backward_last = self.driver.find_element(By.LINK_TEXT, "«")
            #     backward_last.click()
            #     time.sleep(2)
            #     print("clicked on backward_last")
            #     self.driver.execute_script("window.scrollTo(0, 0);")
            #     # time.sleep(2)
            #     print("scrolled the page to top")

            #     jump_to = self.driver.find_element(By.XPATH, "(//input[@placeholder='Jump to page...'])[1]")
            #     jump_to.send_keys("7")
            #     # time.sleep(2)
            #     jump_to.send_keys(Keys.RETURN)
            #     time.sleep(2)
            #     print("clicked on jump to")
                
            #     # self.driver.execute_script("arguments[0].value = '';", jump_to)
            #     # time.sleep(3)
                
            #     # self.driver.execute_script("arguments[0].value = '';", jump_to)
            #     # time.sleep(3)
            #     jump_to = self.driver.find_element(By.XPATH, "(//input[@placeholder='Jump to page...'])[1]")
            #     jump_to.send_keys("23456")
            #     # time.sleep(2)
            #     jump_to.send_keys(Keys.RETURN)
            #     time.sleep(2)
            #     # self.driver.execute_script("arguments[0].value = '';", jump_to)
            #     # time.sleep(3)
            #     # self.driver.refresh()
            #     # time.sleep(3)
            #     self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            #     # time.sleep(2)
            #     print("scrolled the page to bottom")
            #     jump_to = self.driver.find_element(By.XPATH, "(//input[@placeholder='Jump to page...'])[1]")
            #     jump_to.send_keys("0")
            #     # time.sleep(2)
            #     jump_to.send_keys(Keys.RETURN)
            #     time.sleep(2)
            #     try:

            #         first_page = self.driver.find_element(By.XPATH, "(//a[normalize-space()='1'])[1]")
            #         icon_class_name = first_page.get_attribute('class')
            #         if 'active' in icon_class_name:
            #             print("moved to first page successfully")
            #         else:
            #             print("Not moved to first page")
            #     except Exception as e:
            #         print("not showing the first page which is incorrect")

            #     jump_to = self.driver.find_element(By.XPATH, "(//input[@placeholder='Jump to page...'])[1]")
            #     jump_to.send_keys("-1")
            #     # time.sleep(2)
            #     jump_to.send_keys(Keys.RETURN)
            #     time.sleep(2)
            #     toast_message = self.driver.find_element(By.XPATH, "(//div[@role='status'])[1]")
            #     print(toast_message.text)
            #     # time.sleep(2)



            #     operator = self.driver.find_element(By.XPATH, "(//i[@class='dropdown icon'])[2]")
            #     operator.click()
            #     time.sleep(2)
            #     option_locator = "(//span[normalize-space()='25'])[1]"
            #     option = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, option_locator)))
            #     option.click()
                
            #     time.sleep(2)
            #     print("entered devices per page")
            #     self.driver.execute_script("window.scrollTo(0, 0);")
            #     # time.sleep(2)
            #     print("scrolled the page to top")
            # else:
            #     print("not the actionsv3 module")

        except Exception as e:
            file_name = 'phased_actions.png'
            directory_path = 'Screenshots'
            if not os.path.exists(directory_path):
                os.makedirs(directory_path)
            file_path = os.path.abspath(os.path.join(directory_path, file_name))
            self.driver.get_screenshot_as_file(file_path)
            pytest.record_property("screenshot", file_path)  # Record the screenshot path in the report
            self.driver.refresh()
            time.sleep(10)
            print('refreshed the page')
            
            
            self.driver.execute_script("window.scrollTo(0, 0);")
            time.sleep(3)
            print("scrolled the page to top")
            raise e
    def wait_and_send_keys(self,element_xpath, keys):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, element_xpath))).send_keys(keys)
    
    def line_chart(self,dashboard_type):
        #Line chart
        self.wait_and_click("(//button[@class='ui button add-panel-button'])[1]")
        print("clicked on line chart option")


        no_data=self.driver.find_element(By.XPATH,"(//div[@class='panel-no-data'])[1]")
        print('no data on the panel')
        #   time.sleep(3)
        untitled=self.driver.find_element(By.XPATH,"(//div[@class='bytebeam-panel-title'])[1]")
        print(untitled.text)
        if 'Untitled' in untitled.text:
                print('untitled text is there which is correct')
        else:
                print('untitled text is not there which is incorrect')
        if dashboard_type=='device':
            column_disabled=self.driver.find_element(By.XPATH,"(//div[@role='combobox'])[2]")
            class_name=column_disabled.get_attribute('class')
            if 'disabled' in class_name:
                    print('column dropdown is disabled which is correct')
            else:
                    print('column dropdown is enabled which is incorrect')
            

            operator_disabled=self.driver.find_element(By.XPATH,"(//div[@role='combobox'])[3]")
            class_name=operator_disabled.get_attribute('class')
            if 'disabled' in class_name:
                    print('operator dropdown is disabled which is correct')
            else:
                    print('operator dropdown is enabled which is incorrect')

            advanced_disabled=self.driver.find_element(By.XPATH,"(//button[normalize-space()='Advanced'])[1]")
            class_name=advanced_disabled.get_attribute('class')
            if 'disabled' in class_name:
                    print('advanced button is disabled which is correct')
            else:
                    print('advanced button is enabled which is incorrect')
            self.button_clicks(1, "(//button[normalize-space()='Submit'])[1]")
            time.sleep(2)
            toast_message = self.driver.find_element(By.XPATH, "(//div[@role='status'])[1]")
            print(toast_message.text)
            #   time.sleep(5)
            self.wait_and_send_keys("(//input[@placeholder='Title'])[1]","LINE CHART@123")
            print("entered line chart title")
            untitled=self.driver.find_element(By.XPATH,"(//div[@class='bytebeam-panel-title'])[1]")
            print(untitled.text)
            if 'LINE CHART@123' in untitled.text:
                    print('LINE CHART@123 text is there which is correct')
            else:
                    print('LINE CHART@123 text is not there which is incorrect')
            
            self.wait_and_send_keys("(//input[@placeholder='Description'])[1]","Description@123")
            print("entered line chart description")
            self.wait_and_send_keys("(//input[@type='text'])[1]","device_shadow" + Keys.RETURN)
            print("entered stream")
            operator_disabled=self.driver.find_element(By.XPATH,"(//div[@role='combobox'])[3]")
            class_name=operator_disabled.get_attribute('class')
            if 'disabled' in class_name:
                    print('operator dropdown is still disabled which is correct')
            else:
                    print('operator dropdown is still enabled which is incorrect')

            self.wait_and_send_keys("(//input[@type='text'])[2]","range" + Keys.RETURN)
            print("entered column")
            self.wait_and_send_keys("(//input[@type='text'])[3]","sum" + Keys.RETURN)
            print("entered aggregator")
            
            try:
                histo_preview=self.driver.find_element(By.XPATH,"(//*[name()='rect'][@class='nsewdrag drag'])[1]")
                #  time.sleep(3)
                print("preview is coming with data")
            except Exception as e:
                print("preview is not coming with data")
        else:
            column_disabled=self.driver.find_element(By.XPATH,"(//div[@role='combobox'])[4]")
            class_name=column_disabled.get_attribute('class')
            if 'disabled' in class_name:
                    print('column dropdown is disabled which is correct')
            else:
                    print('column dropdown is enabled which is incorrect')
            

            operator_disabled=self.driver.find_element(By.XPATH,"(//div[@role='combobox'])[5]")
            class_name=operator_disabled.get_attribute('class')
            if 'disabled' in class_name:
                    print('operator dropdown is disabled which is correct')
            else:
                    print('operator dropdown is enabled which is incorrect')

            advanced_disabled=self.driver.find_element(By.XPATH,"(//button[normalize-space()='Advanced'])[1]")
            class_name=advanced_disabled.get_attribute('class')
            if 'disabled' in class_name:
                    print('advanced button is disabled which is correct')
            else:
                    print('advanced button is enabled which is incorrect')
            self.button_clicks(1, "(//button[normalize-space()='Submit'])[1]")
            time.sleep(2)
            toast_message = self.driver.find_element(By.XPATH, "(//div[@role='status'])[1]")
            print(toast_message.text)
            #   time.sleep(5)
            self.wait_and_send_keys("(//input[@placeholder='Title'])[1]","LINE CHART@123")
            print("entered line chart title")
            untitled=self.driver.find_element(By.XPATH,"(//div[@class='bytebeam-panel-title'])[1]")
            print(untitled.text)
            if 'LINE CHART@123' in untitled.text:
                    print('LINE CHART@123 text is there which is correct')
            else:
                    print('LINE CHART@123 text is not there which is incorrect')
            
            self.wait_and_send_keys("(//input[@placeholder='Description'])[1]","Description@123")
            print("entered line chart description")
            self.wait_and_send_keys("(//input[@type='text'])[3]","device_shadow" + Keys.RETURN)
            print("entered stream")
            operator_disabled=self.driver.find_element(By.XPATH,"(//div[@role='combobox'])[3]")
            class_name=operator_disabled.get_attribute('class')
            if 'disabled' in class_name:
                    print('operator dropdown is still disabled which is correct')
            else:
                    print('operator dropdown is still enabled which is incorrect')

            self.wait_and_send_keys("(//input[@type='text'])[4]","range" + Keys.RETURN)
            print("entered column")
            self.wait_and_send_keys("(//input[@type='text'])[5]","sum" + Keys.RETURN)
            print("entered aggregator")
            
            try:
                histo_preview=self.driver.find_element(By.XPATH,"(//*[name()='rect'][@class='nsewdrag drag'])[1]")
                #  time.sleep(3)
                print("preview is coming with data")
            except Exception as e:
                print("preview is not coming with data")
             
        # self.button_clicks(1, "(//button[normalize-space()='Advanced'])[1]")
        # time.sleep(5)
        # print("clicked on advanced button")
        # self.button_clicks(1,"(//button[normalize-space()='Cancel'])[1]")
        # time.sleep(3)
        # print("clcked on cancel button")
        # self.button_clicks(1, "(//button[normalize-space()='Advanced'])[1]")
        # time.sleep(5)
        # print("clicked on advanced button")
        # operator_disabled=self.driver.find_element(By.XPATH,"(//div[@class='ui disabled fluid selection dropdown'])[1]")
        # class_name=operator_disabled.get_attribute('class')
        # if 'disabled' in class_name:
        #      print('operator dropdown is still disabled which is correct')
        # else:
        #      print('operator dropdown is still enabled which is incorrect')
        # value_disabled=self.driver.find_element(By.XPATH,"(//div[@class='ui disabled input'])[1]")
        # class_name=value_disabled.get_attribute('class')
        # if 'disabled' in class_name:
        #      print('operator dropdown is still disabled which is correct')
        # else:
        #      print('operator dropdown is still enabled which is incorrect')
        

        # field = self.driver.find_element(By.XPATH, "(//input[@type='text'])[8]")
        # field.send_keys("range")
        # field.send_keys(Keys.RETURN)
        # time.sleep(3)
        # print("entered field")
        # operator = self.driver.find_element(By.XPATH, "(//div[contains(text(),'=')])[1]")
        # operator.click()
        # time.sleep(3)
        # option_locator = "(//span[@class='text'][normalize-space()='>'])[1]"
        # option = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, option_locator)))
        # option.click()
        
        # time.sleep(5)
        # print("entered operator type")
        
        # value = self.driver.find_element(By.XPATH, "(//input[@placeholder='Value'])[1]")
        # value.send_keys(55000)
        # time.sleep(3)
        # print("entered value")
        # self.button_clicks(1, "(//span[normalize-space()='Clear Filter'])[1]")
        # time.sleep(5)
        # print("clicked on clear filter")
        # operator_disabled=self.driver.find_element(By.XPATH,"(//div[@class='ui disabled fluid selection dropdown'])[1]")
        # class_name=operator_disabled.get_attribute('class')
        # if 'disabled' in class_name:
        #      print('operator dropdown is still disabled which is correct')
        # else:
        #      print('operator dropdown is still enabled which is incorrect')
        # field = self.driver.find_element(By.XPATH, "(//input[@type='text'])[8]")
        # field.send_keys("range")
        # field.send_keys(Keys.RETURN)
        # time.sleep(3)
        # print("entered field")
        # operator = self.driver.find_element(By.XPATH, "(//div[contains(text(),'=')])[1]")
        # operator.click()
        # time.sleep(3)
        # option_locator = "(//span[@class='text'][normalize-space()='>'])[1]"
        # option = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, option_locator)))
        # option.click()
        
        # time.sleep(5)
        # print("entered operator type")
        # value = self.driver.find_element(By.XPATH, "(//input[@placeholder='Value'])[1]")
        # value.send_keys(55000)
        # time.sleep(3)
        # print("entered value")
        # self.button_clicks(1, "(//div[@role='alert'][normalize-space()='Add Filter Rule'])[1]")
        # time.sleep(3)
        # print("clicked on add filter rule")
        # self.button_clicks(1, "(//div[@role='option'][normalize-space()='Add Filter Rule'])[1]")
        # time.sleep(3)
        # print("clicked on add filter rule")
        # field = self.driver.find_element(By.XPATH, "(//input[@type='text'])[10]")
        # field.send_keys("mode")
        # field.send_keys(Keys.RETURN)
        # time.sleep(3)
        # print("entered field")
        # operator = self.driver.find_element(By.XPATH, "(//div[contains(text(),'=')])[1]")
        # operator.click()
        # time.sleep(3)
        # option_locator = "(//span[@class='text'][normalize-space()='='])[2]"
        # option = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, option_locator)))
        # option.click()
        
        # time.sleep(5)
        # print("entered operator type")
        # value = self.driver.find_element(By.XPATH, "(//input[@placeholder='Value'])[2]")
        # value.send_keys("on")
        # time.sleep(3)
        # print("entered value")
        # three_dots = self.driver.find_element(By.XPATH, "(//i[@class='ellipsis horizontal icon'])[2]")
        # three_dots.click()
        # time.sleep(3)
        # print("clicked on 3 dots")
        # self.button_clicks(1, "(//div[@role='option'][normalize-space()='Duplicate'])[2]")
        # time.sleep(3)
        # print("clicked on duplicate option")
        # field = self.driver.find_element(By.XPATH, "(//input[@type='text'])[12]")
        # field.send_keys("range")
        # field.send_keys(Keys.RETURN)
        # time.sleep(3)
        # print("entered field")
        # operator = self.driver.find_element(By.XPATH, "(//div[contains(text(),'=')])[2]")
        # operator.click()
        # time.sleep(3)
        # option_locator = "(//span[@class='text'][normalize-space()='<'])[2]"
        # option = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, option_locator)))
        # option.click()
        
        # time.sleep(5)
        # print("entered operator type")
        # value = self.driver.find_element(By.XPATH, "(//input[@placeholder='Value'])[3]")
        # value.send_keys("60000")
        # time.sleep(3)
        # print("entered value")
        # three_dots = self.driver.find_element(By.XPATH, "(//i[@class='ellipsis horizontal icon'])[3]")
        # three_dots.click()
        # time.sleep(3)
        # print("clicked on 3 dots")
        # self.button_clicks(1, "(//div[@role='option'][normalize-space()='Remove'])[3]")
        # time.sleep(3)
        # print("clicked on remove button")

        # groupby_field = self.driver.find_element(By.XPATH, "(//input[@type='text'])[12]")
        # groupby_field.send_keys("mode")
        # groupby_field.send_keys(Keys.RETURN)
        # time.sleep(3)
        # groupby_field.send_keys("Status")
        # groupby_field.send_keys(Keys.RETURN)
        # time.sleep(3)
        # groupby_field.send_keys("firmware_version")
        # groupby_field.send_keys(Keys.RETURN)
        # time.sleep(3)
        # groupby_field.send_keys("config_version")
        # groupby_field.send_keys(Keys.RETURN)
        # time.sleep(2)
        # print("entered groupby_field")
        #   toast_message = self.driver.find_element(By.XPATH, "(//div[@role='status'])[1]")
        #   print(toast_message.text)
        #   time.sleep(5)
        # self.button_clicks(1,"(//i[@class='delete icon'])[2]")
        # print('deleted status column')
        # time.sleep(3)
        
        # groupby_field = self.driver.find_element(By.XPATH, "(//input[@type='text'])[12]")
        # groupby_field.send_keys("config_version")
        # groupby_field.send_keys(Keys.RETURN)
        # time.sleep(3)
        # try:
            #  toast_message = self.driver.find_element(By.XPATH, "(//div[@class='toast toast-error'])[1]")
            #  print(toast_message.text)
            #  time.sleep(3)
        # except Exception as e:
        #      print('toast message didn't appear which is correct)
        

        # self.button_clicks(1, "(//button[normalize-space()='Confirm'])[1]")
        # time.sleep(5)
        # print("clicked on confirm button")
        ##second stream
        if dashboard_type == 'device':
            self.wait_and_click("(//button[@class='ui icon primary button'])[1]")
            print("clicked on + icon")
            self.wait_and_click("(//button[@class='ui icon secondary button'])[3]")
            print("clicked on - icon")
            self.wait_and_click("(//button[@class='ui icon primary button'])[1]")
            print("clicked on + icon")
            self.wait_and_send_keys("(//input[@type='text'])[4]","motor" + Keys.RETURN)
            print("entered stream")
            self.wait_and_send_keys("(//input[@type='text'])[5]","motor_current" + Keys.RETURN)
            print("entered column")
            self.wait_and_send_keys("(//input[@type='text'])[6]","sum" + Keys.RETURN)
            print("entered aggregator")
            self.wait_and_click("(//button[contains(text(),'Advanced')])[2]")
            print("clicked on advanced button")
            self.wait_and_send_keys("(//input[@type='text'])[11]","motor_temperature1" + Keys.RETURN)
            print("entered field")
            operator = self.driver.find_element(By.XPATH, "(//div[contains(text(),'=')])[1]")
            operator.click()
            time.sleep(2)
            option_locator = "(//span[normalize-space()='>'])[1]"
            option = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, option_locator)))
            option.click()
            
            time.sleep(2)
            print("entered operator type")
            self.wait_and_send_keys("(//input[@placeholder='Value'])[1]","10" + Keys.RETURN)
            print("entered value")
            self.wait_and_click("(//button[normalize-space()='Confirm'])[1]")
            print("clicked on confirm button")
        else:
            print("forget about this step")
        # toggle_element = self.driver.find_element(By.XPATH, "(//input[@type='checkbox'])[3]")  # Use your XPath here

        # # Create an ActionChains instance
        # actions = ActionChains(self.driver)

        # # Perform a click action using ActionChains
        # actions.click(toggle_element).perform()
        # time.sleep(4)

        
        # print("disabled the alternate axis toggle")
        self.driver.execute_script("window.scrollTo(0, 0);")
        #   time.sleep(3)
        print("scrolled the page to top")
        self.wait_and_click("(//a[normalize-space()='View'])[1]")
        print("clicked on view option")
        area_chart_toggle = self.driver.find_element(By.XPATH, "(//label[@for='showAreaChartToggle'])[1]")  # Replace 'toggle-checkbox' with the actual ID of the checkbox

        # Check the current state of the checkbox
        if area_chart_toggle.is_selected():
            self.wait_and_click("(//label[@for='showAreaChartToggle'])[1]")
            print("clicked on area_chart_toggle option to disable")
        else:
            
            self.wait_and_click("(//label[@for='showAreaChartToggle'])[1]")
            #  time.sleep(5)
            print("clicked on area_chart_toggle option to enable")
        connect_null__toggle = self.driver.find_element(By.XPATH, "(//label[@for='connectNullToggle'])[1]")  # Replace 'toggle-checkbox' with the actual ID of the checkbox

        # Check the current state of the checkbox
        if connect_null__toggle.is_selected():
            # If it's selected (enabled), click to uncheck and disable it
            self.wait_and_click("(//label[@for='connectNullToggle'])[1]")
            print("clicked on connect_null__toggle option to disable")
        else:
            # If it's not selected (disabled), click to check and enable it
            self.wait_and_click("(//label[@for='connectNullToggle'])[1]")
            print("clicked on connect_null__toggle option to enable")

        pointer_toggle = self.driver.find_element(By.XPATH, "(//label[@for='showPointerToggle'])[1]")  # Replace 'toggle-checkbox' with the actual ID of the checkbox

        # Check the current state of the checkbox
        if pointer_toggle.is_selected():
            # If it's selected (enabled), click to uncheck and disable it
            self.wait_and_click("(//label[@for='showPointerToggle'])[1]")
            print("clicked on pointer_toggle option to disable")
        else:
            # If it's not selected (disabled), click to check and enable it
            self.wait_and_click("(//label[@for='showPointerToggle'])[1]")
            print("clicked on pointer_toggle option to enable")
        
        #slider
        slider = self.driver.find_element(By.XPATH, "(//input[@id='typeinp'])[1]")

        # Get the width of the slider element
        slider_width = slider.size['width']

        # Calculate the desired position on the slider (e.g., move it halfway)
        desired_position = slider_width // 2

        # Create an action chain
        action = ActionChains(self.driver)

        # Move the slider to the desired position
        action.click_and_hold(slider).move_by_offset(desired_position, 0).release().perform()
        time.sleep(2)
        print("performed slider action")
        self.wait_and_send_keys("(//input[@placeholder='Min*'])[1]","20")
        print("entered min_val")
        self.wait_and_click("(//button[normalize-space()='Submit'])[1]")
        time.sleep(2)
        toast_message = self.driver.find_element(By.XPATH, "(//div[@role='status'])[1]")
        print(toast_message.text)
        #   time.sleep(5)
        self.wait_and_send_keys("(//input[@placeholder='Max*'])[1]","50")
        print("entered max_val")
        self.wait_and_send_keys("(//input[@placeholder='Threshold'])[1]","40")
        print("entered threshold")
        self.wait_and_click("(//span[normalize-space()='Axis Settings'])[1]")
        print("clicked on axis_settings option")
        # x_grid = self.driver.find_element(By.XPATH, "(//span[@class='toggle-switch-inner'])[4]")
        # x_grid.click()
        # time.sleep(3)
        # print("clicked on x_grid option")
        # y_grid = self.driver.find_element(By.XPATH, "(//span[@class='toggle-switch-inner'])[5]")
        # y_grid.click()
        # time.sleep(3)
        # print("clicked on y_grid option")
        self.wait_and_send_keys("(//input[@placeholder='X-Axis'])[1]","hi")
        print("entered l_xaxis")
        self.wait_and_send_keys("(//input[@placeholder='Y-Axis'])[1]","hel")
        print("entered l_yaxis")
        self.wait_and_send_keys("(//input[@placeholder='X-Axis'])[2]","kg")
        print("entered u_xaxis")
        self.wait_and_send_keys("(//input[@placeholder='Y-Axis'])[2]","ml")
        print("entered u_yaxis")
        self.wait_and_click("(//button[normalize-space()='Submit'])[1]")
        time.sleep(3)
        print("entered all values in line chart and clicked on submit button")
        self.driver.execute_script("window.scrollTo(0, 0);")
        #   time.sleep(3)
        print("scrolled the page to top")
        #View full page
        panel = self.driver.find_element(By.XPATH, "(//div[@class='react-grid-item react-draggable cssTransforms react-resizable'])[1]")
        hover = ActionChains(self.driver).move_to_element(panel)
        print("moved to element")
        time.sleep(2)
        hover.perform()
        print("performed hover action")
        self.wait_and_click("(//i[@class='expand arrows alternate link icon'])[1]")
        print("clicked on view full page icon")
        time.sleep(2)
        panel = self.driver.find_element(By.XPATH, "(//div[@class='fullscreen'])[1]")
        hover = ActionChains(self.driver).move_to_element(panel)
        print("moved to element")
        time.sleep(2)
        hover.perform()
        print("performed hover action")
        self.wait_and_click("(//span[@class='bytebeam-panel-icon'])[1]")
        print("clicked on minimize icon")
        time.sleep(2)
        #edit icon
        panel = self.driver.find_element(By.XPATH, "(//div[@class='react-grid-item react-draggable cssTransforms react-resizable'])[1]")
        hover = ActionChains(self.driver).move_to_element(panel)
        print("moved to element")
        time.sleep(2)
        hover.perform()
        print("performed hover action")
        self.wait_and_click("(//i[@class='pencil link icon'])[1]")
        print("clicked on edit icon")
        self.driver.execute_script("window.scrollTo(0, 0);")
        #   time.sleep(3)
        print("scrolled the page to top")
        self.wait_and_send_keys("(//input[@placeholder='Description'])[1]","Description through edit icon on panel")
        print("entered description in panel")
        self.wait_and_click("(//button[normalize-space()='Submit'])[1]")
        time.sleep(2)
        print("clicked on submit button")
        #clone icon
        panel = self.driver.find_element(By.XPATH, "(//div[@class='react-grid-item react-draggable cssTransforms react-resizable'])[1]")
        hover = ActionChains(self.driver).move_to_element(panel)
        print("moved to element")
        time.sleep(2)
        hover.perform()
        print("performed hover action")
        self.wait_and_click("(//i[@class='clone link icon'])[1]")
        time.sleep(2)
        print("clicked on clone icon")
        #Full screen icon
        panel = self.driver.find_element(By.XPATH, "(//div[@class='react-grid-item react-draggable cssTransforms react-resizable'])[1]")
        hover = ActionChains(self.driver).move_to_element(panel)
        print("moved to element")
        time.sleep(2)
        hover.perform()
        print("performed hover action")
        self.wait_and_click("(//i[@class='expand link icon'])[1]")
        time.sleep(2)
        print("clicked on full screen icon")

        # pyautogui.press('esc')
        # time.sleep(10)
        # print("clicked on escape key")
        self.driver.execute_script("window.scrollTo(0, 0);")
        #   time.sleep(3)
        print("scrolled the page to top")

    def last_value(self,dashboard_type):
        # #last value
        self.wait_and_click("(//button[normalize-space()='Panel'])[1]")
        print("clicked on +panel button")
        self.wait_and_click("(//button[normalize-space()='Cancel'])[1]")
        print('clicked on cancel button')
        self.wait_and_click("(//button[normalize-space()='Panel'])[1]")
        print("clicked on +panel button")
        self.wait_and_click("(//button[@class='ui button add-panel-button'])[2]")
        print("clicked on last_value option")
        self.wait_and_click("(//button[normalize-space()='Back'])[1]")
        print('clicked on back button')
        self.wait_and_click("(//button[@class='ui button add-panel-button'])[2]")
        print("clicked on last_value option")
        disabled_section=self.driver.find_element(By.XPATH,"(//div[@elementid='tableLastValueSelectColumn'])[1]")
        class_name=disabled_section.get_attribute('class')
        if 'disabled' in class_name:
                print('dropdown is disabled')
        else:
                print('dropdown is enabled which is incorrect')
        disabled_section=self.driver.find_element(By.XPATH,"(//div[@role='combobox'])[3]")
        class_name=disabled_section.get_attribute('class')
        if 'disabled' in class_name:
                print('dropdown is disabled')
        else:
                print('dropdown is enabled which is incorrect')
        disabled_section=self.driver.find_element(By.XPATH,"(//div[@role='combobox'])[4]")
        class_name=disabled_section.get_attribute('class')
        if 'disabled' in class_name:
                print('dropdown is disabled')
        else:
                print('dropdown is enabled which is incorrect')
        disabled_section=self.driver.find_element(By.XPATH,"(//div[@class='ui disabled left labeled input add-panel-title-input'])[1]")
        class_name=disabled_section.get_attribute('class')
        if 'disabled' in class_name:
                print('dropdown is disabled')
        else:
                print('dropdown is enabled which is incorrect')
        untitled=self.driver.find_element(By.XPATH,"(//div[@class='bytebeam-panel-title'])[1]")
        print(untitled.text)
        if 'Untitled' in untitled.text:
                print('untitled text is there which is correct')
        else:
                print('untitled text is not there which is incorrect')
        
        
        no_data=self.driver.find_element(By.XPATH,"(//div[@class='panel-no-data'])[1]")
        print('no data on the panel')
        time.sleep(2)
        self.button_clicks(1, "(//button[normalize-space()='Submit'])[1]")
        time.sleep(1)
        toast_message = self.driver.find_element(By.XPATH, "(//div[@role='status'])[1]")
        print(toast_message.text)
        # time.sleep(5)
        self.wait_and_send_keys("(//input[@placeholder='Title'])[1]","LAST VALUE@123")
        print("entered last value title")
        time.sleep(3)
        untitled=self.driver.find_element(By.XPATH,"(//div[@class='bytebeam-panel-title'])[1]")
        print(untitled.text)
        if 'LAST VALUE@123' in untitled.text:
                print('LAST VALUE@123 text is there which is correct')
        else:
                print('LAST VALUE@123 text is not there which is incorrect')
                
        column_disabled=self.driver.find_element(By.XPATH,"(//div[@elementid='tableLastValueSelectColumn'])[1]")
        class_name=column_disabled.get_attribute('class')
        if 'disabled' in class_name:
                print('column dropdown is disabled which is correct')
        else:
                print('column dropdown is enabled which is incorrect')
        self.wait_and_send_keys("(//input[@placeholder='Description'])[1]","Description@123")
        print("entered line chart description")
        self.wait_and_send_keys("(//input[@type='text'])[1]","device_shadow" + Keys.RETURN)
        print("entered stream")
        self.wait_and_send_keys("(//input[@type='text'])[2]","range" + Keys.RETURN)
        print("entered column")
        try:
                value=self.driver.find_element(By.XPATH,"(//div[@class='big-number-value'])[1]")
                time.sleep(3)
                print("value is coming on preview")
        except Exception as e:
                print('data is not coming on preview')
        self.wait_and_click("(//button[normalize-space()='Submit'])[1]")
        time.sleep(3)
        print("clicked on submit button")
        # #Drag and drop
        # source_panel =  self.driver.find_element(By.XPATH, "(//div[@class='react-grid-item react-draggable cssTransforms react-resizable'])[1]")

        # # Find the target panel element to drop onto
        # target_panel = self.driver.find_element(By.XPATH, "(//div[@class='react-grid-item react-draggable cssTransforms react-resizable'])[2]")

        # # Create an instance of ActionChains
        # actions = ActionChains(self.driver)

        # # Perform the drag and drop operation
        # actions.drag_and_drop(source_panel, target_panel).perform()
        # # actions.click_and_hold(source_panel).move_by_offset(200, 200).release().perform()
        # time.sleep(7)
        # print("performed the drag and drop action")
        #Delete line chart
        panel = self.driver.find_element(By.XPATH, "(//div[@class='react-grid-item react-draggable cssTransforms react-resizable'])[1]")
        hover = ActionChains(self.driver).move_to_element(panel)
        print("moved to element")
        time.sleep(2)
        hover.perform()
        print("performed hover action")
        self.wait_and_click("(//i[@class='trash link icon'])[1]")
        print("clicked on delete icon to delete line chart")
        
        # #last value with so many columns
        self.wait_and_click("(//button[normalize-space()='Panel'])[1]")
        print("clicked on +panel button")
        self.wait_and_click("(//button[normalize-space()='Cancel'])[1]")
        print('clicked on cancel button')
        self.wait_and_click("(//button[normalize-space()='Panel'])[1]")
        print("clicked on +panel button")
        self.wait_and_click("(//button[@class='ui button add-panel-button'])[2]")
        print("clicked on last_value option")
        self.wait_and_click("(//button[normalize-space()='Back'])[1]")
        print('clicked on back button')
        self.wait_and_click("(//button[@class='ui button add-panel-button'])[2]")
        print("clicked on last_value option")
        untitled=self.driver.find_element(By.XPATH,"(//div[@class='bytebeam-panel-title'])[1]")
        print(untitled.text)
        if 'Untitled' in untitled.text:
                print('untitled text is there which is correct')
        else:
                print('untitled text is not there which is incorrect')
        no_data=self.driver.find_element(By.XPATH,"(//div[@class='panel-no-data'])[1]")
        print('no data on the panel')
        # time.sleep(3)
        self.button_clicks(1, "(//button[normalize-space()='Submit'])[1]")
        time.sleep(2)
        toast_message = self.driver.find_element(By.XPATH, "(//div[@role='status'])[1]")
        print(toast_message.text)
        # time.sleep(5)
        self.wait_and_send_keys("(//input[@placeholder='Title'])[1]","LAST VALUE@123")
        print("entered last value title")
        untitled=self.driver.find_element(By.XPATH,"(//div[@class='bytebeam-panel-title'])[1]")
        print(untitled.text)
        if 'LAST VALUE@123' in untitled.text:
                print('LAST VALUE@123 text is there which is correct')
        else:
                print('LAST VALUE@123 text is not there which is incorrect')
                
        column_disabled=self.driver.find_element(By.XPATH,"(//div[@elementid='tableLastValueSelectColumn'])[1]")
        class_name=column_disabled.get_attribute('class')
        if 'disabled' in class_name:
                print('column dropdown is disabled which is correct')
        else:
                print('column dropdown is enabled which is incorrect')
        self.wait_and_send_keys("(//input[@type='text'])[1]","device_shadow" + Keys.RETURN)
        print("entered stream")
        self.wait_and_send_keys("(//input[@type='text'])[2]","range" + Keys.RETURN)
        print("entered column")
        self.wait_and_send_keys("(//input[@placeholder='Prefix'])[1]","hi")
        print("entered prefix")
        self.wait_and_send_keys("(//input[@placeholder='Suffix'])[1]","hel")
        print("entered suffix")
        self.wait_and_send_keys("(//input[@type='text'])[3]","mode" + Keys.RETURN)
        print("entered second column")
        self.wait_and_send_keys("(//input[@placeholder='Prefix'])[2]","hi")
        print("entered prefix")
        self.wait_and_send_keys("(//input[@placeholder='Suffix'])[2]","hel")
        print("entered suffix")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # time.sleep(3)
        print("scrolled the page to bottom")
        self.wait_and_click("(//button[normalize-space()='Add all columns'])[1]")
        time.sleep(2)
        print("clicked on add all columns")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        print("scrolled the page to bottom")
        disabled_section=self.driver.find_element(By.XPATH,"(//div[@elementid='tableLastValueSelectColumn'])[1]")
        class_name=disabled_section.get_attribute('class')
        if 'disabled' in class_name:
                print('dropdown is disabled')
        else:
                print('dropdown is enabled which is incorrect')
        self.driver.execute_script("window.scrollTo(0, 0);")
        # time.sleep(3)
        print("scrolled the page to top")
        self.wait_and_click("(//i[@class='minus icon'])[3]")
        time.sleep(2)
        print("clicked on - icon at the third column")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # time.sleep(3)
        print("scrolled the page to bottom")
        self.wait_and_click("(//button[normalize-space()='Add all columns'])[1]")
        time.sleep(2)
        print("clicked on add all columns")
        time.sleep(2)
        disabled_section=self.driver.find_element(By.XPATH,"(//div[@elementid='tableLastValueSelectColumn'])[1]")
        class_name=disabled_section.get_attribute('class')
        if 'disabled' in class_name:
                print('dropdown is disabled')
        else:
                print('dropdown is enabled which is incorrect')
        self.driver.execute_script("window.scrollTo(0, 0);")
        # time.sleep(3)
        print("scrolled the page to top")
        time.sleep(2)
        try:
            table=self.driver.find_element(By.XPATH,"(//table[@class='ui selectable unstackable compact table'])[1]")
            # time.sleep(3)
            print('table is found on preview')
            second_cell = table.find_element(By.XPATH, './/tbody/tr[1]/td[2]')
            second_cell_text = second_cell.text
            print(second_cell_text)
            if 'km' in second_cell_text:
                print("units are there which is incorrect")
            else:
                print("units are not there which is correct")
        except Exception as e:
            print("preview is not coming with data")
        # drag and drop action
        first_sort_icon = self.driver.find_element(By.XPATH, "(//i[@class='sort icon'])[1]")
        third_sort_icon = self.driver.find_element(By.XPATH, "(//i[@class='sort icon'])[2]")
        action_chains = ActionChains(self.driver)

        # Perform the drag-and-drop operation
        action_chains.drag_and_drop(third_sort_icon, first_sort_icon).perform()
        time.sleep(3)
        print("performed the reordering")

        
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # time.sleep(3)
        print("scrolled the page to bottom")
        self.wait_and_send_keys("(//input[@type='text'])[23]","range" + Keys.RETURN)
        print("entered filter column")
        self.wait_and_send_keys("(//input[@type='text'])[24]",">" + Keys.RETURN)
        print("entered field column")
        self.wait_and_send_keys("(//input[@placeholder='Value'])[1]","52000" + Keys.RETURN)
        print("entered value column")
        self.wait_and_click("(//button[@class='ui icon primary button'])[1]")
        print("clicked on plus icon")
        self.wait_and_click("(//button[@class='ui icon secondary button'])[1]")
        print("clicked on minus icon")
        self.wait_and_click("(//button[@class='ui icon primary button'])[1]")
        print("clicked on plus icon")
        self.wait_and_send_keys("(//input[@type='text'])[25]","SOC" + Keys.RETURN)
        print("entered filter column")
        self.wait_and_send_keys("(//input[@type='text'])[26]","<" + Keys.RETURN)
        print("entered field column")
        self.wait_and_send_keys("(//input[@placeholder='Value'])[2]","70" + Keys.RETURN)
        print("entered value column")
        self.driver.execute_script("window.scrollTo(0, 0);")
        # time.sleep(3)
        print("scrolled the page to top")
        self.wait_and_click("(//a[normalize-space()='View'])[1]")
        time.sleep(2)
        print("clicked on view option")
        enable_units = self.driver.find_element(By.XPATH, "(//label[@for='enableUnits'])[1]")  # Replace 'toggle-checkbox' with the actual ID of the checkbox

        # Check the current state of the checkbox
        if enable_units.is_selected():
            self.wait_and_click("(//label[@for='enableUnits'])[1]")
            print("clicked on enable_units option to disable")
        else:
            self.wait_and_click("(//label[@for='enableUnits'])[1]")
            print("clicked on enable_units option to enable")
        try:
            table=self.driver.find_element(By.XPATH,"(//table[@class='ui selectable unstackable compact table'])[1]")
            time.sleep(2)
            print('table is found on preview')
            second_cell = table.find_element(By.XPATH, './/tbody/tr[1]/td[2]')
            second_cell_text = second_cell.text
            print(second_cell_text)
            if 'km' in second_cell_text:
                print("units are there which is correct")
            else:
                print("units are not there which is incorrect")
        except Exception as e:
            print("preview is not coming with data")
        
        self.button_clicks(1, "(//button[normalize-space()='Submit'])[1]")
        time.sleep(3)
        print("clicked on submit button")

    def gauge_chart(self,dashboard_type):
        #Gauge Chart
        self.driver.execute_script("window.scrollTo(0, 0);")
        # time.sleep(3)
        print("scrolled the page to top")
        self.wait_and_click("(//button[normalize-space()='Panel'])[1]")
        print("clicked on +panel button")
        self.wait_and_click("(//button[normalize-space()='Cancel'])[1]")
        print('clicked on cancel button')
        self.wait_and_click("(//button[normalize-space()='Panel'])[1]")
        print("clicked on +panel button")
        self.wait_and_click("(//button[@class='ui button add-panel-button'])[3]")
        print("clicked on last_value option")
        self.wait_and_click("(//button[normalize-space()='Back'])[1]")
        print('clicked on back button')
        self.wait_and_click("(//button[@class='ui button add-panel-button'])[3]")
        print("clicked on last_value option")
        disabled_section=self.driver.find_element(By.XPATH,"(//div[@class='ui disabled search selection dropdown'])[1]")
        class_name=disabled_section.get_attribute('class')
        if 'disabled' in class_name:
                print('dropdown is disabled')
        else:
                print('dropdown is enabled which is incorrect')
        no_data=self.driver.find_element(By.XPATH,"(//div[@class='panel-no-data'])[1]")
        print('no data on the panel')
        # time.sleep(3)
        untitled=self.driver.find_element(By.XPATH,"(//div[@class='bytebeam-panel-title'])[1]")
        print(untitled.text)
        if 'Untitled' in untitled.text:
                print('untitled text is there which is correct')
        else:
                print('untitled text is not there which is incorrect')
        self.wait_and_click("(//button[normalize-space()='Submit'])[1]")
        time.sleep(2)
        toast_message = self.driver.find_element(By.XPATH, "(//div[@role='status'])[1]")
        print(toast_message.text)
        # time.sleep(5)
        self.wait_and_send_keys("(//input[@placeholder='Title'])[1]","GAUGE CHART@123")
        print("entered gauge chart title")
        untitled=self.driver.find_element(By.XPATH,"(//div[@class='bytebeam-panel-title'])[1]")
        print(untitled.text)
        if 'GAUGE CHART@123' in untitled.text:
                print('GAUGE CHART@123 text is there which is correct')
        else:
                print('GAUGE CHART@123 text is not there which is incorrect')
        self.wait_and_send_keys("(//input[@placeholder='Description'])[1]","Description@123")
        print("entered line chart description")
        self.wait_and_send_keys("(//input[@placeholder='Min Threshold'])[1]","20")
        print("entered min threshold")
        self.wait_and_send_keys("(//input[@placeholder='Max Threshold'])[1]","100")
        print("entered max threshold")
        self.wait_and_send_keys("(//input[@type='text'])[1]","device_shadow" + Keys.RETURN)
        print("entered stream")
        self.wait_and_send_keys("(//input[@type='text'])[2]","SOC" + Keys.RETURN)
        print("entered column")
        time.sleep(2)
        try:
            gauge=self.driver.find_element(By.XPATH,"(//div[@id='gauge_SOC'])[1]")
            # time.sleep(3)
            print("gauge chart is coming on preview")
        except Exception as e:
            print("preview is not coming with data")
        self.wait_and_click("(//a[normalize-space()='View'])[1]")
        time.sleep(2)
        print("clicked on view option")
        area_chart_toggle = self.driver.find_element(By.XPATH, "(//label[@for='showAreaChartToggle'])[1]")  # Replace 'toggle-checkbox' with the actual ID of the checkbox

        # Check the current state of the checkbox
        if area_chart_toggle.is_selected():
            self.wait_and_click("(//label[@for='showAreaChartToggle'])[1]")
            print("clicked on area_chart_toggle option to disable")
        else:
            self.wait_and_click("(//label[@for='showAreaChartToggle'])[1]")
            print("clicked on area_chart_toggle option to enable")

        self.wait_and_click("(//div[@id='default_color'])[1]")
        print("clicked on default color")
        self.wait_and_click("(//div[@title='#F8E71C'])[1]")
        print("clicked on color")
        self.wait_and_click("(//div[@id='default_color'])[2]")
        print("clicked on default color")
        self.wait_and_click("(//div[@title='#50E3C2'])[2]")
        print("clicked on color")
        #slider
        slider = self.driver.find_element(By.XPATH, "(//input[@id='typeinp'])[1]")

        # Get the width of the slider element
        slider_width = slider.size['width']

        # Calculate the desired position on the slider (e.g., move it halfway)
        desired_position = slider_width // 2

        # Create an action chain
        action = ActionChains(self.driver)

        # Move the slider to the desired position
        action.click_and_hold(slider).move_by_offset(desired_position, 0).release().perform()
        time.sleep(2)
        print("performed slider action")
        self.wait_and_send_keys("(//input[@type='text'])[3]","kg" + Keys.RETURN)
        print("entered units")
        self.wait_and_click("(//button[normalize-space()='Submit'])[1]")
        time.sleep(3)
        print("entered all values in gauge chart and clicked on submit button")

    def led_panel(self,dashboard_type):
         #LED Panel
        self.wait_and_click("(//button[normalize-space()='Panel'])[1]")
        print("clicked on +panel button")
        self.wait_and_click("(//button[normalize-space()='Cancel'])[1]")
        print('clicked on cancel button')
        self.wait_and_click("(//button[normalize-space()='Panel'])[1]")
        print("clicked on +panel button")
        if dashboard_type=='device':
            self.wait_and_click("(//button[@class='ui button add-panel-button'])[5]")
            print("clicked on last_value option")
            self.wait_and_click("(//button[normalize-space()='Back'])[1]")
            print('clicked on back button')
            self.wait_and_click("(//button[@class='ui button add-panel-button'])[5]")
            print("clicked on last_value option")
        else:
            self.wait_and_click("(//button[@class='ui button add-panel-button'])[3]")
            print("clicked on last_value option")
            self.wait_and_click("(//button[normalize-space()='Back'])[1]")
            print('clicked on back button')
            self.wait_and_click("(//button[@class='ui button add-panel-button'])[3]")
            print("clicked on last_value option")
        
        disabled_section=self.driver.find_element(By.XPATH,"(//div[@class='ui disabled search selection dropdown'])[1]")
        class_name=disabled_section.get_attribute('class')
        if 'disabled' in class_name:
                print('dropdown is disabled')
        else:
                print('dropdown is enabled which is incorrect')
        no_data=self.driver.find_element(By.XPATH,"(//div[@class='panel-no-data'])[1]")
        print('no data on the panel')
        # time.sleep(3)
        untitled=self.driver.find_element(By.XPATH,"(//div[@class='bytebeam-panel-title'])[1]")
        print(untitled.text)
        if 'Untitled' in untitled.text:
                print('untitled text is there which is correct')
        else:
                print('untitled text is not there which is incorrect')
        self.wait_and_click("(//button[normalize-space()='Submit'])[1]")
        time.sleep(2)
        toast_message = self.driver.find_element(By.XPATH, "(//div[@role='status'])[1]")
        print(toast_message.text)
        # time.sleep(5)
        self.wait_and_send_keys("(//input[@placeholder='Title'])[1]","LED PANEL@123")
        print("entered led panel title")
        untitled=self.driver.find_element(By.XPATH,"(//div[@class='bytebeam-panel-title'])[1]")
        print(untitled.text)
        if 'LED PANEL@123' in untitled.text:
                print('LED PANEL@123 text is there which is correct')
        else:
                print('LED PANEL@123 text is not there which is incorrect')
        self.wait_and_send_keys("(//input[@placeholder='Description'])[1]","Description@123")
        print("entered description")
        self.wait_and_send_keys("(//input[@type='text'])[1]","device_shadow" + Keys.RETURN)
        print("entered stream")
        self.wait_and_send_keys("(//input[@type='text'])[2]","mode" + Keys.RETURN)
        print("entered column")
        self.wait_and_send_keys("(//input[@type='text'])[3]","range" + Keys.RETURN)
        print("entered second column")
        try:
            circle=self.driver.find_element(By.XPATH,"(//*[name()='circle'])[1]")
            # time.sleep(3)
            print("circles are coming on preview")
        except Exception as e:
            print("preview is not coming with data")

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # time.sleep(3)
        print("scrolled the page to bottom")
        self.wait_and_click("(//button[normalize-space()='Add all columns'])[1]")
        time.sleep(2)
        print("clicked on add all columns")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # time.sleep(3)
        print("scrolled the page to bottom")
        disabled_section=self.driver.find_element(By.XPATH,"(//div[@class='ui disabled search selection dropdown'])[1]")
        class_name=disabled_section.get_attribute('class')
        if 'disabled' in class_name:
                print('dropdown is disabled')
        else:
                print('dropdown is enabled which is incorrect')
        self.driver.execute_script("window.scrollTo(0, 0);")
        # time.sleep(3)
        print("scrolled the page to top")
        self.wait_and_click("(//i[@class='minus icon'])[3]")
        print("clicked on - icon at the third column")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # time.sleep(3)
        print("scrolled the page to bottom")
        self.wait_and_click("(//button[normalize-space()='Add all columns'])[1]")
        time.sleep(2)
        print("clicked on add all columns")
        disabled_section=self.driver.find_element(By.XPATH,"(//div[@class='ui disabled search selection dropdown'])[1]")
        class_name=disabled_section.get_attribute('class')
        if 'disabled' in class_name:
                print('dropdown is disabled')
        else:
                print('dropdown is enabled which is incorrect')
        self.driver.execute_script("window.scrollTo(0, 0);")
        # time.sleep(3)
        print("scrolled the page to top")
        # drag and drop action
        first_sort_icon = self.driver.find_element(By.XPATH, "(//i[@class='sort icon'])[1]")
        third_sort_icon = self.driver.find_element(By.XPATH, "(//i[@class='sort icon'])[2]")
        action_chains = ActionChains(self.driver)

        # Perform the drag-and-drop operation
        action_chains.drag_and_drop(third_sort_icon, first_sort_icon).perform()
        time.sleep(2)
        print("performed the reordering")

        
        self.driver.execute_script("window.scrollTo(0, 0);")
        # time.sleep(3)
        print("scrolled the page to top")
        self.wait_and_click("(//a[normalize-space()='View'])[1]")
        time.sleep(2)
        print("clicked on view option")
        try:
                on=self.driver.find_element(By.XPATH,"(//p[normalize-space()='on'])[1]")
                # time.sleep(3)
                print("found the default on text")
        except Exception as e:
                print('default on text is not found')
        try:
                on=self.driver.find_element(By.XPATH,"(//p[normalize-space()='off'])[1]")
                # time.sleep(3)
                print("found the default off text")
        except Exception as e:
                print('default off text is not found')
        self.wait_and_send_keys("(//input[@placeholder='Add State value and press Enter'])[1]","off" + Keys.RETURN)
        time.sleep(2)
        try:
            message=self.driver.find_element(By.XPATH,'''(//span[normalize-space()="This state is already added in 'Inactive state'."])[1]''')
            print('found the message')
        except Exception as e:
            print("didn't find the message")
        self.wait_and_send_keys("(//input[@placeholder='Add State value and press Enter'])[1]","on" + Keys.RETURN)
        time.sleep(2)
        try:
            message=self.driver.find_element(By.XPATH,'''(//span[normalize-space()='value already exists!'])[1]''')
            print('found the message')
        except Exception as e:
            print("didn't find the message")
        # time.sleep(3)
        self.wait_and_click("(//div[@id='default_color'])[1]")
        print("clicked on default color")
        self.wait_and_click("(//div[@title='#F8E71C'])[1]")
        print("clicked on color")
        self.wait_and_click("(//div[@id='default_color'])[2]")
        print("clicked on default color")
        self.wait_and_click("(//div[@title='#50E3C2'])[2]")
        print("clicked on color")

        #slider
        slider = self.driver.find_element(By.XPATH, "(//input[@id='typeinp'])[1]")

        # Get the width of the slider element
        slider_width = slider.size['width']

        # Calculate the desired position on the slider (e.g., move it halfway)
        desired_position = slider_width // 2

        # Create an action chain
        action = ActionChains(self.driver)

        # Move the slider to the desired position
        action.click_and_hold(slider).move_by_offset(desired_position, 0).release().perform()
        time.sleep(3)
        print("performed slider action")
        self.wait_and_click("(//button[normalize-space()='Submit'])[1]")
        time.sleep(3)
        print("entered all values in led panel and clicked on submit button")

    def aggregate_value(self,dashboard_type):
        #AGGREGATE VALUE
        self.wait_and_click("(//button[normalize-space()='Panel'])[1]")
        print("clicked on +panel button")
        self.wait_and_click("(//button[normalize-space()='Cancel'])[1]")
        print('clicked on cancel button')
        self.wait_and_click("(//button[normalize-space()='Panel'])[1]")
        print("clicked on +panel button")
        if dashboard_type=='device':
            self.wait_and_click("(//button[@class='ui button add-panel-button'])[6]")
            print("clicked on aggregate value option")
            self.wait_and_click("(//button[normalize-space()='Back'])[1]")
            print('clicked on back button')
            self.wait_and_click("(//button[@class='ui button add-panel-button'])[6]")
            print("clicked on aggregate value option")
        else:
            self.wait_and_click("(//button[@class='ui button add-panel-button'])[4]")
            print("clicked on aggregate value option")
            self.wait_and_click("(//button[normalize-space()='Back'])[1]")
            print('clicked on back button')
            self.wait_and_click("(//button[@class='ui button add-panel-button'])[4]")
            print("clicked on aggregate value option")
        
        disabled_section=self.driver.find_element(By.XPATH,"(//div[@class='ui disabled search selection dropdown'])[1]")
        class_name=disabled_section.get_attribute('class')
        if 'disabled' in class_name:
                print('dropdown is disabled')
        else:
                print('dropdown is enabled which is incorrect')
        disabled_section=self.driver.find_element(By.XPATH,"(//div[@class='ui disabled multiple search selection dropdown'])[1]")
        class_name=disabled_section.get_attribute('class')
        if 'disabled' in class_name:
                print('dropdown is disabled')
        else:
                print('dropdown is enabled which is incorrect')
        no_data=self.driver.find_element(By.XPATH,"(//div[@class='panel-no-data'])[1]")
        print('no data on the panel')
        # time.sleep(3)
        untitled=self.driver.find_element(By.XPATH,"(//div[@class='bytebeam-panel-title'])[1]")
        print(untitled.text)
        if 'Untitled' in untitled.text:
                print('untitled text is there which is correct')
        else:
                print('untitled text is not there which is incorrect')
        self.wait_and_click("(//button[normalize-space()='Submit'])[1]")
        time.sleep(2)
        toast_message = self.driver.find_element(By.XPATH, "(//div[@role='status'])[1]")
        print(toast_message.text)
        # time.sleep(5)
        self.wait_and_send_keys("(//input[@placeholder='Title'])[1]","AGGREGATE VALUE@123")
        print("entered aggregate value title")
        untitled=self.driver.find_element(By.XPATH,"(//div[@class='bytebeam-panel-title'])[1]")
        print(untitled.text)
        if 'AGGREGATE VALUE@123' in untitled.text:
                print('AGGREGATE VALUE@123 text is there which is correct')
        else:
                print('AGGREGATE VALUE@123 text is not there which is incorrect')
        self.wait_and_send_keys("(//input[@placeholder='Description'])[1]","Description@123")
        print("entered description")
        self.wait_and_send_keys("(//input[@type='text'])[1]","device_shadow" + Keys.RETURN)
        print("entered stream")
        disabled_section=self.driver.find_element(By.XPATH,"(//div[@class='ui disabled error multiple search selection dropdown'])[1]")
        class_name=disabled_section.get_attribute('class')
        if 'disabled' in class_name:
                print('dropdown is disabled')
        else:
                print('dropdown is enabled which is incorrect')
        self.wait_and_send_keys("(//input[@type='text'])[2]","range" + Keys.RETURN)
        print("entered column")
        self.wait_and_send_keys("(//input[@type='text'])[3]","sum" + Keys.RETURN)
        time.sleep(2)
        try:
                value=self.driver.find_element(By.XPATH,"(//div[@class='big-number-value'])[1]")
                # time.sleep(3)
                print("value is coming on preview")
        except Exception as e:
                print('data is not coming on preview')
        self.wait_and_send_keys("(//input[@placeholder='Prefix'])[1]","hi" + Keys.RETURN)
        print("entered prefix")
        self.wait_and_send_keys("(//input[@placeholder='Suffix'])[1]","hel" + Keys.RETURN)
        print("entered suffix")
        self.wait_and_click("(//a[normalize-space()='View'])[1]")
        print("clicked on view option")
        auto_text_size = self.driver.find_element(By.XPATH, "(//label[@for='showRangeZeroToggle'])[1]")  # Replace 'toggle-checkbox' with the actual ID of the checkbox

        # Check the current state of the checkbox
        if auto_text_size.is_selected():
            self.wait_and_click("(//label[@for='showRangeZeroToggle'])[1]")
            print("clicked on area_chart_toggle option to disable")
        else:
            self.wait_and_click("(//label[@for='showRangeZeroToggle'])[1]")
            print("clicked on area_chart_toggle option to enable")
        
        
        #slider
        slider = self.driver.find_element(By.XPATH, "(//input[@id='typeinp'])[1]")

        # Get the width of the slider element
        slider_width = slider.size['width']

        # Calculate the desired position on the slider (e.g., move it halfway)
        desired_position = slider_width // 2

        # Create an action chain
        action = ActionChains(self.driver)

        # Move the slider to the desired position
        action.click_and_hold(slider).move_by_offset(desired_position, 0).release().perform()
        time.sleep(3)
        print("performed slider action")
        self.wait_and_click("(//button[normalize-space()='Submit'])[1]")
        time.sleep(3)
        print("entered all values in aggregate value and clicked on submit button")
        
        #AGGREGATE VALUE with many operator values
        self.wait_and_click("(//button[normalize-space()='Panel'])[1]")
        print("clicked on +panel button")
        self.wait_and_click("(//button[normalize-space()='Cancel'])[1]")
        print('clicked on cancel button')
        self.wait_and_click("(//button[normalize-space()='Panel'])[1]")
        print("clicked on +panel button")
        if dashboard_type=='device':
            self.wait_and_click("(//button[@class='ui button add-panel-button'])[6]")
            print("clicked on aggregate value option")
            self.wait_and_click("(//button[normalize-space()='Back'])[1]")
            print('clicked on back button')
            self.wait_and_click("(//button[@class='ui button add-panel-button'])[6]")
            print("clicked on aggregate value option")
        else:
            self.wait_and_click("(//button[@class='ui button add-panel-button'])[4]")
            print("clicked on aggregate value option")
            self.wait_and_click("(//button[normalize-space()='Back'])[1]")
            print('clicked on back button')
            self.wait_and_click("(//button[@class='ui button add-panel-button'])[4]")
            print("clicked on aggregate value option")
        no_data=self.driver.find_element(By.XPATH,"(//div[@class='panel-no-data'])[1]")
        print('no data on the panel')
        # time.sleep(3)
        untitled=self.driver.find_element(By.XPATH,"(//div[@class='bytebeam-panel-title'])[1]")
        print(untitled.text)
        if 'Untitled' in untitled.text:
                print('untitled text is there which is correct')
        else:
                print('untitled text is not there which is incorrect')
        self.wait_and_click("(//button[normalize-space()='Submit'])[1]")
        time.sleep(2)
        toast_message = self.driver.find_element(By.XPATH, "(//div[@role='status'])[1]")
        print(toast_message.text)
        # time.sleep(5)
        self.wait_and_send_keys("(//input[@placeholder='Title'])[1]","AGGREGATE VALUE@123")
        print("entered aggregate value title")
        untitled=self.driver.find_element(By.XPATH,"(//div[@class='bytebeam-panel-title'])[1]")
        print(untitled.text)
        if 'AGGREGATE VALUE@123' in untitled.text:
                print('AGGREGATE VALUE@123 text is there which is correct')
        else:
                print('AGGREGATE VALUE@123 text is not there which is incorrect')
        self.wait_and_send_keys("(//input[@type='text'])[1]","device_shadow" + Keys.RETURN)
        print("entered stream")
        self.wait_and_send_keys("(//input[@type='text'])[2]","range" + Keys.RETURN)
        print("entered column")
        self.wait_and_send_keys("(//input[@type='text'])[3]","sum" + Keys.RETURN)
        # time.sleep(2)
        self.wait_and_send_keys("(//input[@type='text'])[3]","min" + Keys.RETURN)
        # time.sleep(2)
        self.wait_and_send_keys("(//input[@type='text'])[3]","max" + Keys.RETURN)
        print("entered aggregator value")
        self.wait_and_send_keys("(//input[@placeholder='Prefix'])[1]","hi" + Keys.RETURN)
        print("entered prefix")
        self.wait_and_send_keys("(//input[@placeholder='Suffix'])[1]","hel" + Keys.RETURN)
        print("entered suffix")
        try:
            table=self.driver.find_element(By.XPATH,"(//table[@class='ui small selectable unstackable compact table'])[1]")
            time.sleep(2)
            print('table is found on preview')
            second_cell = table.find_element(By.XPATH, './/tbody/tr[1]/td[2]')
            second_cell_text = second_cell.text
            print(second_cell_text)
            if 'km' in second_cell_text:
                print("units are there which is incorrect")
            else:
                print("units are not there which is correct")
        except Exception as e:
            print("preview is not coming with data")
        self.wait_and_click("(//a[normalize-space()='View'])[1]")
        print("clicked on view option")
        enable_units = self.driver.find_element(By.XPATH, "(//label[@for='enableUnits'])[1]")  # Replace 'toggle-checkbox' with the actual ID of the checkbox

        # Check the current state of the checkbox
        if enable_units.is_selected():
            self.wait_and_click("(//label[@for='enableUnits'])[1]")
            time.sleep(2)
            print("clicked on enable_units option to disable")
        else:
            self.wait_and_click("(//label[@for='enableUnits'])[1]")
            time.sleep(2)
            print("clicked on enable_units option to enable")
        try:
            table=self.driver.find_element(By.XPATH,"(//table[@class='ui small selectable unstackable compact table'])[1]")
            time.sleep(2)
            print('table is found on preview')
            second_cell = table.find_element(By.XPATH, './/tbody/tr[1]/td[2]')
            second_cell_text = second_cell.text
            print(second_cell_text)
            if 'km' in second_cell_text:
                print("units are there which is correct")
            else:
                print("units are not there which is incorrect")
        except Exception as e:
            print("preview is not coming with data")
        auto_text_size = self.driver.find_element(By.XPATH, "(//label[@for='showRangeZeroToggle'])[1]")  # Replace 'toggle-checkbox' with the actual ID of the checkbox

        # Check the current state of the checkbox
        if auto_text_size.is_selected():
            self.wait_and_click("(//label[@for='showRangeZeroToggle'])[1]")
            print("clicked on area_chart_toggle option to disable")
        else:
            self.wait_and_click("(//label[@for='showRangeZeroToggle'])[1]")
            print("clicked on area_chart_toggle option to enable")
        
        
        #slider
        slider = self.driver.find_element(By.XPATH, "(//input[@id='typeinp'])[1]")

        # Get the width of the slider element
        slider_width = slider.size['width']

        # Calculate the desired position on the slider (e.g., move it halfway)
        desired_position = slider_width // 2

        # Create an action chain
        action = ActionChains(self.driver)

        # Move the slider to the desired position
        action.click_and_hold(slider).move_by_offset(desired_position, 0).release().perform()
        time.sleep(3)
        print("performed slider action")
        self.wait_and_click("(//button[normalize-space()='Submit'])[1]")
        time.sleep(3)
        print("entered all values in aggregate value and clicked on submit button")

    def locate_devices(self,dashboard_type):
         #LOCATE DEVICES
        self.wait_and_click("(//button[normalize-space()='Panel'])[1]")
        print("clicked on +panel button")
        self.wait_and_click("(//button[normalize-space()='Cancel'])[1]")
        print('clicked on cancel button')
        self.wait_and_click("(//button[normalize-space()='Panel'])[1]")
        print("clicked on +panel button")
        if dashboard_type=='device':
            self.wait_and_click("(//button[@class='ui button add-panel-button'])[7]")
            print("clicked on aggregate value option")
            self.wait_and_click("(//button[normalize-space()='Back'])[1]")
            print('clicked on back button')
            self.wait_and_click("(//button[@class='ui button add-panel-button'])[7]")
            print("clicked on aggregate value option")
        else:
            self.wait_and_click("(//button[@class='ui button add-panel-button'])[5]")
            print("clicked on aggregate value option")
            self.wait_and_click("(//button[normalize-space()='Back'])[1]")
            print('clicked on back button')
            self.wait_and_click("(//button[@class='ui button add-panel-button'])[5]")
            print("clicked on aggregate value option")
        disabled_section=self.driver.find_element(By.XPATH,"(//div[@elementid='LocateDevicesColumn'])[1]")
        class_name=disabled_section.get_attribute('class')
        if 'disabled' in class_name:
                print('dropdown is disabled')
        else:
                print('dropdown is enabled which is incorrect')
        disabled_section=self.driver.find_element(By.XPATH,"(//div[@elementid='LocateDevicesLongitude'])[1]")
        class_name=disabled_section.get_attribute('class')
        if 'disabled' in class_name:
                print('dropdown is disabled')
        else:
                print('dropdown is enabled which is incorrect')
        no_data=self.driver.find_element(By.XPATH,"(//div[@class='panel-no-data'])[1]")
        print('no data on the panel')
        # time.sleep(3)
        untitled=self.driver.find_element(By.XPATH,"(//div[@class='bytebeam-panel-title'])[1]")
        print(untitled.text)
        if 'Untitled' in untitled.text:
                print('untitled text is there which is correct')
        else:
                print('untitled text is not there which is incorrect')
        self.wait_and_click("(//button[normalize-space()='Submit'])[1]")
        time.sleep(2)
        toast_message = self.driver.find_element(By.XPATH, "(//div[@role='status'])[1]")
        print(toast_message.text)
        # time.sleep(5)
        self.wait_and_send_keys("(//input[@placeholder='Title'])[1]","LOCATE DEVICE@123")
        print("entered locate device title")
        untitled=self.driver.find_element(By.XPATH,"(//div[@class='bytebeam-panel-title'])[1]")
        print(untitled.text)
        if 'LOCATE DEVICE@123' in untitled.text:
                print('LOCATE DEVICE@123 text is there which is correct')
        else:
                print('LOCATE DEVICE@123 text is not there which is incorrect')
        self.wait_and_send_keys("(//input[@placeholder='Description'])[1]","Description@123")
        print("entered description")
        time.sleep(2)
        stream = self.driver.find_element(By.XPATH, "(//input[@type='text'])[1]")
        stream.send_keys("gps")
        self.button_clicks(1, "(//span[normalize-space()='gps'])[1]")
        time.sleep(2)
        
        print("entered stream")
        self.wait_and_send_keys("(//input[@type='text'])[2]","latitude" + Keys.RETURN)
        print("entered latitude")
        self.wait_and_send_keys("(//input[@type='text'])[3]","longitude" + Keys.RETURN)
        print("entered longitude")
        self.wait_and_send_keys("(//input[@type='text'])[4]","162 - Vehicle Dashboard" + Keys.RETURN)
        self.wait_and_send_keys("(//input[@placeholder='Description'])[1]","desc@123")
        print("entered desc")

        # dev_dashboard.send_keys("37 - Simulator tables")
        # dev_dashboard.send_keys(Keys.RETURN)
        # time.sleep(3)
        # dev_dashboard.send_keys("67 - Testers")
        # dev_dashboard.send_keys(Keys.RETURN)
        # time.sleep(3)
        print("entered dashboard values")
        self.wait_and_send_keys("(//input[@type='text'])[5]","owner" + Keys.RETURN)
        self.wait_and_send_keys("(//input[@type='text'])[5]","model" + Keys.RETURN)
        time.sleep(2)
        description = self.driver.find_element(By.XPATH, "(//input[@placeholder='Description'])[1]")
        description.send_keys(Keys.COMMAND, "A")
        description.send_keys("desc")
        
        time.sleep(3)
        print("entered desc")
        self.wait_and_send_keys("(//input[@type='text'])[6]","range" + Keys.RETURN)
        self.wait_and_send_keys("(//input[@type='text'])[6]","mode" + Keys.RETURN)
        time.sleep(2)
        description = self.driver.find_element(By.XPATH, "(//input[@placeholder='Description'])[1]")
        description.send_keys(Keys.COMMAND, "A")
        description.send_keys("description")
        
        time.sleep(3)
        print("entered desc")
        self.driver.execute_script("window.scrollTo(0, 0);")
        # time.sleep(3)
        print("scrolled the page to top")

        # img_element = self.driver.find_element(By.XPATH, "//div[@aria-label='']")

        # # Click on the <img> element
        
        # img_element.click()

        # time.sleep(5)
        # print("clicked on the icon")
        # self.button_clicks(1, "(//a[@id='162_dashboardLink'])[1]")
        # time.sleep(5)
        # print("clicked on dashboard")
        # self.driver.switch_to.window(self.driver.window_handles[0])
        # print("moved back to old wiwndow")
        self.wait_and_click("(//a[normalize-space()='View'])[1]")
        print("clicked on view option")
        satellite_layer = self.driver.find_element(By.XPATH, "(//input[@type='radio'])[1]")  # Replace 'toggle-checkbox' with the actual ID of the checkbox

        # Check the current state of the checkbox
        if satellite_layer.is_selected():
            self.driver.execute_script("arguments[0].click();", satellite_layer)
            print("clicked on satellite_layer option to disable")
        else:
            self.driver.execute_script("arguments[0].click();", satellite_layer)
            print("clicked on satellite_layer option to enable")
        self.wait_and_click("(//i[@class='car large icon'])[1]")
        print("clicked on car icon")
        self.wait_and_click("(//button[normalize-space()='Add State'])[1]")
        print("clicked on add state button")
        self.wait_and_click("(//button[normalize-space()='Delete State'])[1]")
        print("clicked on delete state button")
        self.wait_and_click("(//button[normalize-space()='Add State'])[1]")
        print("clicked on add state button")
        self.wait_and_click("(//div[@id='default_color'])[1]")
        print("clicked on default color")
        self.wait_and_click("(//div[@title='#F8E71C'])[1]")
        print("clicked on color")
        self.wait_and_send_keys("(//input[@placeholder='Enter Status Field Value'])[1]","OnTrip")
        print("entered new state")
        self.wait_and_click("(//button[normalize-space()='Submit'])[1]")
        time.sleep(3)
        print("entered all values in locate device and clicked on submit button")

    def track_devices(self,dashboard_type):
        #TRACK DEVICES
        self.driver.execute_script("window.scrollTo(0, 0);")
        # time.sleep(3)
        print("scrolled the page to top")
        self.wait_and_click("(//button[normalize-space()='Panel'])[1]")
        print("clicked on +panel button")
        self.wait_and_click("(//button[normalize-space()='Cancel'])[1]")
        print('clicked on cancel button')
        self.wait_and_click("(//button[normalize-space()='Panel'])[1]")
        print("clicked on +panel button")
        self.wait_and_click("(//button[@class='ui button add-panel-button'])[8]")
        print("clicked on aggregate value option")
        self.wait_and_click("(//button[normalize-space()='Back'])[1]")
        print('clicked on back button')
        self.wait_and_click("(//button[@class='ui button add-panel-button'])[8]")
        print("clicked on aggregate value option")
        disabled_section=self.driver.find_element(By.XPATH,"(//div[@elementid='TrackDevicesColumn'])[1]")
        class_name=disabled_section.get_attribute('class')
        if 'disabled' in class_name:
                print('dropdown is disabled')
        else:
                print('dropdown is enabled which is incorrect')
        disabled_section=self.driver.find_element(By.XPATH,"(//div[@elementid='TrackDevicesLongitude'])[1]")
        class_name=disabled_section.get_attribute('class')
        if 'disabled' in class_name:
                print('dropdown is disabled')
        else:
                print('dropdown is enabled which is incorrect')
        no_data=self.driver.find_element(By.XPATH,"(//div[@class='panel-no-data'])[1]")
        print('no data on the panel')
        # time.sleep(3)
        untitled=self.driver.find_element(By.XPATH,"(//div[@class='bytebeam-panel-title'])[1]")
        print(untitled.text)
        if 'Untitled' in untitled.text:
                print('untitled text is there which is correct')
        else:
                print('untitled text is not there which is incorrect')
        self.wait_and_click("(//button[normalize-space()='Submit'])[1]")
        time.sleep(2)
        toast_message = self.driver.find_element(By.XPATH, "(//div[@role='status'])[1]")
        print(toast_message.text)
        # time.sleep(5)
        self.wait_and_send_keys("(//input[@placeholder='Title'])[1]","TRACK DEVICE@123")
        print("entered track device title")
        untitled=self.driver.find_element(By.XPATH,"(//div[@class='bytebeam-panel-title'])[1]")
        print(untitled.text)
        if 'TRACK DEVICE@123' in untitled.text:
                print('TRACK DEVICE@123 text is there which is correct')
        else:
                print('TRACK DEVICE@123 text is not there which is incorrect')
        self.wait_and_send_keys("(//input[@placeholder='Description'])[1]","Description@123")
        print("entered description")
        time.sleep(2)
        stream = self.driver.find_element(By.XPATH, "(//input[@type='text'])[1]")
        stream.send_keys("gps")
        self.button_clicks(1, "(//span[normalize-space()='gps'])[1]")
        time.sleep(2)
        print("entered stream")
        self.wait_and_send_keys("(//input[@type='text'])[2]","latitude" + Keys.RETURN)
        print("entered latitude")
        self.wait_and_send_keys("(//input[@type='text'])[3]","longitude" + Keys.RETURN)
        print("entered longitude")

        self.driver.execute_script("window.scrollTo(0, 0);")
        # time.sleep(3)
        print("scrolled the page to top")

        # img_element = self.driver.find_element(By.XPATH, "//div[@aria-label='']")

        # # Click on the <img> element
        
        # img_element.click()

        # time.sleep(5)
        # print("clicked on the icon")
        
        self.driver.execute_script("window.scrollTo(0, 0);")
        # time.sleep(3)
        print("scrolled the page to top")
        self.wait_and_click("(//a[normalize-space()='View'])[1]")
        print("clicked on view option")
        traffic_layer = self.driver.find_element(By.XPATH, "(//input[@type='radio'])[2]")  # Replace 'toggle-checkbox' with the actual ID of the checkbox

        # Check the current state of the checkbox
        if traffic_layer.is_selected():
            # If it's selected (enabled), click to uncheck and disable it
            self.driver.execute_script("arguments[0].click();", traffic_layer)
        #    traffic_layer.click()
            # time.sleep(5)
            print("clicked on traffic_layer option to disable")
        else:
            # If it's not selected (disabled), click to check and enable it
            self.driver.execute_script("arguments[0].click();", traffic_layer)
        #    traffic_layer.click()
            # time.sleep(5)
            print("clicked on traffic_layer option to enable")
        self.wait_and_click("(//button[normalize-space()='Submit'])[1]")
        time.sleep(3)
        print("entered all values in locate device and clicked on submit button")

    def time_series_table(self,dashboard_type):
        # TIME SERIES TABLE
        self.driver.execute_script("window.scrollTo(0, 0);")
        # time.sleep(3)
        print("scrolled the page to top")
        self.wait_and_click("(//button[normalize-space()='Panel'])[1]")
        print("clicked on +panel button")
        self.wait_and_click("(//button[normalize-space()='Cancel'])[1]")
        print('clicked on cancel button')
        self.wait_and_click("(//button[normalize-space()='Panel'])[1]")
        print("clicked on +panel button")
        if dashboard_type=='device':
            self.wait_and_click("(//button[@class='ui button add-panel-button'])[9]")
            print("clicked on aggregate value option")
            self.wait_and_click("(//button[normalize-space()='Back'])[1]")
            print('clicked on back button')
            self.wait_and_click("(//button[@class='ui button add-panel-button'])[9]")
            print("clicked on aggregate value option")
        else:
            self.wait_and_click("(//button[@class='ui button add-panel-button'])[6]")
            print("clicked on aggregate value option")
            self.wait_and_click("(//button[normalize-space()='Back'])[1]")
            print('clicked on back button')
            self.wait_and_click("(//button[@class='ui button add-panel-button'])[6]")
            print("clicked on aggregate value option")
        column_disabled=self.driver.find_element(By.XPATH,"(//div[@role='combobox'])[2]")
        class_name=column_disabled.get_attribute('class')
        if 'disabled' in class_name:
                print('column dropdown is disabled which is correct')
        else:
                print('column dropdown is enabled which is incorrect')
        column_disabled=self.driver.find_element(By.XPATH,"(//div[@role='combobox'])[3]")
        class_name=column_disabled.get_attribute('class')
        if 'disabled' in class_name:
                print('column dropdown is disabled which is correct')
        else:
                print('column dropdown is enabled which is incorrect')
        column_disabled=self.driver.find_element(By.XPATH,"(//div[@role='combobox'])[4]")
        class_name=column_disabled.get_attribute('class')
        if 'disabled' in class_name:
                print('column dropdown is disabled which is correct')
        else:
                print('column dropdown is enabled which is incorrect')
        column_disabled=self.driver.find_element(By.XPATH,"(//div[@class='ui disabled left labeled input add-panel-title-input'])[1]")
        class_name=column_disabled.get_attribute('class')
        if 'disabled' in class_name:
                print('column dropdown is disabled which is correct')
        else:
                print('column dropdown is enabled which is incorrect')
        no_data=self.driver.find_element(By.XPATH,"(//div[@class='panel-no-data'])[1]")
        print('no data on the panel')
        # time.sleep(3)
        untitled=self.driver.find_element(By.XPATH,"(//div[@class='bytebeam-panel-title'])[1]")
        print(untitled.text)
        if 'Untitled' in untitled.text:
                print('untitled text is there which is correct')
        else:
                print('untitled text is not there which is incorrect')
        self.wait_and_click("(//button[normalize-space()='Submit'])[1]")
        time.sleep(2)
        toast_message = self.driver.find_element(By.XPATH, "(//div[@role='status'])[1]")
        print(toast_message.text)
        # time.sleep(5)
        self.wait_and_send_keys("(//input[@placeholder='Title'])[1]","TIME SERIES TABLE@123")
        print("entered time series title")
        untitled=self.driver.find_element(By.XPATH,"(//div[@class='bytebeam-panel-title'])[1]")
        print(untitled.text)
        if 'TIME SERIES TABLE@123' in untitled.text:
                print('TIME SERIES TABLE@123 text is there which is correct')
        else:
                print('TIME SERIES TABLE@123 text is not there which is incorrect')
        self.wait_and_send_keys("(//input[@placeholder='Description'])[1]","Description@123")
        print("entered description")
        self.wait_and_send_keys("(//input[@type='text'])[1]","device_shadow" + Keys.RETURN)
        print("entered stream")
        self.wait_and_click("(//button[normalize-space()='Add all columns'])[1]")
        time.sleep(2)
        print("entered add all columns hyperlink")

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # time.sleep(3)
        print("scrolled the page to bottom")
        disabled_section=self.driver.find_element(By.XPATH,"(//div[@role='combobox'])[23]")
        class_name=disabled_section.get_attribute('class')
        if 'disabled' in class_name:
                print('dropdown is disabled')
        else:
                print('dropdown is enabled which is incorrect')
        self.driver.execute_script("window.scrollTo(0, 0);")
        # time.sleep(3)
        print("scrolled the page to top")
        self.wait_and_click("(//i[@class='minus icon'])[3]")
        print("clicked on - icon at the third column")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # time.sleep(3)
        print("scrolled the page to bottom")
        self.wait_and_click("(//button[normalize-space()='Add all columns'])[1]")
        time.sleep(2)
        print("entered add all columns hyperlink")
        disabled_section=self.driver.find_element(By.XPATH,"(//div[@role='combobox'])[23]")
        class_name=disabled_section.get_attribute('class')
        if 'disabled' in class_name:
                print('dropdown is disabled')
        else:
                print('dropdown is enabled which is incorrect')
        self.driver.execute_script("window.scrollTo(0, 0);")
        # time.sleep(3)
        print("scrolled the page to top")
        try:

            table=self.driver.find_element(By.XPATH,"(//table[@class='ui small selectable sortable unstackable compact table'])[1]")
            time.sleep(2)
            print('table is found on preview')
            second_cell = table.find_element(By.XPATH, './/tbody/tr[1]/td[3]')
            second_cell_text = second_cell.text
            print(second_cell_text)
            if 'km' in second_cell_text:
                print("units are there which is incorrect")
            else:
                print("units are not there which is correct")
        except Exception as e:
            print("preview is not coming with data")


        # drag and drop action
        first_sort_icon = self.driver.find_element(By.XPATH, "(//i[@class='sort icon'])[1]")
        third_sort_icon = self.driver.find_element(By.XPATH, "(//i[@class='sort icon'])[2]")
        action_chains = ActionChains(self.driver)

        # Perform the drag-and-drop operation
        action_chains.drag_and_drop(third_sort_icon, first_sort_icon).perform()
        time.sleep(5)
        print("performed the reordering")

        
        #Click on sort toggle
        sort_toggle = self.driver.find_element(By.XPATH, "(//div[@class='ui fitted toggle checkbox'])[1]")
        sort_toggle.click()
        
        time.sleep(2)
        print("clicked on sort toggle")
        # #click on sort on preview
        # sort_preview = self.driver.find_element(By.XPATH, "(//th[@class='descending sorted'])[1]")
        # sort_preview.click()
        
        # time.sleep(5)
        # print("clicked on sort on preview")
        # pagination on preview
        try:
            self.wait_and_click("(//a[normalize-space()='2'])[1]")
            print("clicked on second page")
            self.wait_and_click("(//a[contains(text(),'⟩')])[1]")
            print("clicked on forward_one")
            self.wait_and_click("(//a[normalize-space()='»'])[1]")
            print("clicked on forward_last")
            self.wait_and_click("(//a[contains(text(),'⟨')])[1]")
            print("clicked on backward_one")
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # time.sleep(3)
            print("scrolled the page to bottom")
            self.wait_and_click("(//a[normalize-space()='«'])[1]")
            print("clicked on backward_last")
            self.wait_and_send_keys("(//input[@placeholder='Jump to page...'])[1]","3" + Keys.RETURN)
            print("clicked on jump to")
            self.wait_and_click("(//i[@class='blue redo icon'])[1]")
            print("clicked on blue_redo")
        except Exception as e:
            time.sleep(3)
            print("no data is there")
        # Filtering
        self.wait_and_send_keys("(//input[@type='text'])[24]","range" + Keys.RETURN)
        print("entered filter column")
        self.wait_and_send_keys("(//input[@type='text'])[25]",">" + Keys.RETURN)
        print("entered field column")
        self.wait_and_send_keys("(//input[@placeholder='Value'])[1]","52000" + Keys.RETURN)
        print("entered value column")
        self.wait_and_click("(//button[@class='ui icon primary button'])[1]")
        print("clicked on plus icon")
        self.wait_and_click("(//button[@class='ui icon secondary button'])[1]")
        print("clicked on minus icon")
        self.wait_and_click("(//button[@class='ui icon primary button'])[1]")
        print("clicked on plus icon")
        self.wait_and_send_keys("(//input[@type='text'])[26]","SOC" + Keys.RETURN)
        print("entered filter column")
        self.wait_and_send_keys("(//input[@type='text'])[27]","<" + Keys.RETURN)
        print("entered field column")
        self.wait_and_send_keys("(//input[@placeholder='Value'])[2]","70" + Keys.RETURN)
        print("entered value column")
        self.driver.execute_script("window.scrollTo(0, 0);")
        # time.sleep(3)
        print("scrolled the page to top")
        self.wait_and_click("(//a[normalize-space()='View'])[1]")
        print("clicked on view option")
        enable_units = self.driver.find_element(By.XPATH, "(//label[@for='enableUnits'])[1]")  # Replace 'toggle-checkbox' with the actual ID of the checkbox

        # Check the current state of the checkbox
        if enable_units.is_selected():
            self.wait_and_click("(//label[@for='enableUnits'])[1]")
            print("clicked on enable_units option to disable")
        else:
            self.wait_and_click("(//label[@for='enableUnits'])[1]")
            print("clicked on enable_units option to enable")
        try:
            table=self.driver.find_element(By.XPATH,"(//table[@class='ui small selectable sortable unstackable compact table'])[1]")
            time.sleep(3)
            print('table is found on preview')
            second_cell = table.find_element(By.XPATH, './/tbody/tr[1]/td[3]')
            second_cell_text = second_cell.text
            print(second_cell_text)
            if 'km' in second_cell_text:
                print("units are there which is correct")
            else:
                print("units are not there which is incorrect")
        except Exception as e:
            print("preview is not coming with data")
        self.wait_and_click("(//label[@for='connectNullToggle'])[1]")
        print("clicked on toggle")
        self.wait_and_click("(//button[normalize-space()='Submit'])[1]")
        time.sleep(3)
        print("clicked on submit button")
        
    def histogram(self,dashboard_type):
        #HISTOGRAM
        self.driver.execute_script("window.scrollTo(0, 0);")
        # time.sleep(3)
        print("scrolled the page to top")
        self.wait_and_click("(//button[normalize-space()='Panel'])[1]")
        print("clicked on +panel button")
        self.wait_and_click("(//button[normalize-space()='Cancel'])[1]")
        print('clicked on cancel button')
        self.wait_and_click("(//button[normalize-space()='Panel'])[1]")
        print("clicked on +panel button")
        self.wait_and_click("(//button[@class='ui button add-panel-button'])[10]")
        print("clicked on histogram option")
        self.wait_and_click("(//button[normalize-space()='Back'])[1]")
        print('clicked on back button')
        self.wait_and_click("(//button[@class='ui button add-panel-button'])[10]")
        print("clicked on histogram option")
        column_disabled=self.driver.find_element(By.XPATH,"(//div[@class='ui disabled search selection dropdown'])[1]")
        class_name=column_disabled.get_attribute('class')
        if 'disabled' in class_name:
                print('column dropdown is disabled which is correct')
        else:
                print('column dropdown is enabled which is incorrect')
        no_data=self.driver.find_element(By.XPATH,"(//div[@class='panel-no-data'])[1]")
        print('no data on the panel')
        # time.sleep(3)
        untitled=self.driver.find_element(By.XPATH,"(//div[@class='bytebeam-panel-title'])[1]")
        print(untitled.text)
        if 'Untitled' in untitled.text:
                print('untitled text is there which is correct')
        else:
                print('untitled text is not there which is incorrect')
        self.wait_and_click("(//button[normalize-space()='Submit'])[1]")
        time.sleep(2)
        toast_message = self.driver.find_element(By.XPATH, "(//div[@role='status'])[1]")
        print(toast_message.text)
        # time.sleep(5)
        self.wait_and_send_keys("(//input[@placeholder='Title'])[1]","HISTOGRAM@123")
        print("entered histogram title")
        untitled=self.driver.find_element(By.XPATH,"(//div[@class='bytebeam-panel-title'])[1]")
        print(untitled.text)
        if 'HISTOGRAM@123' in untitled.text:
                print('HISTOGRAM@123 text is there which is correct')
        else:
                print('HISTOGRAM@123 text is not there which is incorrect')
        self.wait_and_send_keys("(//input[@placeholder='Description'])[1]","Description@123")
        print("entered description")
        self.wait_and_send_keys("(//input[@type='text'])[1]","device_shadow" + Keys.RETURN)
        print("entered stream")
        self.wait_and_send_keys("(//input[@type='text'])[2]","range" + Keys.RETURN)
        print("entered column")
        try:
            histo_preview=self.driver.find_element(By.XPATH,"(//*[name()='rect'][@class='nsewdrag drag'])[1]")
            # time.sleep(3)
            print("preview is coming with data")
        except Exception as e:
            print("preview is not coming with data")
        #slider
        slider = self.driver.find_element(By.XPATH, "(//input[@id='typeinp'])[1]")

        # Get the width of the slider element
        slider_width = slider.size['width']

        # Calculate the desired position on the slider (e.g., move it halfway)
        desired_position = slider_width // 2

        # Create an action chain
        action = ActionChains(self.driver)

        # Move the slider to the desired position
        action.click_and_hold(slider).move_by_offset(desired_position, 0).release().perform()
        time.sleep(3)
        print("performed slider action")
        self.wait_and_click("(//button[normalize-space()='Submit'])[1]")
        time.sleep(3)
        print("clicked on submit button")
    
    def logs(self,dashboard_type):
        #LOGS
        self.wait_and_click("(//button[normalize-space()='Panel'])[1]")
        print("clicked on +panel button")
        self.wait_and_click("(//button[normalize-space()='Cancel'])[1]")
        print('clicked on cancel button')
        self.wait_and_click("(//button[normalize-space()='Panel'])[1]")
        print("clicked on +panel button")
        if dashboard_type=='device':
            self.wait_and_click("(//button[@class='ui button add-panel-button'])[11]")
            print("clicked on logs option")
            self.wait_and_click("(//button[normalize-space()='Back'])[1]")
            print('clicked on back button')
            self.wait_and_click("(//button[@class='ui button add-panel-button'])[11]")
            print("clicked on logs option")
        else:
            self.wait_and_click("(//button[@class='ui button add-panel-button'])[7]")
            print("clicked on logs option")
            self.wait_and_click("(//button[normalize-space()='Back'])[1]")
            print('clicked on back button')
            self.wait_and_click("(//button[@class='ui button add-panel-button'])[7]")
            print("clicked on logs option")
        no_data=self.driver.find_element(By.XPATH,"(//div[@class='panel-no-data'])[1]")
        print('no data on the panel')
        # time.sleep(3)
        untitled=self.driver.find_element(By.XPATH,"(//div[@class='bytebeam-panel-title'])[1]")
        print(untitled.text)
        if 'Untitled' in untitled.text:
                print('untitled text is there which is correct')
        else:
                print('untitled text is not there which is incorrect')
        self.wait_and_click("(//button[normalize-space()='Submit'])[1]")
        time.sleep(2)
        toast_message = self.driver.find_element(By.XPATH, "(//div[@role='status'])[1]")
        print(toast_message.text)
        # time.sleep(5)
        self.wait_and_send_keys("(//input[@placeholder='Title'])[1]","LOGS@123")
        print("entered logs title")
        untitled=self.driver.find_element(By.XPATH,"(//div[@class='bytebeam-panel-title'])[1]")
        print(untitled.text)
        if 'LOGS@123' in untitled.text:
                print('LOGS@123 text is there which is correct')
        else:
                print('LOGS@123 text is not there which is incorrect')
        self.wait_and_send_keys("(//input[@placeholder='Description'])[1]","Description@123")
        print("entered description")
        self.wait_and_send_keys("(//input[@type='text'])[1]","device_shadow"+ Keys.RETURN)
        time.sleep(2)
        print("entered stream")
        try:
            logs_preview=self.driver.find_element(By.XPATH,"(//*[name()='rect'][@class='nsewdrag drag'])[1]")
            # time.sleep(3)
            print("preview is coming with data")
        except Exception as e:
            print("preview is not coming with data")
        # search_bar = self.driver.find_element(By.XPATH, "(//label)[1]")  # Replace 'toggle-checkbox' with the actual ID of the checkbox

        # # Check the current state of the checkbox
        # if search_bar.is_selected():
        #     # If it's selected (enabled), click to uncheck and disable it
        #     search_bar.click()
        #     time.sleep(5)
        #     print("clicked on traffic_layer option to disable")
        # else:
        #     # If it's not selected (disabled), click to check and enable it
        #     search_bar.click()
        #     time.sleep(5)
        #     print("clicked on traffic_layer option to enable")

        self.driver.execute_script("window.scrollTo(0, 0);")
        # time.sleep(3)
        print("scrolled the page to top")
        self.wait_and_click("(//a[normalize-space()='View'])[1]")
        print("clicked on view option")
        #slider
        slider = self.driver.find_element(By.XPATH, "(//input[@id='typeinp'])[1]")

        # Get the width of the slider element
        slider_width = slider.size['width']

        # Calculate the desired position on the slider (e.g., move it halfway)
        desired_position = slider_width // 2

        # Create an action chain
        action = ActionChains(self.driver)

        # Move the slider to the desired position
        action.click_and_hold(slider).move_by_offset(desired_position, 0).release().perform()
        time.sleep(3)
        print("performed slider action")
        self.wait_and_click("(//button[normalize-space()='Submit'])[1]")
        time.sleep(3)
        print("entered all values in logs and clicked on submit button")
        self.driver.execute_script("window.scrollTo(0, 0);")
        # time.sleep(3)
        print("scrolled the page to top")

    def static_text(self,dashboard_type):
        #STATIC TEXT
        self.driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)
        print("scrolled the page to top")
        self.wait_and_click("(//button[normalize-space()='Panel'])[1]")
        print("clicked on +panel button")
        self.wait_and_click("(//button[normalize-space()='Cancel'])[1]")
        print('clicked on cancel button')
        self.wait_and_click("(//button[normalize-space()='Panel'])[1]")
        print("clicked on +panel button")
        if dashboard_type=='device':
            self.wait_and_click("(//button[@class='ui button add-panel-button'])[12]")
            print("clicked on static text option")
            self.wait_and_click("(//button[normalize-space()='Back'])[1]")
            print('clicked on back button')
            self.wait_and_click("(//button[@class='ui button add-panel-button'])[12]")
            print("clicked on static text option")
        else:
            self.wait_and_click("(//button[@class='ui button add-panel-button'])[8]")
            print("clicked on static text option")
            self.wait_and_click("(//button[normalize-space()='Back'])[1]")
            print('clicked on back button')
            self.wait_and_click("(//button[@class='ui button add-panel-button'])[8]")
            print("clicked on static text option")
        no_data=self.driver.find_element(By.XPATH,"(//div[@class='panel-no-data'])[1]")
        print('no data on the panel')
        # time.sleep(3)
        untitled=self.driver.find_element(By.XPATH,"(//div[@class='bytebeam-panel-title'])[1]")
        print(untitled.text)
        if 'Untitled' in untitled.text:
                print('untitled text is there which is correct')
        else:
                print('untitled text is not there which is incorrect')
        self.wait_and_click("(//button[normalize-space()='Submit'])[1]")
        time.sleep(2)
        toast_message = self.driver.find_element(By.XPATH, "(//div[@role='status'])[1]")
        print(toast_message.text)
        # time.sleep(5)
        self.wait_and_send_keys("(//input[@placeholder='Title'])[1]","STATIC TEXT@123")
        print("entered static_text title")
        time.sleep(2)
        untitled=self.driver.find_element(By.XPATH,"(//div[@class='bytebeam-panel-title'])[1]")
        print(untitled.text)
        if 'STATIC TEXT@123' in untitled.text:
                print('STATIC TEXT@123 text is there which is correct')
        else:
                print('STATIC TEXT@123 text is not there which is incorrect')
        self.wait_and_send_keys("(//input[@placeholder='Description'])[1]","Description@123")
        print("entered description")
        self.wait_and_send_keys("(//input[@placeholder='Text'])[1]","STATIC TEXT")
        time.sleep(2)
        print("entered static_text title")
        try:
                value=self.driver.find_element(By.XPATH,"(//div[@class='big-number-value'])[1]")
                # time.sleep(3)
                print("value is coming on preview")
        except Exception as e:
                print('data is not coming on preview')
        self.wait_and_click("(//a[normalize-space()='View'])[1]")
        print("clicked on view option")
        self.wait_and_click("(//div[contains(text(),'Normal')])[1]")
        print("clicked on text_drop")
        self.wait_and_click("(//span[normalize-space()='Italic'])[1]")
        print("clicked on italic_text")
        self.wait_and_click("(//div[@id='default_color'])[1]")
        print("clicked on default color")
        self.wait_and_click("(//div[@title='#F8E71C'])[1]")
        print("clicked on color")
        
        #slider
        slider = self.driver.find_element(By.XPATH, "(//input[@id='typeinp'])[1]")

        # Get the width of the slider element
        slider_width = slider.size['width']

        # Calculate the desired position on the slider (e.g., move it halfway)
        desired_position = slider_width // 2

        # Create an action chain
        action = ActionChains(self.driver)

        # Move the slider to the desired position
        action.click_and_hold(slider).move_by_offset(desired_position, 0).release().perform()
        time.sleep(3)
        print("performed slider action")
        self.wait_and_click("(//button[normalize-space()='Submit'])[1]")
        time.sleep(3)
        print("entered all values in logs and clicked on submit button")
        self.driver.execute_script("window.scrollTo(0, 0);")
        # time.sleep(3)
        print("scrolled the page to top")

    def bar_chart(self,dashboard_type):
        # #BAR CHART
        self.driver.execute_script("window.scrollTo(0, 0);")
        # time.sleep(3)
        print("scrolled the page to top")
        self.wait_and_click("(//button[normalize-space()='Panel'])[1]")
        print("clicked on +panel button")
        self.wait_and_click("(//button[normalize-space()='Cancel'])[1]")
        print('clicked on cancel button')
        self.wait_and_click("(//button[normalize-space()='Panel'])[1]")
        print("clicked on +panel button")
        if dashboard_type=='device':
            self.wait_and_click("(//button[@class='ui button add-panel-button'])[13]")
            print("clicked on bar chart option")
            self.wait_and_click("(//button[normalize-space()='Back'])[1]")
            print('clicked on back button')
            self.wait_and_click("(//button[@class='ui button add-panel-button'])[13]")
            print("clicked on bar chart option")
        else:
            self.wait_and_click("(//button[@class='ui button add-panel-button'])[9]")
            print("clicked on bar chart option")
            self.wait_and_click("(//button[normalize-space()='Back'])[1]")
            print('clicked on back button')
            self.wait_and_click("(//button[@class='ui button add-panel-button'])[9]")
            print("clicked on bar chart option")
        column_disabled=self.driver.find_element(By.XPATH,"(//div[@elementid='groupBarChart'])[1]")
        class_name=column_disabled.get_attribute('class')
        if 'disabled' in class_name:
                print('column dropdown is disabled which is correct')
        else:
                print('column dropdown is enabled which is incorrect')
        

        operator_disabled=self.driver.find_element(By.XPATH,"(//div[@elementid='fieldBarChart'])[1]")
        class_name=operator_disabled.get_attribute('class')
        if 'disabled' in class_name:
                print('operator dropdown is disabled which is correct')
        else:
                print('operator dropdown is enabled which is incorrect')

        operator_disabled=self.driver.find_element(By.XPATH,"(//div[@elementid='aggregatorBarChart'])[1]")
        class_name=operator_disabled.get_attribute('class')
        if 'disabled' in class_name:
                print('operator dropdown is disabled which is correct')
        else:
                print('operator dropdown is enabled which is incorrect')

        no_data=self.driver.find_element(By.XPATH,"(//div[@class='panel-no-data'])[1]")
        print('no data on the panel')
        # time.sleep(3)
        untitled=self.driver.find_element(By.XPATH,"(//div[@class='bytebeam-panel-title'])[1]")
        print(untitled.text)
        if 'Untitled' in untitled.text:
                print('untitled text is there which is correct')
        else:
                print('untitled text is not there which is incorrect')
        self.wait_and_click("(//button[normalize-space()='Submit'])[1]")
        time.sleep(2)
        toast_message = self.driver.find_element(By.XPATH, "(//div[@role='status'])[1]")
        print(toast_message.text)
        # time.sleep(5)
        self.wait_and_send_keys("(//input[@placeholder='Title'])[1]","BAR CHART@123")
        print("entered static_text title")
        time.sleep(2)
        untitled=self.driver.find_element(By.XPATH,"(//div[@class='bytebeam-panel-title'])[1]")
        print(untitled.text)
        if 'BAR CHART@123' in untitled.text:
                print('BAR CHART@123 text is there which is correct')
        else:
                print('BAR CHART@123 text is not there which is incorrect')
        self.wait_and_send_keys("(//input[@placeholder='Description'])[1]","Description@123")
        print("entered description")
        self.wait_and_send_keys("(//input[@type='text'])[1]","device_shadow" + Keys.RETURN)
        print("entered stream")
        operator_disabled=self.driver.find_element(By.XPATH,"(//div[@elementid='fieldBarChart'])[1]")
        class_name=operator_disabled.get_attribute('class')
        if 'disabled' in class_name:
                print('operator dropdown is disabled which is correct')
        else:
                print('operator dropdown is enabled which is incorrect')

        operator_disabled=self.driver.find_element(By.XPATH,"(//div[@elementid='aggregatorBarChart'])[1]")
        class_name=operator_disabled.get_attribute('class')
        if 'disabled' in class_name:
                print('operator dropdown is disabled which is correct')
        else:
                print('operator dropdown is enabled which is incorrect')
        self.wait_and_send_keys("(//input[@type='text'])[2]","firmware_version" + Keys.RETURN)
        print("entered group by field")
        

        operator_disabled=self.driver.find_element(By.XPATH,"(//div[@elementid='aggregatorBarChart'])[1]")
        class_name=operator_disabled.get_attribute('class')
        if 'disabled' in class_name:
                print('operator dropdown is disabled which is correct')
        else:
                print('operator dropdown is enabled which is incorrect')
        self.wait_and_send_keys("(//input[@type='text'])[3]","range" + Keys.RETURN)
        print("entered aggregate by field")
        self.wait_and_send_keys("(//input[@type='text'])[4]","sum" + Keys.RETURN)
        time.sleep(2)
        print("entered aggregator field")
        try:
            logs_preview=self.driver.find_element(By.XPATH,"(//*[name()='rect'][@class='nsewdrag drag'])[1]")
            # time.sleep(3)
            print("preview is coming with data")
        except Exception as e:
            print("preview is not coming with data")
        self.wait_and_click("(//a[normalize-space()='View'])[1]")
        print("clicked on view option")
        self.wait_and_send_keys("(//input[@placeholder='Min*'])[1]","20")
        print("entered min_val")
        self.wait_and_click("(//button[normalize-space()='Submit'])[1]")
        time.sleep(2)
        toast_message = self.driver.find_element(By.XPATH, "(//div[@role='status'])[1]")
        print(toast_message.text)
        # time.sleep(5)
        self.wait_and_send_keys("(//input[@placeholder='Max*'])[1]","100")
        print("entered max_val")
        self.wait_and_click("(//button[normalize-space()='Submit'])[1]")
        time.sleep(3)
        print("entered all values in bar chart and clicked on submit button")
        self.driver.execute_script("window.scrollTo(0, 0);")
        # time.sleep(3)
        print("scrolled the page to top")

    def custom_time_range(self):
        #custom time range
        
        last_five = self.driver.find_element(By.XPATH, "(//div[@class='ui button selection dropdown'])[1]")
        print(last_five.text)
        self.wait_and_click("(//div[@class='ui button selection dropdown'])[1]")
        print("clicked on last five minutes")
        self.wait_and_click("(//span[normalize-space()='Custom Time Range'])[1]")
        print("clicked on custom_time")
        self.wait_and_click("(//i[@class='chevron right fitted icon'])[1]")
        print("clicked on first_forward")
        self.wait_and_click("(//i[@class='chevron left fitted icon'])[1]")
        print("clicked on first_backward")
        self.wait_and_click("(//i[@class='chevron right fitted icon'])[2]")
        print("clicked on second_forward")
        self.wait_and_click("(//i[@class='chevron left fitted icon'])[2]")
        print("clicked on second_backward")
        self.wait_and_click("(//div[@id='from_dropdown'])[1]")
        print("clicked on minutes_ago")
        self.wait_and_click("(//div[@role='option'][normalize-space()='30 minutes ago'])[1]")
        print("clicked on 30 minutes_ago")
        
        input_box = self.driver.find_element(By.XPATH, "(//input[@value='30'])[1]")
        # input_box.send_keys(Keys.COMMAND, "A")
        self.driver.execute_script("arguments[0].value = '';", input_box)
        self.wait_and_send_keys("(//input[@value='30'])[1]","45")
        print("entered on input_box")
        self.wait_and_click("(//div[@id='to_dropdown'])[1]")
        print("clicked on seconds_ago")
        self.wait_and_click("(//div[@role='option'][normalize-space()='10 minutes ago'])[2]")
        print("clicked on 10 minutes_ago")
        
        input_box = self.driver.find_element(By.XPATH, "(//input[@value='10'])[1]")
        # input_box.send_keys(Keys.COMMAND, "A")
        self.driver.execute_script("arguments[0].value = '';", input_box)
        self.wait_and_send_keys("(//input[@value='10'])[1]","12")
        print("entered on input_box")
        self.wait_and_click("(//label[@for='showSaveCustomTimeRangeToggle'])[1]")
        print("clicked on toggle")
        custom_box = self.driver.find_element(By.XPATH, "(//input[@placeholder='Custom Time Range Label'])[1]")
        custom_name_one = '45 to 12 for {}'.format(random.randint(1,100))
        self.wait_and_send_keys("(//input[@placeholder='Custom Time Range Label'])[1]",custom_name_one)
        print("entered on custom_box")
        self.wait_and_click("(//button[normalize-space()='Apply'])[1]")
        print("clicked on apply_button")
        time.sleep(3)
        self.wait_and_click("(//div[@class='ui button selection dropdown'])[1]")
        print("clicked on last five minutes")
        self.wait_and_click("(//span[normalize-space()='Custom Time Range'])[1]")
        print("clicked on custom_time")
        
        # nine_text = self.driver.find_element(By.XPATH, "(//span[contains(text(),'9')])[1]")
        # nine_text.click()
        # time.sleep(3)
        # print("clicked on nine_text")

        
        # wait = WebDriverWait(self.driver, 10)
        
        # wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[contains(text(),'9')])[1]"))).click()
        # time.sleep(2)
        # print("clicked on nine_text")

        #new addition
        # Wait for the table to load (adjust timeout as needed)
        wait = WebDriverWait(self.driver, 10)
        table = wait.until(EC.presence_of_element_located((By.XPATH, "(//table[@class='ui celled unstackable center aligned table'])[1]")))  # Replace 'table-id' with the ID of your table
        print("table located")

        # Find the row containing the chosen value
        rows = table.find_elements(By.TAG_NAME, 'tr')
        
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, 'td')
            
            # print(cells)
            for cell in cells:
                print(cell.text)
                if cell.text=="14":
                    
                        
                        
                        span_element = cell.find_element(By.TAG_NAME, 'span')
                        span_element.click()
                        print("clicked on cell")
                        time.sleep(2)
                        break
                else:
                        continue
                    
                    
            else:
                continue
            break


        


        self.wait_and_click("(//span[normalize-space()='09:00'])[1]")
        print("clicked on nine_o_text")
        self.wait_and_click("(//span[normalize-space()='09:00'])[1]")
        print("clicked on nine_o_text")

        
        # twenty_eight_text = self.driver.find_element(By.XPATH, "(//span[contains(text(),'28')])[2]")
        # twenty_eight_text.click()
        # time.sleep(3)
        # print("clicked on twenty_eight_text")

        #new addition
        # Wait for the table to load (adjust timeout as needed)
        wait = WebDriverWait(self.driver, 10)
        table = wait.until(EC.presence_of_element_located((By.XPATH, "(//table[@class='ui celled unstackable center aligned table'])[2]")))  # Replace 'table-id' with the ID of your table
        print("table located")

        # Find the row containing the chosen value
        rows = table.find_elements(By.TAG_NAME, 'tr')
        
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, 'td')
            
            # print(cells)
            for cell in cells:
                print(cell.text)
                if cell.text=="18":
                    
                        
                        
                        span_element = cell.find_element(By.TAG_NAME, 'span')
                        span_element.click()
                        print("clicked on cell")
                        time.sleep(2)
                        break
                else:
                        continue
                    
                    
            else:
                continue
            break


        

        self.wait_and_click("(//span[normalize-space()='14:00'])[1]")
        print("clicked on fourteen_text")
        self.wait_and_click("(//span[normalize-space()='14:00'])[1]")
        print("clicked on fourteen_text")
        self.wait_and_click("(//label[@for='showSaveCustomTimeRangeToggle'])[1]")
        print("clicked on toggle")
        self.wait_and_click("(//button[normalize-space()='Apply'])[1]")
        time.sleep(2)
        print("clicked on apply_button")
        toast_message = self.driver.find_element(By.XPATH, "(//div[@role='status'])[1]")
        print(toast_message.text)
        # time.sleep(5)
        custom_box = self.driver.find_element(By.XPATH, "(//input[@placeholder='Custom Time Range Label'])[1]")
        custom_name_two = 'new_custom{}'.format(random.randint(1,100))
        self.wait_and_send_keys("(//input[@placeholder='Custom Time Range Label'])[1]",custom_name_two)
        print("entered on custom_box")
        self.wait_and_click("(//button[normalize-space()='Apply'])[1]")
        print("clicked on apply_button")
        time.sleep(3)
        self.wait_and_click("(//div[@class='ui button selection dropdown'])[1]")
        print("clicked on last five minutes")
        self.wait_and_click("(//span[normalize-space()='Custom Time Range'])[1]")
        print("clicked on custom_time")
        self.wait_and_click("(//label[@for='showSaveCustomTimeRangeToggle'])[1]")
        print("clicked on toggle")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # time.sleep(3)
        print("scrolled the page to bottom")
        delete_custom_name = custom_name_two+'_delete'
        print(delete_custom_name)
        self.wait_and_click("(//i[@id='{}'])[1]".format(delete_custom_name))
        print("clicked on close_icon")
        cancel_custom_name = custom_name_two+'_cancel'
        self.wait_and_click("(//i[@id='{}'])[1]".format(cancel_custom_name))
        print("clicked on second_close_icon")

        delete_custom_name = custom_name_two+'_delete'
        self.wait_and_click("(//i[@id='{}'])[1]".format(delete_custom_name))
        print("clicked on deleteicon")

        confirm_custom_name = custom_name_two+'_confirm'
        self.wait_and_click("(//i[@id='{}'])[1]".format(confirm_custom_name))
        print("clicked on second confirm icon")
        time.sleep(2)
        
        delete_custom_name = custom_name_one+'_delete'
        self.wait_and_click("(//i[@id='{}'])[1]".format(delete_custom_name))
        print("clicked on delete icon")

        confirm_custom_name = custom_name_one+'_confirm'
        self.wait_and_click("(//i[@id='{}'])[1]".format(confirm_custom_name))
        print("clicked on first confirm icon")
        self.wait_and_click("(//button[normalize-space()='Cancel'])[1]")
        time.sleep(2)
        print("clicked on cancel")

    def device_pulse(self,dashboard_type):
        self.wait_and_click("(//button[normalize-space()='Panel'])[1]")
        print("clicked on +panel button")
        self.wait_and_click("(//button[normalize-space()='Cancel'])[1]")
        print('clicked on cancel button')
        self.wait_and_click("(//button[normalize-space()='Panel'])[1]")
        print("clicked on +panel button")
        self.wait_and_click("(//button[@class='ui button add-panel-button'])[10]")
        print("clicked on bar chart option")
        self.wait_and_click("(//button[normalize-space()='Back'])[1]")
        print('clicked on back button')
        self.wait_and_click("(//button[@class='ui button add-panel-button'])[10]")
        print("clicked on bar chart option")
        try:
            no_data=self.driver.find_element(By.XPATH,"(//div[@class='panel-no-data'])[1]")
            print('no data on the panel')
            # time.sleep(3)
        except Exception as e:
            print("data is coming which is incorrect")
        untitled=self.driver.find_element(By.XPATH,"(//div[@class='bytebeam-panel-title'])[1]")
        print(untitled.text)
        if 'Untitled' in untitled.text:
                print('untitled text is there which is correct')
        else:
                print('untitled text is not there which is incorrect')
        self.wait_and_send_keys("(//input[@placeholder='Title'])[1]","DEVICE PULSE@123")
        print("entered dev_pulse title")
        untitled=self.driver.find_element(By.XPATH,"(//div[@class='bytebeam-panel-title'])[1]")
        print(untitled.text)
        if 'DEVICE PULSE@123' in untitled.text:
                print('DEVICE PULSE@123 text is there which is correct')
        else:
                print('DEVICE PULSE@123 text is not there which is incorrect')
        self.wait_and_send_keys("(//input[@placeholder='Description'])[1]","Description@123")
        print("entered description")
        self.wait_and_send_keys("(//input[@type='text'])[1]","device_shadow" + Keys.RETURN)
        threshold1 = self.driver.find_element(By.XPATH, "(//input[@placeholder='Threshold 1'])[1]")
        # threshold1.send_keys(Keys.COMMAND, "A")
        self.driver.execute_script("arguments[0].value = '';", threshold1)
        # time.sleep(2)
        self.wait_and_send_keys("(//input[@placeholder='Threshold 1'])[1]","100")
        threshold2 = self.driver.find_element(By.XPATH, "(//input[@placeholder='Threshold 2'])[1]")
        # threshold2.send_keys(Keys.COMMAND, "A")
        self.driver.execute_script("arguments[0].value = '';", threshold2)
        # time.sleep(2)
        self.wait_and_send_keys("(//input[@placeholder='Threshold 2'])[1]","600")
        threshold3 = self.driver.find_element(By.XPATH, "(//input[@placeholder='Threshold 3'])[1]")
        # threshold3.send_keys(Keys.COMMAND, "A")
        self.driver.execute_script("arguments[0].value = '';", threshold3)
        # time.sleep(2)
        self.wait_and_send_keys("(//input[@placeholder='Threshold 3'])[1]","6000")
        threshold4 = self.driver.find_element(By.XPATH, "(//input[@placeholder='Threshold 4'])[1]")
        # threshold4.send_keys(Keys.COMMAND, "A")
        self.driver.execute_script("arguments[0].value = '';", threshold4)
        # time.sleep(2)
        self.wait_and_send_keys("(//input[@placeholder='Threshold 4'])[1]","36000")
        threshold5 = self.driver.find_element(By.XPATH, "(//input[@placeholder='Threshold 5'])[1]")
        # threshold5.send_keys(Keys.COMMAND, "A")
        self.driver.execute_script("arguments[0].value = '';", threshold5)
        # time.sleep(2)
        self.wait_and_send_keys("(//input[@placeholder='Threshold 5'])[1]","864000")
        print("entered stream")
        time.sleep(30)
        try:
            target_element = self.driver.find_element(By.XPATH, "(//div[@id='7_#2fc76a'])[1]")
            print("identified the element")

            # Click on the element
            self.driver.execute_script("arguments[0].click();", target_element)
            # time.sleep(1)
            # toast_message = self.driver.find_element(By.XPATH, "(//div[@class='toast toast-error'])[1]")
            # print(toast_message.text)
            time.sleep(2)
        except Exception as e:
            time.sleep(2)
            print("not working correctly")

        try:
        
        
            target_element = self.driver.find_element(By.XPATH, "(//span[@id='#2fc76a'])[1]")
            action_chains = ActionChains(self.driver)
            
            # Perform a click action on the element
            action_chains.click(target_element).perform()
            print("clicked on the number")
            # time.sleep(1)
            # toast_message = self.driver.find_element(By.XPATH, "(//div[@class='toast toast-error'])[1]")
            # print(toast_message.text)
            time.sleep(2)
            self.wait_and_click("(//button[normalize-space()='Download Metadata'])[1]")
            print("clicked on download metadata")

            self.wait_and_send_keys("(//input[@type='text'])[2]","311 - Device Dashboard" + Keys.RETURN)
            # pagination
            # second_page = self.driver.find_element(By.XPATH, "(//a[normalize-space()='2'])[1]")
            # second_page.click()
            # time.sleep(3)
            # print("clicked on second page")
            self.wait_and_click("(//a[contains(text(),'⟩')])[1]")
            print("clicked on forward_one")
            self.wait_and_click("(//a[normalize-space()='»'])[1]")
            print("clicked on forward_last")
            self.wait_and_click("(//a[contains(text(),'⟨')])[1]")
            print("clicked on backward_one")
            self.wait_and_click("(//a[normalize-space()='«'])[1]")
            print("clicked on backward_last")
            number_element = self.driver.find_element(By.CSS_SELECTOR, "tbody tr:nth-child(1) td:nth-child(1)")
            print("identified the element")

            # Click on the element
            # self.driver.execute_script("arguments[0].click();", target_element)
            action_chains = ActionChains(self.driver)

            # Perform a click action on the element
            action_chains.click(number_element).perform()
            print("clicked on the number")
            # time.sleep(5)
            self.wait_and_click("(//button[normalize-space()='Close'])[1]")
            print("clicked on close button")
            self.wait_and_send_keys("(//input[@placeholder='Description'])[1]","desc")
            time.sleep(6)
            print("entered dev_pulse desc")
            # fleet_dashboard.send_keys("37 - Simulator tables")
            # fleet_dashboard.send_keys(Keys.RETURN)
            # time.sleep(2)
            # fleet_dashboard.send_keys("67 - Testers")
            # fleet_dashboard.send_keys(Keys.RETURN)
            # time.sleep(3)
            print("entered dashboard values")
            try:
            
                target_element = self.driver.find_element(By.XPATH, "(//div[@id='7_#2fc76a'])[1]")
                print("identified the element")

                # Click on the element
                # self.driver.execute_script("arguments[0].click();", target_element)
                wait = WebDriverWait(self.driver, 10)
                # target_element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath_expression)))
                target_element = self.driver.find_element(By.XPATH, "(//div[@id='7_#2fc76a'])[1]")
                target_element.click()
                # time.sleep(1)
                # toast_message = self.driver.find_element(By.XPATH, "(//div[@class='toast toast-error'])[1]")
                # print(toast_message.text)
                time.sleep(3)
                print("clicked on the color")
            except Exception as e:
                time.sleep(5)
                print("not working correctly")
        except Exception as e:
            print("the panel itself is not loading")
        
        self.wait_and_click("(//button[normalize-space()='Submit'])[1]")
        time.sleep(3)
        print("entered all values in device pulse and clicked on submit button")
        self.driver.execute_script("window.scrollTo(0, 0);")
        # time.sleep(3)
        print("scrolled the page to top")

    def sessions(self,dashboard_type, session_name):
        self.wait_and_click("(//button[normalize-space()='Panel'])[1]")
        print("clicked on +panel button")
        self.wait_and_click("(//button[normalize-space()='Cancel'])[1]")
        print('clicked on cancel button')
        self.wait_and_click("(//button[normalize-space()='Panel'])[1]")
        print("clicked on +panel button")
        if dashboard_type=='device':
            self.wait_and_click("(//button[@class='ui button add-panel-button'])[15]")
            print("clicked on bar chart option")
            self.wait_and_click("(//button[normalize-space()='Back'])[1]")
            print('clicked on back button')
            self.wait_and_click("(//button[@class='ui button add-panel-button'])[15]")
            print("clicked on bar chart option")
        else:
            self.wait_and_click("(//button[@class='ui button add-panel-button'])[12]")
            print("clicked on sessions option")
            self.wait_and_click("(//button[normalize-space()='Back'])[1]")
            print('clicked on back button')
            self.wait_and_click("(//button[@class='ui button add-panel-button'])[12]")
            print("clicked on sessions option")
        column_disabled=self.driver.find_element(By.XPATH,"(//div[@role='combobox'])[3]")
        class_name=column_disabled.get_attribute('class')
        if 'disabled' in class_name:
                print('field dropdown is disabled which is correct')
        else:
                print('field dropdown is enabled which is incorrect')
        

        operator_disabled=self.driver.find_element(By.XPATH,"(//div[@role='combobox'])[4]")
        class_name=operator_disabled.get_attribute('class')
        if 'disabled' in class_name:
                print('aggregator dropdown is disabled which is correct')
        else:
                print('aggregator dropdown is enabled which is incorrect')

        no_data=self.driver.find_element(By.XPATH,"(//div[@class='panel-no-data'])[1]")
        print('no data on the panel')
        # time.sleep(3)
        untitled=self.driver.find_element(By.XPATH,"(//div[@class='bytebeam-panel-title'])[1]")
        print(untitled.text)
        if 'Untitled' in untitled.text:
                print('untitled text is there which is correct')
        else:
                print('untitled text is not there which is incorrect')
        self.wait_and_click("(//button[normalize-space()='Submit'])[1]")
        time.sleep(2)
        toast_message = self.driver.find_element(By.XPATH, "(//div[@role='status'])[1]")
        print(toast_message.text)
        # time.sleep(5)
        self.wait_and_send_keys("(//input[@placeholder='Title'])[1]","SESSIONS@123")
        print("entered static_text title")
        time.sleep(2)
        untitled=self.driver.find_element(By.XPATH,"(//div[@class='bytebeam-panel-title'])[1]")
        print(untitled.text)
        if 'BAR CHART@123' in untitled.text:
                print('BAR CHART@123 text is there which is correct')
        else:
                print('BAR CHART@123 text is not there which is incorrect')
        self.wait_and_send_keys("(//input[@placeholder='Description'])[1]","Description@123")
        print("entered description")
        self.wait_and_send_keys("(//input[@type='text'])[1]",session_name + Keys.RETURN)
        print("entered stream")
        self.wait_and_send_keys("(//input[@placeholder='Aggregate Name'])[1]","agg@123")
        print("entered aggregator name")
        self.wait_and_send_keys("(//input[@type='text'])[1]","device_shadow" + Keys.RETURN)
        print("entered stream")



        operator_disabled=self.driver.find_element(By.XPATH,"(//div[@role='combobox'])[4]")
        class_name=operator_disabled.get_attribute('class')
        if 'disabled' in class_name:
                print('aggregator dropdown is disabled which is correct')
        else:
                print('aggregator dropdown is enabled which is incorrect')

        self.wait_and_send_keys("(//input[@type='text'])[3]","range" + Keys.RETURN)
        print("entered group by field")
        self.wait_and_send_keys("(//input[@type='text'])[4]","sum" + Keys.RETURN)
        print("entered aggregate by field")
        time.sleep(2)
        try:
            logs_preview=self.driver.find_element(By.XPATH,"(//th[normalize-space()='agg@123'])[1]")
            # time.sleep(3)
            print("preview is coming with data")
        except Exception as e:
            print("preview is not coming with data")

        self.wait_and_click("(//button[@class='ui icon primary button'])[1]")
        print("clicked on plus icon")
        self.wait_and_click("(//i[@class='minus icon'])[2]")
        print("clicked on plus icon")
        self.wait_and_click("(//button[@class='ui icon primary button'])[1]")
        print("clicked on plus icon")


        self.wait_and_send_keys("(//input[@placeholder='Aggregate Name'])[2]","agg@12345")
        print("entered aggregator name")



        column_disabled=self.driver.find_element(By.XPATH,"(//div[@role='combobox'])[6]")
        class_name=column_disabled.get_attribute('class')
        if 'disabled' in class_name:
                print('field dropdown is disabled which is correct')
        else:
                print('field dropdown is enabled which is incorrect')
        

        operator_disabled=self.driver.find_element(By.XPATH,"(//div[@role='combobox'])[7]")
        class_name=operator_disabled.get_attribute('class')
        if 'disabled' in class_name:
                print('aggregator dropdown is disabled which is correct')
        else:
                print('aggregator dropdown is enabled which is incorrect')

        self.wait_and_send_keys("(//input[@type='text'])[5]","device_shadow" + Keys.RETURN)
        print("entered stream")
        

        operator_disabled=self.driver.find_element(By.XPATH,"(//div[@role='combobox'])[7]")
        class_name=operator_disabled.get_attribute('class')
        if 'disabled' in class_name:
                print('aggregator dropdown is disabled which is correct')
        else:
                print('aggregator dropdown is enabled which is incorrect')

        self.wait_and_send_keys("(//input[@type='text'])[6]","SOC" + Keys.RETURN)
        print("entered group by field")
        self.wait_and_send_keys("(//input[@type='text'])[7]","avg" + Keys.RETURN)
        print("entered aggregate by field")
        time.sleep(2)
        try:
            logs_preview=self.driver.find_element(By.XPATH,"(//th[normalize-space()='agg@12345'])[1]")
            # time.sleep(3)
            print("preview is coming with data")
        except Exception as e:
            print("preview is not coming with data")

        self.wait_and_send_keys("(//input[@type='text'])[8]","Vehicle Dashboard" + Keys.RETURN)
        print("entered group by field")

        try:
            logs_preview=self.driver.find_element(By.XPATH,"(//th[normalize-space()='Dashboards'])[1]")
            # time.sleep(3)
            print("preview is coming with data")
        except Exception as e:
            print("preview is not coming with data")

        
        self.wait_and_click("(//button[normalize-space()='Submit'])[1]")
        time.sleep(3)
        print("entered all values in sessions panel and clicked on submit button")
        self.driver.execute_script("window.scrollTo(0, 0);")
        # time.sleep(3)
        print("scrolled the page to top")

    def add_phase(self,action_type,action_name,flag,phased, metadata_key, second_metadata_key):
        try:
            name = metadata_key
            second_name = second_metadata_key
            actions_tab = self.driver.find_element(By.LINK_TEXT, "Actions")
            actions_tab.click()
            time.sleep(3)
            print("clicked on actions tab")
            self.driver.execute_script("window.scrollTo(0, 0);")
            # time.sleep(3)
            print("scrolled the page to top")
            self.wait_and_click("(//button[normalize-space()='Add Phase'])[1]")
            print("clicked on add phase button")
            self.wait_and_click("(//button[normalize-space()='Discard'])[1]")
            print("clicked on discard button")
            self.wait_and_click("(//button[normalize-space()='Add Phase'])[1]")
            print("clicked on add phase button")
            # self.new_action_pagination_check('add_phase')
            #Display section
            self.wait_and_click("(//button[normalize-space()='Display'])[1]")
            print("clicked on desktop icon")
            self.wait_and_click("(//h3[normalize-space()='{}'])[1]".format(name))
            print("clicked on metadata key option")
            self.wait_and_click("(//i[@class='desktop icon'])[1]")
            print("clicked on desktop icon")
            time.sleep(3)
            try:
                metadata = self.driver.find_element(By.XPATH,"(//th[normalize-space()='{}'])[1]".format(name))
                print("metadata key is getting added")
            except Exception as e:
                print("metadata key is not getting added which is incorrect")
            self.wait_and_click("(//button[normalize-space()='Display'])[1]")
            print("clicked on desktop icon")
            self.wait_and_click("(//h3[normalize-space()='{}'])[1]".format(name))
            print("clicked on metadata key option")
            self.wait_and_click("(//i[@class='desktop icon'])[1]")
            print("clicked on desktop icon")
            time.sleep(3)
            try:
                metadata = self.driver.find_element(By.XPATH,"(//th[normalize-space()='{}'])[1]".format(name))
                print("metadata key is not getting removed in second phase which is incorrect")
            except Exception as e:
                print("metadata key is getting removed in second phase which is correct")
                time.sleep(2)
            if action_type == "update_firmware" and phased=='phased':
                self.wait_and_click("(//button[normalize-space()='Filters'])[1]")
                print("clicked on filters option")
                time.sleep(2)
                self.wait_and_send_keys("(//input[@id='search-action-filters-input'])[1]",name)
                self.wait_and_click("(//div[@id='metadata-name-{}-0'])[1]".format(name))
                # # elements=self.driver.find_elements(By.XPATH, "(//div[@id='dropdown-wrapper'])[1]")
                
                # # elements[-1].click()
                # option_locator = "(//div[normalize-space()='{}'])[1]".format(name)
                # option = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, option_locator)))
                # option.click()
                # time.sleep(2)
                # print("clicked on metadata key option")

                # # self.wait_and_click("(//i[@class='filter icon'])[3]")
                # # print("clicked on filters option")
                
                # # self.wait_and_click("(//div[normalize-space()='{}'])[1]".format(name))
                # # time.sleep(2)
                checkbox = self.driver.find_element(By.XPATH,"(//label[@for='metadata-dropdown-value-1'])[1]")
                # checkbox.click()
                self.driver.execute_script("arguments[0].click();", checkbox)
                time.sleep(2)
                print("clicked on first checkbox")
                self.wait_and_click("(//i[@id='phase-modal-add-filters-button'])[1]")
                print("clicked on plus icon")
                self.wait_and_send_keys("(//input[@id='search-action-filters-input'])[1]",second_name)
                self.wait_and_click("(//div[@id='metadata-name-{}-0'])[1]".format(second_name))
                checkbox = self.driver.find_element(By.XPATH,"(//label[@for='metadata-dropdown-value-0'])[1]")
                # checkbox.click()
                self.driver.execute_script("arguments[0].click();", checkbox)
                time.sleep(2)
                print("clicked on first checkbox")
                self.wait_and_click("(//i[@class='close icon'])[2]")
                print("clicked on cross icon")
                try:
                    icon=self.driver.find_element(By.XPATH,"(//i[@class='file icon'])[2]")
                    print("icon is there which is incorrect")
                    info_icon=self.driver.find_element(By.XPATH,"(//i[@class='info circle icon'])[2]")
                    print("icon is there which is incorrect")
                    # time.sleep(2)
                except Exception as e:
                    # time.sleep(2)
                    print("icons are not found which is correct")
                self.wait_and_click("(//i[@id='phase-modal-add-filters-button'])[1]")
                self.wait_and_send_keys("(//input[@id='search-action-filters-input'])[1]",second_name)
                self.wait_and_click("(//div[@id='metadata-name-{}-0'])[1]".format(second_name))
                checkbox = self.driver.find_element(By.XPATH,"(//label[@for='metadata-dropdown-value-0'])[1]")
                # checkbox.click()
                self.driver.execute_script("arguments[0].click();", checkbox)
                time.sleep(2)
                print("clicked on first checkbox")
                self.wait_and_click("(//h3[normalize-space()='Clear All'])[1]")
                print("clicked on clear all hyperlink")
                time.sleep(3)
                first_page_action_id = self.driver.find_element(By.XPATH,"(//table[@class='ui celled selectable table'])[1]//tr[1]/td[2]")
                first_page_action_id_text=first_page_action_id.text
                print(first_page_action_id_text)
                first_page_action_id_text_int=int(first_page_action_id_text)
                print(first_page_action_id_text_int)
                if first_page_action_id_text_int!=4:
                    print("clear all hyperlink is functioning properly which is correct")
                else:
                    print("clear all hyperlink is not functioning properly which is incorrect")

                    
                    
            self.wait_and_click("(//button[normalize-space()='Filters'])[1]")
            print("clicked on filters option")
            time.sleep(2)
            self.wait_and_send_keys("(//input[@id='search-action-filters-input'])[1]",name)
            self.wait_and_click("(//div[@id='metadata-name-{}-0'])[1]".format(name))
            # # elements=self.driver.find_elements(By.XPATH, "(//div[@id='dropdown-wrapper'])[1]")
            
            # # elements[-1].click()
            # option_locator = "(//div[normalize-space()='{}'])[1]".format(name)
            # option = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, option_locator)))
            # option.click()
            # time.sleep(2)
            # print("clicked on metadata key option")

            # # self.wait_and_click("(//i[@class='filter icon'])[3]")
            # # print("clicked on filters option")
            
            # # self.wait_and_click("(//div[normalize-space()='{}'])[1]".format(name))
            # # time.sleep(2)
            checkbox = self.driver.find_element(By.XPATH,"(//label[@for='metadata-dropdown-value-1'])[1]")
            # checkbox.click()
            self.driver.execute_script("arguments[0].click();", checkbox)
            time.sleep(2)
            print("clicked on first checkbox")
            self.wait_and_click("(//i[@id='phase-modal-add-filters-button'])[1]")
            self.wait_and_send_keys("(//input[@id='search-action-filters-input'])[1]",second_name)
            self.wait_and_click("(//div[@id='metadata-name-{}-0'])[1]".format(second_name))
            checkbox = self.driver.find_element(By.XPATH,"(//label[@for='metadata-dropdown-value-0'])[1]")
            # checkbox.click()
            self.driver.execute_script("arguments[0].click();", checkbox)
            time.sleep(2)
            print("clicked on first checkbox")
            checkbox = self.driver.find_element(By.XPATH, "//tbody/tr[1]/td[1]/div[1]/input[1]")
            # self.driver.execute_script("arguments[0].checked = true;", checkbox)
            # checkbox.send_keys(Keys.SPACE)
            self.driver.execute_script("arguments[0].click();", checkbox)
            
            time.sleep(2)
            print("clicked on checkboxes")
            self.wait_and_click("(//button[normalize-space()='Submit'])[1]")
            time.sleep(3)
            print("clicked on submit button")
            try:
                if phased =='phased':
                    phase7= self.driver.find_element(By.XPATH,"(//button[normalize-space()='Phase VII'])[1]")
                    print("phase 7 is found")
                else:
                    phase2= self.driver.find_element(By.XPATH,"(//button[normalize-space()='Phase II'])[1]")
                    print("phase 2 is found")
            except Exception as e:
                print("phase 7 or 2 is not found which is incorrect")
            self.wait_and_click("(//i[@title='More details'])[1]")
            print("clicked on eye icon")
            if phased =='phased':
                self.wait_and_click("(//button[normalize-space()='Phase VII'])[1]")
                print("clicked on phase 7")
            else:
                self.wait_and_click("(//button[normalize-space()='Phase II'])[1]")
                print("clicked on phase 2")
            time.sleep(3)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # time.sleep(3)
            print("scrolled the page to bottom")
            # Wait for the table to load (adjust timeout as needed)
            wait = WebDriverWait(self.driver, 10)
            table = wait.until(EC.presence_of_element_located((By.XPATH, "(//table[@class='ui selectable table sc-kMHJlo jPaBpe'])[1]")))  # Replace 'table-id' with the ID of your table
            print("table located")

            # Find the row containing the chosen value
            rows = table.find_elements(By.TAG_NAME, 'tr')
            if len(rows)<1:
                print("rows might have gotten added in some other phase because of same devices")
            else:
                list1=[]
                for i in range(len(rows)):

                    first_page_action_id = self.driver.find_element(By.XPATH,"(//table[@class='ui selectable table sc-kMHJlo jPaBpe'])[1]//tr[1]/td[1]")
                    first_page_action_id_text=first_page_action_id.text
                    list1.append(first_page_action_id_text)
            if '4' in list1 or '5' in list1 or '6' in list1:
                print("devices are coming correctly in the add phase section which is correct")
            elif '4' in list1 and '5' in list1 and '6' in list1:
                print("all devices are coming correctly in the add phase section which is correct")
            else:
                print("rows might have gotten added in some other phase because of same devices")

        except Exception as e:
            exception_type = type(e).__name__
            exc_info = sys.exc_info()
            line_number = exc_info[2].tb_lineno
            print(f"e1. Exception type: {exception_type}")
            print(f"e2. Line number: {line_number}")
            file_name = 'add_phase_in_user_account.png'
            directory_path = 'Screenshots'
            if not os.path.exists(directory_path):
                os.makedirs(directory_path)
            file_path = os.path.abspath(os.path.join(directory_path, file_name))
            self.driver.get_screenshot_as_file(file_path)
            pytest.record_property("screenshot", file_path)  # Record the screenshot path in the report
            self.driver.refresh()
            time.sleep(10)
            print('refreshed the page')
            
            
            self.driver.execute_script("window.scrollTo(0, 0);")
            time.sleep(3)
            print("scrolled the page to top")
            raise e
        

    def delete_dashboard(self, name):
        try:
            device_mg_tab = self.driver.find_element(By.LINK_TEXT, "Device Management")
            device_mg_tab.click()
            time.sleep(5)
            print("clicked on device managememnt tab")

            dash_button = self.driver.find_element(By.LINK_TEXT, "Dashboards")
            dash_button.click()
            time.sleep(5)
            print("clicked on dashboards tab")
            chosen_value = name

            # Wait for the table to load (adjust timeout as needed)
            wait = WebDriverWait(self.driver, 10)
            table = wait.until(EC.presence_of_element_located((By.XPATH, "(//table[@class='ui celled fixed selectable sortable table responsive-table'])[1]")))  # Replace 'table-id' with the ID of your table
            print("table located")

            # Find the row containing the chosen value
            rows = table.find_elements(By.TAG_NAME, 'tr')
            # print(rows)
            i=0
            for row in rows:
                cells = row.find_elements(By.TAG_NAME, 'td')
                
                # print(cells)
                for cell in cells:
                    if chosen_value in cell.text:
                        # Click on the edit icon in the same row
                        if i==0:
                            delete_icon = self.driver.find_element(By.XPATH, '//body[1]/div[2]/div[2]/div[3]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[{}]/td[5]/i[2]'.format(i+1))  # Replace 'edit-icon-class' with the class of your edit icon
                            
                            delete_icon.click()
                            print("clicked on delete icon")
                            time.sleep(3)
                            break
                        else:
                            delete_icon = self.driver.find_element(By.XPATH, '//body[1]/div[2]/div[2]/div[3]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[{}]/td[5]/i[2]'.format(i))  # Replace 'edit-icon-class' with the class of your edit icon
                            
                            delete_icon.click()
                            print("clicked on delete icon")
                            time.sleep(3)
                            break
                        
                        
                else:
                    i=i+1
                    continue
                break
            confirm_button = self.driver.find_element(By.XPATH, "(//button[normalize-space()='Confirm'])[1]")
            icon_class_name = confirm_button.get_attribute('class')
            if 'disabled' in icon_class_name:
                print("icon is disabled")
            else:
                print("icon is not disabled")
            self.wait_and_send_keys("(//input[@type='text'])[1]",name)
            print("enetered the name")
            self.wait_and_click("(//button[normalize-space()='Confirm'])[1]")
            time.sleep(3)
            print("deleted the dashboard")

        except Exception as e:
            exception_type = type(e).__name__
            exc_info = sys.exc_info()
            line_number = exc_info[2].tb_lineno
            print(f"e1. Exception type: {exception_type}")
            print(f"e2. Line number: {line_number}")
            file_name = 'delete_dev_dashboard.png'
            directory_path = 'Screenshots'
            if not os.path.exists(directory_path):
                os.makedirs(directory_path)
            file_path = os.path.abspath(os.path.join(directory_path, file_name))
            self.driver.get_screenshot_as_file(file_path)
            pytest.record_property("screenshot", file_path)  # Record the screenshot path in the report
            self.driver.refresh()
            time.sleep(10)
            print('refreshed the page')






        
        

        
