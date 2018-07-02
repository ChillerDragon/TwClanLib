#!/usr/bin/env python3
import os
import re

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
    os.system("curl https://uniqueclan.net/member > web/unique.html")
    data = "failed to load site"
    with open("web/unique.html", "r") as qfile:
        data=qfile.read().replace("\n", "")
    start = data.find(">Leaders<")
    end = data.rfind("<footer")
    data = data[start:end]
    return data
#####################################

def GetMembers():
    return Tech2(FetchData())

#print(Tech2(FetchData()))


