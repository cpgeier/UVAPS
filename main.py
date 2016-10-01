from bs4 import BeautifulSoup
import urllib.request

import time
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
import random

driver = webdriver.Chrome('C:/Python35/chromedriver.exe')  # Optional argument, if not specified will search path.
driver.get('https://search.people.virginia.edu/search?combine=')

username_input = driver.find_element_by_name('user')
password_input = driver.find_element_by_name('pass')
submit_input = driver.find_element_by_xpath('//*[@id="loginBoxes"]/fieldset[2]/span[2]/form/p[3]/input[1]')
username = 'cpg3rb'
password = 'Kbz?2[Qx'
username_input.send_keys(username)
password_input.send_keys(password)
submit_input.submit()
#Alert(driver).accept()
compIDS = []
letterList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
              'v', 'w', 'x', 'y', 'z']
i = 0
while i <= 25:
    pageNum = 0
    letter = letterList[i]
    i += 1
    while True:
        driver.get('https://search.people.virginia.edu/search?combine=' + letter + '&page=' + str(pageNum))
        search = driver.find_elements(By.XPATH, '//body//a[contains(@href,"person")]')
        for el in search:
            try:
                text = el.text
                clean = text[text.index("(") + 1:text.rindex(")")]
                print(clean)
                compIDS.append(clean)
            except ValueError:
                continue
        print('*********    ' + str(pageNum) + '  *********')
        #rand = random.uniform(1, 5)
        #time.sleep(rand)
        pageNum += 1
        if pageNum > 399:
            break

compIDS = list(set(compIDS))


print(compIDS)
f = open('UVACOMPIDS','w')
f.write(compIDS)
f.close()


#link = driver.find_element_by_xpath("//*[@href]").text
#print(link.get_attribute('href'))

time.sleep(3)
driver.quit()
