from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

# or you can set driver in PATH

driver.set_page_load_timeout(5)
driver.maximize_window()
driver.get("https://rvision.exadel.com")

driver.find_element_by_xpath("//input[@type='text'][@name='loginForm:login']").send_keys("amazur")
driver.find_element_by_xpath("//input[@type='password'][@name='loginForm:password']").send_keys("Password12")
driver.find_element_by_xpath("//input[@type='submit'][@name='loginForm:j_idt39']").click()

time.sleep(2)

driver.find_element_by_xpath("//a[text()='Add new Time Off']").click()
time.sleep(2)
driver.find_element_by_xpath("//a[text()='Show available Time Offs ▼']").click()

#el = driver.find_element_by_id("timeoff_edit_panel_container")
#print(el)
time.sleep(2)
el = (driver.find_element_by_xpath("//table[2]/tbody/tr[2]/td/table/tbody/tr/td[4]"))
print (el.text)
#driver.switchTo().frame("frame_viewport");

time.sleep(10)




#driver.find_element_by_xpath("//table[2]/tbody/tr[2]/td/table/tbody/tr/td[4]")

#driver.quit()
