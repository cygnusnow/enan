#!/usr/bin/python   
# -*- coding: gb2312 -*-   
  
from selenium import webdriver  
from selenium.common.exceptions import TimeoutException  
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0   
import time  
import sys

reload(sys)
sys.setdefaultencoding('gb2312')
  
# Create a new instance of the Firefox driver   
driver = webdriver.Chrome()  
  
# go to the google home page   
driver.get("http://www.jisilu.cn/data/sfnew/#tlink_3")  

# find the element that's name attribute is q (the google search box)   
inputElement = driver.find_element_by_id('150175')
  
print inputElement.text

# type in the search   
#inputElement.send_keys("hello jojo!")
  
# submit the form. (although google automatically searches now without submitting)   
#inputElement.submit()
  
# the page is ajaxy so the title is originally this:   
  
try:  
    # we have to wait for the page to refresh, the last thing that seems to be updated is the title   
    WebDriverWait(driver, 10).until(lambda driver : driver.title.lower().startswith("cheese!"))  
  
    # You should see "cheese! - Google Search"   
    print driver.title  
  
finally:  
    driver.quit()  
