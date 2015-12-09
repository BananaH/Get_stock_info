#!/usr/bin/python

import json,os,sys,compare

f_input = open("page_data.txt","r")
i=0

while True:
    i+=1
    tbody = '</tbody>'
    line = f_input.readline()
    if not line: break
    if compare.compare_str(line,tbody):
        line = f_input.readline()
        compare.decode(line,file_name)

f_input.close()
