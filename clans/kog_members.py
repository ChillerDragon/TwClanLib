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
        start = data.find("<span", end)
        if start == -1:
            break
        start = data.find(">", start)
        end = data.find("</span>", start)
        aMember.append(data[start + 1:end])
    return aMember


#####################################
def FetchData():
    os.system("curl https://qshar.com > web/qshar.html")
    data = "failed to load site"
    with open("web/qshar.html", "r") as qfile:
        data=qfile.read().replace("\n", "")
    start = data.find("If you are in TOP100 on the main server")
    end = data.find("Hall of shame")
    data = data[start:end]
    return data
#####################################

def GetMembers():
    return Tech2(FetchData())

#print(Tech2(FetchData()))
