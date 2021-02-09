# from selenium import webdriver
#
# # Mac and linux:
# driver = webdriver.Chrome(executable_path="/Users/arnonbrouner/Downloads/chromedriver")
# driver.implicitly_wait(10) # wait upto 10 sec to find_element(s) functions
# # functions get - load a new webpage in the current browser window
# driver.get("https://translate.google.com")
# # current_url -the url you are on
# #print(driver.current_url)
# # title - the title of thr webpage
# #print(driver.title)
# # page_source - the source of tha page
# #print(driver.page_source)
#
# # find elements
# # find element
# # close - close current tab x on the tab if you only have one its quit
# # quit - close all tabs and the session clean all webdriver resorces
# #driver.quit()
# # navigation
# # back ,forward,refresh - just like on the browser
# # driver.back
#
# # Locators -- find elemet(s) by the attributes below.
# # ID
# # NAme
# # LinkText
# # PartialLinkText
# # ClassName
# # Xpath
# # driver.find_element(s)_by_name()
# # history_elements = driver.find_elements_by_link_text("History")
# # for elem in history_elements
# #     print(elem)
#
# text_elements = driver.find_element_by_class_name("er8xn")
# text_elements.send_keys("hello")
# text_elements.send_keys((keys.ENTER))
# text_elements.send_keys(('C\users\1.jpg') # upload a file
# if text_elements.is_enabled():
#     print("the element is enabled")
#
#
# roll_attribute = text_elements.get_attribute("roll")
# print(len(text_elements))
# #driver.quit()
# # Xpath
# # find element in side the xml path tree
#
# # controllers
# #botton
# #radio button
# #checkbix
# #list
# #Datepicker
# #
#
# #synchronization
# #speed of the code Vs site speed
# #unconditional syn - using sleep BAD PRACTICE
# #conditional syn - drive.implicitly_wait(10) any place in the code where you use find_elemeent(s) wait up to 10 sec
# # there is also explicitly_wait for a specific element
#
