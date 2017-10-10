from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()


# or you can set driver in PATH

driver.set_page_load_timeout(5)
driver.get("https://rvision.exadel.com")
driver.maximize_window()
driver.find_element_by_xpath("//input[@type='text'][@name='loginForm:login']").send_keys("amazur")
driver.find_element_by_xpath("//input[@type='password'][@name='loginForm:password']").send_keys("Password12")
driver.find_element_by_xpath("//input[@type='submit'][@name='loginForm:j_idt39']").click()

time.sleep(2)

driver.find_element_by_xpath("//span[text()='Reports']").click()
driver.find_element_by_xpath("//span[text()='Time Offs']").click()


#driver.quit()



