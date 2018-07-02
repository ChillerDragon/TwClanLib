#!/usr/bin/env python3
import os
import re
import urllib.request

### tech 1 ###

def CleanWebData(data):
    cleanr = re.compile("<.*?>")
    cleantext = re.sub(cleanr, '', data)
    return cleantext

def SpliceNames(data):
    return data.replace("</span>", "\n")

def Tech1(data):
    return CleanWebData(SpliceNames(data))

### tech 2 ###

def Tech2(data):
    aMember = []
    end = 0
    while True:
        start = data.find("<h1>", end)
        if start == -1:
            break
        end = data.find("</h1>", start)
        aMember.append(data[start + 4:end])
    return aMember


#####################################
def FetchData():
    data = urllib.request.urlopen("http://aeon.teewars.com/about/members").read()
    data = str(data)
    cut = data.rfind("Team")
    #print("cut: " + str(end))
    data1 = data[:cut]
    data2 = data[cut:]
    return data1, data2
#####################################

def GetMembers():
    d1, d2 = FetchData()
    return Tech2(d1), Tech2(d2)

#data1, data2 = FetchData()
#print("aeon: \n" + str(Tech2(data1)) + "\nxron: \n" + str(Tech2(data2)))



