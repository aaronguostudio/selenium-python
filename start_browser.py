#coding=utf-8
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.5itest.cn/register")
print("-------------")
print(EC.title_contains("注册"))

# element = driver.find_element_by_class_name("controls")
locator = (By.CLASS_NAME, "controls")

WebDriverWait(driver, 1).until(EC.visibility_of_element_located(locator))

driver.find_element_by_id("register_email").send_keys("aaronguostudio@gmail.com")
user_name_element_node = driver.find_elements_by_class_name("controls")[1]
user_element = user_name_element_node.find_element_by_class_name("form-control")
user_element.send_keys("aaronguo")
driver.find_element_by_name("password").send_keys("password1")
driver.find_element_by_xpath("//*[@id='register_password']").send_keys("password2")

driver.close()
driver.quit()
