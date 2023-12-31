# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestHanyamengisidataemaildanmengosongkandatapassword():
  def setup_method(self, method):
    self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_hanyamengisidataemaildanmengosongkandatapassword(self):
    # Test name: Hanya mengisi data email dan mengosongkan data password
    # Step # | name | target | value
    # 1 | open | / | 
    self.driver.get("https://shopee.co.id/")
    # 2 | setWindowSize | 656x680 | 
    self.driver.set_window_size(656, 680)
    # 3 | mouseOver | css=.stardust-carousel__item:nth-child(2) .VNlkcn | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".stardust-carousel__item:nth-child(2) .VNlkcn")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 4 | mouseOver | css=.wpHTxX:nth-child(2) .\_9puaeP | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".wpHTxX:nth-child(2) .\\_9puaeP")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 5 | runScript | window.scrollTo(0,0) | 
    self.driver.execute_script("window.scrollTo(0,0)")
    # 6 | click | linkText=Log In | 
    self.driver.find_element(By.LINK_TEXT, "Log In").click()
    # 7 | type | name=loginKey | ev10n9un66
    self.driver.find_element(By.NAME, "loginKey").send_keys("ev10n9un66")
  
