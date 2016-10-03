from selenium import webdriver
from selenium.webdriver.common.by import By

# logging into SSO
letterList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
              'u', 'v', 'w', 'x', 'y', 'z']
drivers = []
[drivers.append('driver_' + letterList[a]) for a in range(len(letterList))]

for inds in range(len(drivers)):
    inds = webdriver.Chrome('C:/Python35/chromedriver.exe')
    inds.get('https://google.com/')

'''
driver = webdriver.Chrome('C:/Python35/chromedriver.exe')  # Optional argument, if not specified will search path.
driver.get('https://search.people.virginia.edu/search?combine=')
username_input = driver.find_element_by_name('user')
password_input = driver.find_element_by_name('pass')
submit_input = driver.find_element_by_xpath('//*[@id="loginBoxes"]/fieldset[2]/span[2]/form/p[3]/input[1]')
username = input('Enter computing ID: ')
password = input('Enter computing ID password: ')
username_input.send_keys(username)
password_input.send_keys(password)
submit_input.submit()
'''
