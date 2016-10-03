import time
from selenium import webdriver
from selenium.webdriver.common.by import By


# logging into SSO
class scrape_uvaps:
    def __init__(self):
        self.compIDS = []
        self.letterList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                           's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.init_drivers()
        self.change_page()
        self.write_results()

    def init_drivers(self):
        drivers = []
        [drivers.append('driver_' + letterList[a]) for a in range(len(letterList))]
        drivers = webdriver.Chrome('C:/Python35/chromedriver.exe')

        driver = webdriver.Chrome('C:/Python35/chromedriver.exe')
        driver.get('https://search.people.virginia.edu/search?combine=')
        username_input = driver.find_element_by_name('user')
        password_input = driver.find_element_by_name('pass')
        submit_input = driver.find_element_by_xpath('//*[@id="loginBoxes"]/fieldset[2]/span[2]/form/p[3]/input[1]')
        username = user
        password = pw
        username_input.send_keys(username)
        password_input.send_keys(password)
        submit_input.submit()
        return drivers

    def change_page(self):
        # take search through each letter because blank search is 400 page limited
        i = 0
        while i <= 25:
            compIDS = []
            pageNum = 0
            letter = letterList[i]
            i += 1
            while True:
                # retrieve page
                driver.get('https://search.people.virginia.edu/search?combine=' + letter + '&page=' + str(pageNum))
                # find all links to ids
                search = driver.find_elements(By.XPATH, '//body//a[contains(@href,"person")]')
                # clean links by removing everthing but the ids
                for el in search:
                    try:
                        text = el.text
                        clean = text[text.index("(") + 1:text.rindex(")")]
                        print(clean)
                        compIDS.append(clean)
                    except ValueError:
                        continue
                print('*********    ' + str(pageNum) + '  *********')
                pageNum += 1
                if pageNum > 399:
                    break

    def write_results(self):
        # remove duplicates
        compIDS = list(set(compIDS))

        # Write id list to file
        resultFile = open('UVACOMPIDS2', 'w')
        for rows in range(len(compIDS)):
            resultFile.write(compIDS[rows] + '\n')


scrape_uvaps()


#TODO: Gather names from classes

#TODO: Object orient

#TODO: Goto each UVA Comp ID profile and retrieve profile info

#TODO: Categorize persons (Undergraduate, First year)
