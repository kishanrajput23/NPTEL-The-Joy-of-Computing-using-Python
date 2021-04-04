# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 10:37:37 2021

@author: Lakhan KumawatN
"""

#C:/Users/Lakhan Kumawat/Downloads/chromedriver_win32/chromedriver.exe 


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

#lets select the web driver with path first i m using win 32 it works on my 64 bit 
driver=webdriver.Chrome("C:/Users/Lakhan Kumawat/Downloads/chromedriver_win32/chromedriver.exe")

driver.get("https://web.whatsapp.com/")

wait=WebDriverWait(driver, 600)

# Replace 'Friend's Name' with the name of your friend  
# or the name of a group  
target = '"BRO"'
  
# Replace the below string with your own message 
string = "Message sent using Python!!!"
  
x_arg = '//span[contains(@title,' + target + ')]'

group_title = wait.until(EC.presence_of_element_located(( 
    By.XPATH, x_arg))) 

group_title.click() 


input_box=driver.find_element_by_class_name('_2_1wd')
    
for i in range(5): 
    input_box.send_keys(string + Keys.ENTER) 
    time.sleep(1) 













