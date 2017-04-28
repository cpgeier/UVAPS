'''
Christopher Geier Presents:

A method to download a list of everyone's email, username, and name at the University of Virginia.

A UVA Computing ID is needed to access the database.
Use data responsibly.
'''

from selenium import webdriver
from selenium.webdriver.common.by import By


class UVAPSComputerIDS:
    def __init__(self, user, pw, thread_letter):
        self.letter = thread_letter
        self.username = user
        self.password = pw
        self.compIDS = []
        self.letterList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                           's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.driver = webdriver.Chrome('C:/Python35/chromedriver.exe')
        self.login_sso()
        self.change_page()
        self.write_results()

    def login_sso(self):
        print('***** Initializing WebDriver *****')
        self.driver.get('https://search.people.virginia.edu/search?combine=')
        username_input = self.driver.find_element_by_name('user')
        password_input = self.driver.find_element_by_name('pass')
        submit_input = self.driver.find_element_by_xpath('//*[@id="loginBoxes"]/fieldset[2]/span[2]/form/p[3]/input[1]')

        username_input.send_keys(self.username)
        password_input.send_keys(self.password)
        submit_input.submit()

    def change_page(self):
        # take search through each letter because blank search is 400 page limited
        page_num = 0
        while page_num < 399:
            # retrieve page
            self.driver.get('https://search.people.virginia.edu/search?combine=' + self.letter + '&page=' +
                            str(page_num))
            # find all links to ids
            search = self.driver.find_elements(By.XPATH, '//body//a[contains(@href,"person")]')

            # clean links by removing everthing but the ids
            for el in search:
                try:
                    text = el.text
                    clean = text[text.index("(") + 1:text.rindex(")")]
                    self.compIDS.append(clean)
                except ValueError:
                    continue
            print('Search: ' + self.letter + '   Page number: ' + str(page_num))
            page_num += 1

    def write_results(self):
        # remove duplicates
        print('***** Writing File *****')
        self.compIDS = list(set(self.compIDS))
        # Write id list to file
        result_file = open(self.letter, 'w')
        for rows in range(len(self.compIDS)):
            result_file.write(self.compIDS[rows] + '\n')
        print('***** File write completed for letter ' + self.letter + ' *****')
        return self.compIDS

class UVAPSProfileInfo:
    def __init__(self, username, password, compids):
        self.driver = webdriver.Chrome('C:/Python35/chromedriver.exe')
        self.login_sso()
        self.username = username
        self.password = password
        self.a = []
        for profile in compids:
            self.a.append(self.profile_info(profile))
        self.save()

    def login_sso(self):
        ''' Logs into SSO '''
        print('***** Initializing WebDriver *****')
        self.driver.get('https://search.people.virginia.edu/search?combine=')
        username_input = self.driver.find_element_by_name('user')
        password_input = self.driver.find_element_by_name('pass')
        submit_input = self.driver.find_element_by_xpath('//*[@id="loginBoxes"]/fieldset[2]/span[2]/form/p[3]/input[1]')

        username_input.send_keys(self.username)
        password_input.send_keys(self.password)
        submit_input.submit()

    def profile_info(self, profile_name):
        ''' Scrapes profile and returns dictionary of profile elements '''

        self.driver.get('https://search.people.virginia.edu/person/' + profile_name)

        attribute_search = self.driver.find_elements(By.XPATH, '//body//div[contains(@class,"attribute")]')
        attributes = []
        for att in attribute_search:
            text = att.text
            attributes.append(text)
        attributes = attributes[1:]
        attributes = dict(attributes[i:i + 2] for i in range(0, len(attributes), 2))

        name_search = self.driver.find_elements(By.XPATH, '//body//h3')
        name = []
        for nm in name_search:
            text = nm.text
            name.append(text)
        name = str(name[0])
        name = name[0:name.rindex("(")]

        attributes['Name'] = name
        attributes['Profile'] = profile_name
        return attributes

    def save(self):
        final_file = open('Total', 'w')
        for rows in range(len(self.a)):
            final_file.write(self.a[rows] + '\n')
