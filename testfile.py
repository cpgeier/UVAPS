from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('C:/Python35/chromedriver.exe')
driver.get('https://search.people.virginia.edu/search?combine=')
username_input = driver.find_element_by_name('user')
password_input = driver.find_element_by_name('pass')
submit_input = driver.find_element_by_xpath('//*[@id="loginBoxes"]/fieldset[2]/span[2]/form/p[3]/input[1]')

username_input.send_keys('')
password_input.send_keys('')
submit_input.submit()
driver.get('https://search.people.virginia.edu/person/cpg3rb')

search = driver.find_elements(By.XPATH,'//body//a[contains(@href,"@Virginia.EDU")]')

emails = []

for el in search:
    text = el.text
    emails.append(text)
emails = str(emails[0])
print(emails)

search2 = driver.find_elements(By.XPATH,'//body//div[contains(@class,"attribute")]')
attributes = []
for el in search2:
    text = el.text
    attributes.append(text)
attributes = attributes[1:]
attributes = dict(attributes[i:i+2] for i in range(0, len(attributes), 2))
print(attributes)

search3 = driver.find_elements(By.XPATH,'//body//h3')
name = []
for el in search3:
    text = el.text
    name.append(text)
name = str(name[0])
name = name[0:name.rindex("(")]
print(name)

attributes['Name'] = name
print(attributes)
#['', 'UVA Computing ID:', 'cpg3rb', 'Classification:', 'Undergraduate Student', 'Department:', 'Engineering Undergraduate-genu', 'Department Code:', 'Engineering Undergraduate-genu', 'Primary Email Address:', 'cpg3rb@Virginia.EDU', 'Registered Email Address:', 'cpg3rb@virginia.edu']
