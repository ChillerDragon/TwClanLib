#!/usr/bin/env python3
import os
import re

### tech 2 ###

def Tech2(data):
    aMember = []
    aMember2 = []
    aMember3 = []
    end = 0
    ClanIndex = 0
    index1 = data.find("<h1>hmm</h1>")
    index2 = data.find("<h1>-.iB</h1>")

    while True:
        start = data.find("<p>", end)
        if start == -1:
            break
        elif start > index1 and ClanIndex == 0:
            ClanIndex = 1
        elif start > index2:
            ClanIndex = 2
            print("using index ib")
        end = data.find("</p>", start)
        if ClanIndex == 0:
            aMember.append(data[start + 3:end])
        elif ClanIndex == 1:
            aMember2.append(data[start + 3:end])
        elif ClanIndex == 2:
            aMember3.append(data[start + 3:end])
        #print("appended '" + data[start + 3:end] + "' at start_index[" + str(start) + "]")
    return aMember, aMember2, aMember3


#####################################
def FetchData():
    os.system("curl https://cinaera.github.io/kappa_website/ > web/kappa.html")
    data = "failed to load site"
    with open("web/kappa.html", "r") as qfile:
        data=qfile.read().replace("\n", "")
    start = data.find("<header>")
    end = data.rfind("</header>")
    data = data[start:end]
    return data
#####################################

def GetMembers():
    return Tech2(FetchData())

print(Tech2(FetchData()))


