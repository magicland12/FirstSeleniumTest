from selenium import webdriver
driver = webdriver.Chrome()
driver.get('http://google.com')


try:
    driver.find_element_by_tag_name('form')
    print('Passed test: tag name found')

except Exception as e:
    print('exception found', format(e))