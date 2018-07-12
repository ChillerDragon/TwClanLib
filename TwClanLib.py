#!/usr/bin/env python3

import os
import sys
import clans.unique_members
import clans.kog_members
import clans.aeon_xron_members
import clans.kappa_members

TotalClans = 0

clan_unique = clans.unique_members.GetMembers()
TotalClans += 1
clan_aeon, clan_xron = clans.aeon_xron_members.GetMembers()
TotalClans += 2
clan_kog = clans.kog_members.GetMembers()
TotalClans += 1
clan_kappa, clan_hmm, clan_ib = clans.kappa_members.GetMembers()
TotalClans += 3

aaClans = [[0 for x in range(2)] for x in range(TotalClans)]
aaClans[0][0] = "unique"
aaClans[0][1] = clan_unique
aaClans[1][0] = "aeon"
aaClans[1][1] = clan_aeon
aaClans[2][0] = "xron"
aaClans[2][1] = clan_xron
aaClans[3][0] = "kog"
aaClans[3][1] = clan_kog
aaClans[4][0] = "kappa"
aaClans[4][1] = clan_kappa
aaClans[5][0] = "hmm"
aaClans[5][1] = clan_hmm
aaClans[6][0] = "-.iB"
aaClans[6][1] = clan_ib



def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def PrintAllClans():
    cls()
    for aClan in aaClans:
        print("===== " + str(aClan[0]) + " ======")
        for player in aClan[1]:
            print(player)

def ShowClanPlayers(clan):
    cls()
    clan = int(clan)
    clan -= 1
    if clan < 0:
        print("error: index too small")
        return False
    if clan >= TotalClans:
        print("error: index too big")
        return False
    print("=== " + str(aaClans[clan][0]) + " ===")
    for player in aaClans[clan][1]:
        print(player)

def ShowClans():
    cls()
    x = 0
    for cclan in aaClans:
        x += 1
        clan = cclan[0]
        print("[" + str(x) + "] " + str(clan))
    clan = input("clan: ")
    if not clan.isdigit():
        ShowClans()
    ShowClanPlayers(clan)


def ShowClansOfPlayer(name):
    clans = 0
    cls()
    print("player: " + str(name))
    print("clans: ")
    for aClan in aaClans:
        for clan in aClan[1]:
            if (name == clan):
                if clans > 0:
                    print(", " + aClan[0])
                else:
                    print(aClan[0])
                clans += 1
    if clans == 0:
        cls()
        print("player '" + str(name) + "' isn't in the database")


def main(argv):
    cls()
    print("==============================")
    print("    Teeworlds Clan Library    ")
    print("       by ChillerDragon       ")
    print("==============================")
    print("clans: " + str(TotalClans))
    print("[1] show all clans")
    print("[2] show clans of player")
    print("[3] show players of clan")
    print("[4] quit")
    inp = input("cmd: ")
    if (inp == "1"):
        PrintAllClans()
    elif (inp == "2"):
        player = input("player: ")
        ShowClansOfPlayer(player)
    elif (inp == "3"):
        ShowClans()
    elif (inp == "4" or inp == "q"):
        exit()
    else:
        print("unknown command")
    input("[ENTER] to go back to menu")
    main(None)

def PrintAllClansOLD():
    print("\naeon: \n")
    print(clan_aeon)
    print("\nxron: \n")
    print(clan_xron)
    print("\nunique: \n")
    print(clan_unique)
    print("\nkog: \n")
    print(clan_kog)

if __name__ == "__main__":
    main(sys.argv)
