
#   *   This is a basic webscraper for different usecases
#   *   You will need to uncomment/comment the sections that you want to use 
#   *   You can uncomment entire sections as the comments have been double commented
#   *   Each section will have its own description and uses listed
#   !!  I suggest having "better comments" enabled if you use vscode as it allows for colour coded comments for specific sections

from selenium import webdriver
from selenium.webdriver.common.keys import Keys                                         
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://example.com")
# print(driver.title)

#   * This section shows action chains and automation/ clicking
#   this will make script wait 10 seconds to load the page or whatever else before running the script so that all elements are on the page
driver.implicitly_wait(10)
#   the element of the webpage that you want to put an action onto
element = driver.find_element_by_id("elementID")
#   you can add condiitions within ther elementID such as for loops, if statement etc
element_count = driver.find_element_by_id("elementID")
items = [driver.find_element_by_id("elementID")]
#   the action you want to perform, for example click
actions = ActionChains(driver)
actions.click()

#   how many times you want to press click
for i in range(10):
    actions.perform()
    count = element_count.text
    actions.perform()
#   this print will print out to terminal
    print(count)
# #   *   This section will be basic page navigation
# link = driver.find_element_by_link_text("Python Script")
# link.click()

# try:
#     element = WebDriverWait(driver, 10).until(   
# #   the main variable here is the elemennt you want for example LINK_TEXT="What you want to click" you can specify any element                          
#         EC.presence_of_element_located((By.LINK_TEXT, "first element you want to click"))     
#     )
#     element.click()

#     element = WebDriverWait(driver, 10).until(                          
#         EC.presence_of_element_located((By.ID, "second element you want to click"))     
#     )
# #   this clears all the text that is in searchbox you want to search in
#     element.clear()
#     element.click()                                       
# #   you can use finally or except here, except has been used incase the piece of code doesnt work                                                 
# except: 
#     driver.quit()

# #   *   This section is for searching information on a website or webpage
# #   ?   when searching for someting specfic on a wepage or website first look for the ID if not available 
# #   ?   then -> name if not available 
# #   ?   then -> class
# #   this looks for the search box on the website by the 'name'
# # search = driver.find_element_by_name("s")     
# #   this is the search parameters that you want to look for in the search box on the webpage                                        
# search.send_keys("test")                                                              
# search.send_keys(Keys.RETURN)
# #   this looks for the 'main' ID on the webpage. The next try condtions make this irrelavent
# main = driver.find_element_by_id("main")                                              

# try:
#     main = WebDriverWait(driver, 10).until( 
# #   the main variable here is the elemennt you want for example ID="main" you can specify any element                            
#         EC.presence_of_element_located((By.ID, "main"))                               

#     )
#     print(main.text)  

#     articles = main.find_elements_by_tag_name("article")
#     for article in articles:
#         header = article.find_element_by_class_name("entry-summary")
#         print(header.text)                                              
                                                 
# finally:
#     driver.quit()

# #   this delays the program by 5 second before quiting so that we can see what the search results are, but not needed with the try condtions above, but it is good for testing the script
# time.sleep(5)
# #   this will close the tab                                                                          
# driver.close() 
# #   this will quit the browser becomes redundant with the try try condition but is good for testing the script                                                                       
# driver.quit()
# # this navigates back to previous pages
# driver.back()
# #   this navigates forward pages
# driver.forward()
