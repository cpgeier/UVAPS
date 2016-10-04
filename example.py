"""
Christopher Geier Presents:

Initializing ScrapeUVAPS
"""

import ScrapeUVAPS

username = input('Enter Computing ID Username: ')
password = input('Enter Computing ID Password: ')

file = open('listcomp','r')
fileText = file.read()
profileList = fileText.split('\n')

ScrapeUVAPS.UVAPSProfileInfo(username, password, profileList)