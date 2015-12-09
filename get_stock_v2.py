#!/usr/bin/python

import requests, json, os, sys

payload = {
	'input_date':'104/12/04',
	'select2':'ALL',
	'sorting':'by_issue',
}

res = requests.post("http://www.twse.com.tw/ch/trading/fund/T86/T86.php", data = payload)
f_origin = open("page_data.txt","w")

f_origin.write(res.text.encode('utf-8','replace'))
f_origin.close()

f_filter = open("filter_data.txt","w")
f_origin = open("page_data.txt","r")



f_origin.close()
f_filter.close()
