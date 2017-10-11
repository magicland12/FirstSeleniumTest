from selenium import webdriver
import re


driver = webdriver.Chrome()
driver.get('http://www.airindia.in/contact-details.htm')

doc = driver.page_source

emails = re.findall(r'[\w\.-]+@[\w\.-]+', doc)
for email in emails:
    print(email)



    # for phone numbers use this structure: phones with structure: (999) 999-9999
    # phones = re.findall(r'[(][\d]{3}[)][]?[\d]{3}-[\d]{4}',doc)