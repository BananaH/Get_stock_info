#!/usr/bin/python
    
import os, sys
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys #for sending key
from selenium.webdriver.support.ui import Select #for select from list

cwd = os.getcwd() + '/'
driver = webdriver.Chrome(cwd + 'chromedriver')
driver.get("http://www.twse.com.tw/ch/trading/fund/T86/T86.php")        #go to TWSE website

delay = 10

try:
    driver.implicitly_wait(delay)
    #wait for loading page
    search_date = driver.find_element_by_name("input_date")     
    #choose date
    search_date.clear()     
    #clear the diagram
    search_date.send_keys("104/12/04")      
    #enter the date
    Select(driver.find_element_by_name("select2")).select_by_index(0)       
    #find category and choose 'ALL'
    #sort_by = driver.find_elements(name="select2")
    driver.find_element_by_name("login_btn").click()        
    #sending reauest
    
    driver.find_element_by_xpath("//img[@src='/ch/images/save_csv.gif']").click()       
    #find the download icon
finally:
    driver.close()
