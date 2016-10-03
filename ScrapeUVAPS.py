import threading
from selenium import webdriver
from selenium.webdriver.common.by import By


class ScrapeUVAPS:
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

        username_input.send_keys(username)
        password_input.send_keys(password)
        submit_input.submit()

    def change_page(self):
        # take search through each letter because blank search is 400 page limited
        page_num = 0
        while page_num > 399:
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
        result_file = open('UVACOMPIDS2', 'w')
        for rows in range(len(self.compIDS)):
            result_file.write(self.compIDS[rows] + '\n')
        print('***** File write completed for letter ' + self.letter + ' *****')


#TODO: Gather names from classes

#TODO: Object orient

#TODO: Goto each UVA Comp ID profile and retrieve profile info

#TODO: Categorize persons (Undergraduate, First year)
