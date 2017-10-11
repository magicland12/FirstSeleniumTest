import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://rvision.exadel.com')

ids=[]

ids = driver.find_elements_by_xpath('//*[@id]')

for ii in ids:
    print(ii.get_attribute('id'))

time.sleep(4)

driver.close()