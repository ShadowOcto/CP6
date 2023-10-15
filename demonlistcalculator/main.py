import os

import pyperclip as pyperclip
import requests as requests
from colorama import Fore, Style

def getColour(colour):
    if (os.name == 'nt'):
        if (colour == "white"): return Fore.WHITE + Style.BRIGHT
        if (colour == "accent"): return Fore.LIGHTYELLOW_EX + Style.BRIGHT
        if (colour == "red"): return Fore.LIGHTRED_EX + Style.BRIGHT
        if (colour == "grey"): return Fore.LIGHTBLACK_EX
    else:
        return ""

def getPositionInList(level):
    f = requests.get(f"https://raw.githubusercontent.com/ShadowOcto/CP6/main/list").text
    lines = f.splitlines()
    i = 1;
    for x in lines:
        if level.lower() in x.lower():
            return i
        i += 1

def getListPointsForLevel(levelPosition):
    return round(250 / ((levelPosition + 4) * 0.2))

def printUserError(user):
    print(f"{getColour('red')}{user} was not found.")
    input()
    init()

def init():
    if os.name == 'nt':
        os.system("cls")
        os.system("title List Point Calculator v2.0 by ShadowOcto")
    print(f"{getColour('accent')}List Point Calculator {getColour('white')}v2.0 {getColour('grey')}by ShadowOcto\n")
    listPoints = 0;
    user = input(f"{getColour('white')}User: ")
    try:
        f = requests.get(f"https://raw.githubusercontent.com/ShadowOcto/CP6/main/users/{user.lower()}").text
        lines = f.splitlines()
        i = 1;
        listPoints = 0
        for x in lines:
            listPos = getPositionInList(x.strip())
            print(f"{getColour('grey')}Level: {getColour('white')}{x.strip()} | {getColour('grey')}Position: {getColour('white')}{listPos} | {getColour('grey')}List Points: {getColour('accent')}{getListPointsForLevel(listPos)}")
            listPoints = listPoints + getListPointsForLevel(listPos)
        print(f"{getColour('white')}Total List Points: {getColour('accent')}{listPoints} {getColour('grey')}(Copied to clipboard)")
        pyperclip.copy(listPoints)
        input()
        init()
    except:
        printUserError(user)
init()



