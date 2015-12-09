#!/usr/bin/python

import requests, json, os, sys

payload = {
	'input_date':'104/12/04',
	'select2':'ALL',
	'sorting':'by_issue',
}

res = requests.post("http://www.twse.com.tw/ch/trading/fund/T86/T86.php", data = payload)
fout = open("out.txt","w")

fout.write(res.text.encode('utf-8','replace'))
#Without adding ".encode('utf-8','replace') will cause a UnicodeEncodeError.
#I'm not sure how it works.

fout.close()
