#!/usr/bin/python

def compare_str(text,target):
    j=0
    for i in range(len(text)):
        if text[i]==target[j]:
            j+=1
            if j>=len(target):
                return 1
        elif j>0:
            j=0
    else:
        return 0

def decode(text,file_name):
    file_name += '.csv'
    f_out = open(file_name,"w")
    for i in range(len(text)):
    f_out.close()
