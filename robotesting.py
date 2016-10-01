from robobrowser import RoboBrowser
import time

browser = RoboBrowser(history=True,parser='lxml')

#browser.open('https://search.people.virginia.edu/search?combine=')
#browser.follow_link(link="https://collab.itc.virginia.edu/portal/relogin?containerLogin=true")
browser.open("https://shibidp.its.virginia.edu/idp/profile/SAML2/POST/SSO")
browser.open(login_url)

form = browser.get_form(action="index.cgi")

print(form)
form['user'].value = 'cpg3rb'
form['pass'].value = 'Kbz?2[Qx'

browser.submit_form(form)
print(browser)
time.sleep(5)
browser.open('https://search.people.virginia.edu/search?combine=')
print(browser)


#print(li)