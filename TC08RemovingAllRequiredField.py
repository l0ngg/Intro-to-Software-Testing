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

class TestTC08Removingallrequiredfield():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_tC08Removingallrequiredfield(self, username, password):
    self.driver.get("https://localhost/moodle/")
    self.driver.find_element(By.LINK_TEXT, "Log in").click()
    self.driver.find_element(By.ID, "username").click()
    self.driver.find_element(By.ID, "username").clear()
    self.driver.find_element(By.ID, "username").send_keys(username)
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "password").send_keys(password)
    self.driver.find_element(By.ID, "loginbtn").click()
    WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.XPATH, "//span[contains(.,\'Software Testing\')]")))
    self.driver.find_element(By.NAME, "setmode").click()
    WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.XPATH, "//span[contains(.,\'Software Testing\')]")))
    self.driver.find_element(By.XPATH, "//span[contains(.,\'Software Testing\')]").click()
    
    WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.XPATH, "//li[2]/div/div/div[2]/div/div/div/div/a")))
    time.sleep(3)
    self.driver.find_element(By.XPATH, "//li[2]/div/div/div[2]/div/div/div/div/a").click()
    
    WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "Edit settings")))
    time.sleep(3)
    self.driver.find_element(By.ID, "actionmenuaction-8").click()
    
    self.driver.find_element(By.ID, "id_name").click()
    self.driver.find_element(By.ID, "id_name").send_keys("a")
    self.driver.find_element(By.XPATH, "//a/div/div[3]").click()
    WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.XPATH, "//form/div/button[2]")))
    self.driver.find_element(By.XPATH, "//form/div/button[2]").click()
    WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.XPATH, "//p[contains(.,\'Are you sure you want to delete this file?\')]")))
    self.driver.find_element(By.XPATH, "//button[@class=\'fp-dlg-butconfirm btn-primary btn\']").click()
    self.driver.find_element(By.ID, "id_submitbutton").click()
    assert self.driver.find_element(By.ID, "id_error_name").text == "- You must supply a value here."
    self.driver.find_element(By.ID, "id_name").click()
    self.driver.find_element(By.ID, "id_name").send_keys("emptyfiletest")
    self.driver.find_element(By.ID, "id_submitbutton").click()
    assert self.driver.find_element(By.ID, "id_error_files").text == "Required "
    
    WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.ID, "user-menu-toggle")))
    time.sleep(3)
    self.driver.find_element(By.CSS_SELECTOR, ".userinitials").click()
    self.driver.find_element(By.LINK_TEXT, "Log out").click()
    elements = self.driver.find_elements(By.LINK_TEXT, "Log in")
    assert len(elements) > 0

if __name__ == '__main__':
  file1 = open("login_credentials.json")
  
  login = json.load(file1)
  
  testcase8 = TestTC08Removingallrequiredfield()
  testcase8.setup_method(1)
  
  testcase8.test_tC08Removingallrequiredfield(login["username"], login["password"])
  
  testcase8.teardown_method(1)