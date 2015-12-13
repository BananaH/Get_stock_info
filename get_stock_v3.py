#!/usr/bin/python

import os, sys
import requests
from selenium import webdriver
from bs4 import BeautifulSoup

payload = {
	'input_date':'104/12/04',
	'select2':'ALL',
	'sorting':'by_issue',
}

res = requests.post("http://www.twse.com.tw/ch/trading/fund/T86/T86.php", data = payload)
f_origin = open("page_data.txt","w")
browser = webdriver.Firefox()
driver.get("http://www.twse.com.tw/ch/trading/fund/T86/T86.php")
element = driver.find_elements(src="/ch/images/save_csv.gif")
driver.click(element)
f_origin.write(res.text.encode('utf-8','replace'))
f_origin.close()
soup = BeautifulSoup(res.text.encode('utf-8','replace'))
'''
for item in soup.select('a'):
    print len(item.select('a'))#.text
'''
#f_filter = open("filter_data.txt","w")
#f_origin = open("page_data.txt","r")



#f_origin.close()
#f_filter.close()
