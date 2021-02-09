# Write a program that does the following:
# 1. Using Selenium Webdriver write a script which will open
# the below browsers on the following URL:
# a. Chrome – http://www.walla.co.il
# b. FireFox – http://www.ynet.co.il
#
# from selenium import webdriver
# # # Mac and linux:
# from selenium.webdriver.common.keys import Keys
#
# driver = webdriver.Chrome(executable_path="/Users/arnonbrouner/Downloads/chromedriver")
# # driver.implicitly_wait(10) # wait upto 10 sec to find_element(s) functions
# # # functions get - load a new webpage in the current browser window
# driver.get("http://www.walla.co.il")
# driver.quit()

# 2. In one of the browsers you open, do the following:
# a. Create a variable with the website’s title
# b. Refresh website
# c. Get website title again and compare it to the variable you
# created in clause 1.
#
# from selenium import webdriver
# # # Mac and linux:
# from selenium.webdriver.common.keys import Keys
#
# driver = webdriver.Chrome(executable_path="/Users/arnonbrouner/Downloads/chromedriver")
# # driver.implicitly_wait(10) # wait upto 10 sec to find_element(s) functions
# # # functions get - load a new webpage in the current browser window
# driver.get("http://www.walla.co.il")
# title = driver.title
# driver.refresh()
# title2 = driver.title
# if (title2 == title) :
#     print('titles match')
# else:
#     print('tiles dont match')
#
# #driver.quit()


# 3. Open a few browsers, locate any element in the same
# website, does the element has the same locators in all the
# browsers?
#
# from selenium import webdriver
# # # Mac and linux:
# from selenium.webdriver.common.keys import Keys
# drv1 = webdriver.Chrome(executable_path="/Users/arnonbrouner/Downloads/chromedriver")
# drv1.implicitly_wait(10)
# drv2 = webdriver.Chrome(executable_path="/Users/arnonbrouner/Downloads/chromedriver")
# drv2.implicitly_wait(10)
# drv3 = webdriver.Chrome(executable_path="/Users/arnonbrouner/Downloads/chromedriver")
# drv3.implicitly_wait(10)
#
# drv1.get("http://www.walla.co.il")
# drv2.get("http://www.walla.co.il")
# drv3.get("http://www.walla.co.il")
# #
# drv1.find_element_by_class_name('css-2wk1yz no-mobile')
# drv2.find_element_by_class_name('css-2wk1yz no-mobile')
# drv3.find_element_by_class_name('css-2wk1yz no-mobile')


# 4. Create a test with the following:
# • Open Google Translate (https://translate.google.com) web page
# • Write anything in Hebrew in the text area
#
# from selenium import webdriver
# # # # Mac and linux:
# from selenium.webdriver.common.keys import Keys
# driver = webdriver.Chrome(executable_path="/Users/arnonbrouner/Downloads/chromedriver")
# txt = 'שלום זה קורס פאיטון'
# driver.get("https://translate.google.com")
# driver.find_element_by_class_name("er8xn").send_keys(txt)

# 5.
# • Open Youtube web page (https://www.youtube.com)
# • Type a name of a song in the search box
# • Click on search button.
#
# from selenium import webdriver
# # # # Mac and linux:
# from selenium.webdriver.common.keys import Keys
# driver = webdriver.Chrome(executable_path="/Users/arnonbrouner/Downloads/chromedriver")
# txt = 'Tom & jerry'
# driver.get("https://www.youtube.com")
# driver.find_element_by_id("search").send_keys(txt)
# driver.find_element_by_id("search-icon-legacy").click()


# 6.
# • Open Chrome browser on Google Translate website:
# https://translate.google.com/
# • Find translation text field (the one you send keys to)
# with 3 different locators and print the WebElement
# you created (e.g: print(web_element)).
#
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# driver = webdriver.Chrome(executable_path="/Users/arnonbrouner/Downloads/chromedriver")
# driver.get("https://translate.google.com")
# txt = 'Arnon'
# print(driver.find_element_by_class_name("er8xn"))
# print(driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[1]/span/span/div/textarea'))
# print(driver.find_element_by_tag_name('textarea'))


# 7.
# • Open Chrome browser on Facebook website
# https://www.facebook.com/
# • Login into Facebook (No need to send me credentials).
#
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# driver = webdriver.Chrome(executable_path="/Users/arnonbrouner/Downloads/chromedriver")
# driver.get("https://facebook.com")
#
# driver.find_element_by_id("email").send_keys('your email address')
# driver.find_element_by_id("pass").send_keys('your pass')
# driver.find_element_by_id("u_0_b").click()


# CHALLENGES:
# 8.
# • Open Chrome browser on any webpage.
# • Delete all cookies from browser.
# • Make sure all cookies are deleted by printing all
# cookies stored in the browser.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path="/Users/arnonbrouner/Downloads/chromedriver")
driver.get("https://facebook.com")
all_cookies = driver.get_cookies()
print(all_cookies)
print(len(all_cookies))
for cky in all_cookies :
    print(cky['name'] + ' Is going to be deleted ')
    driver.delete_cookie(cky['name'])
#
# 9.
# • Open any browser on "Github" website.
# • https://github.com/
# • Enter “Selenium” keyword in search textfield
# • Press Enter to search (through code - of course).
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# driver = webdriver.Chrome(executable_path="/Users/arnonbrouner/Downloads/chromedriver")
# txt = 'Selenium'
# driver.get("https://github.com/")
# driver.find_element_by_name("q").send_keys(txt)
# driver.find_element_by_name("q").send_keys(Keys.ENTER)
