from selenium import webdriver

#
# # Mac and linux:
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="/Users/arnonbrouner/Downloads/chromedriver")
driver.implicitly_wait(10) # wait upto 10 sec to find_element(s) functions
# # functions get - load a new webpage in the current browser window
driver.get("https://filebin.net")

driver.find_element_by_class_name("er8xn").send_keys(Keys.ENTER)

driver.quit()

# made a change for git

#commit msg