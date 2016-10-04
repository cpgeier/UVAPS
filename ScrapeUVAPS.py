'''
Christopher Geier Presents:

A method to download a list of everyone's email, username, and name at the University of Virginia.

A UVA Computing ID and password is needed to access the database.
Use data responsibly.
'''

import time
from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.common.by import By


class Interface:
    def __init__(self):
        print('----- Christopher Geier Presents -----')
        time.sleep(2)
        print('\n\n' + '      Everyone        ' + '\n\n')
        time.sleep(1)
        while True:
            print('Press 1 to scrape everyones computing ID.')
            print('Press 2 to process and combine scraped IDs.')
            print('Press 3 to retrieve everyones profile information.')
            self.i = input('Please Enter Option: ')
            self.username = input('Please enter UVa Username: ')
            self.password = input('Please enter UVa Password: ')
            self.letterList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                               's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
            if self.i == 1:
                UVAPSComputerIDS(self.username, self.password, self.letterList)
            elif self.i == 2:
                CleanLetterSets()
            elif self.i == 3:
                profiles = input('Enter name of profiles file: ')
                file = open(str(profiles), 'r')
                filetext = file.read()
                profilelist = filetext.split('\n')
                UVAPSProfileInfo(self.username, self.password, profilelist)
            else:
                print('Unrecognized Input...')


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
        pbar = tqdm(total=400)
        while page_num < 400:
            # TODO: Exit on null result
            # retrieve page
            pbar.update(1)
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
        # intermediate_file = open('foobar','w')
        # intermediate_file.write(self.compIDS)
        # intermediate_file.close()
        print('***** File write completed for letter ' + self.letter + ' *****')
        return self.compIDS

    # def results(self):
    #     return self.compIDS


class CleanLetterSets:
    def __init__(self):
        self.letterList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                           's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.completeList = []
        print('***** Importing Sets *****')
        self.import_sets()
        self.completeList = list(set(self.completeList))
        final_file = open('UVA_IDS', 'w')
        final_file.write(str(self.completeList))
        final_file.close()
        print('***** Final list export complete *****')

    def import_sets(self):
        """ Builds complete list from letter files """
        for i in range(len(self.letterList)):
            a = open(self.letterList[i])
            atext = a.readlines()
            for ind in range(len(atext)):
                atext[ind] = atext[ind].rstrip()
            self.completeList.extend(atext)
            print('***** Import for letter ' + self.letterList[i] + ' completed *****')


class UVAPSProfileInfo:
    def __init__(self, username, password, compids):
        self.driver = webdriver.Chrome('C:/Python35/chromedriver.exe')
        self.username = username
        self.password = password
        self.login_sso()
        self.a = []

        for profile in tqdm(compids):
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
        print('***** Writing File *****')
        final_file = open('All_Profiles', 'w')
        for rows in range(len(self.a)):
            final_file.write(str(self.a[rows]) + '\n')
            print('     Row ' + str(rows) + ' complete    ')
        print('***** File Write Complete *****')
