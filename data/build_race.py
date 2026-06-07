#!/usr/bin/python

import sys
from sys import platform
import os
import subprocess
import shutil

def getRegionLetter():
    regionLetter = input("Input the letters P, E, J or K for your region.\n")

    if len(regionLetter) > 1:
        print ("No more than one character can be input. Aborting.\n")
        sys.exit()

    return regionLetter

def buildGlobalArchive(regionLetter):
    if os.path.isfile("Race_R.szs") is True:
        if os.path.isfile("Race.szs") is True:
            os.remove("Race.szs")
        os.rename("Race_R.szs", "Race.szs")
        print ("Found Korean Race archive. Renamed for convenience.\n")

    subprocess.run(["wszst", "extract", "Race.szs"])
    print("Copying Race files.\n")
    shutil.copyfile("position_12players.brlyt", "Race.d/result/blyt/position_12players.brlyt")
    os.remove("Race.szs")
    subprocess.run(["wszst", "create", "Race.d"])
    shutil.rmtree("Race.d")
    print ("Created Race file.\n")

    if regionLetter == 'K' or regionLetter == 'k':
        os.rename("Race.szs", "Race_R.szs")

def buildFont(regionLetter):
    fontFile = "Font"
    if regionLetter == 'K' or regionLetter == 'k':
        fontFile = "Font_K"

    subprocess.run(["wszst", "extract", f"{fontFile}.szs"])
    shutil.copyfile("tt_kart_extension_font.brfnt", f"{fontFile}.d/tt_kart_extension_font.brfnt")
    os.remove(f"{fontFile}.szs")
    subprocess.run(["wszst", "create", f"{fontFile}.d"])
    shutil.rmtree(f"{fontFile}.d")
    print("Created font file.\n")

def buildRegionalArchives(regionLetter):
    bmgLocation = "message/Race.bmg"
    maxCycle = 0

    if regionLetter == 'E' or regionLetter == 'e':
        gameVersion = "NTSC-U"
        English = "Race_U"
        French = "Race_Q"
        Spanish = "Race_M"
        languageList = [
            English,
            French,
            Spanish
        ]
        maxCycle = 2
    elif regionLetter == 'P' or regionLetter == 'p':
        gameVersion = "PAL"
        English = "Race_E"
        French = "Race_F"
        German = "Race_G"
        Italian = "Race_I"
        Spanish = "Race_S"
        languageList = [
            English,
            French,
            German,
            Italian,
            Spanish
        ]
        maxCycle = 4
    elif regionLetter == 'J' or regionLetter == 'j':
        gameVersion = "NTSC-J"
        Japanese = "Race_J"
        languageList = [Japanese]
    elif regionLetter == 'K' or regionLetter == 'k':
        gameVersion = "NTSC-K"
        Korean = "Race_K"
        languageList = [Korean]
    else:
        print("Unrecoverable error. Aborting.\n")
        sys.exit()

    languageCycle = 0

    for entry in languageList:
        subprocess.run(["wszst", "extract", f"{languageList[languageCycle]}.szs"])
        languageCycle += 1

    sorted(languageList)

    languageCycle = 0
    curDir = f"text/{gameVersion}"

    for entry in languageList:
        if regionLetter == 'E' or regionLetter == 'e':
            if languageCycle == 0:
                language = "English"
            elif languageCycle == 1:
                language = "French"
            elif languageCycle == 2:
                language = "Spanish"
        elif regionLetter == 'P' or regionLetter == 'p':
            if languageCycle == 0:
                language = "English"
            elif languageCycle == 1:
                language = "French"
            elif languageCycle == 2:
                language = "German"
            elif languageCycle == 3:
                language = "Italian"
            elif languageCycle == 4:
                language = "Spanish"
        elif regionLetter == 'J' or regionLetter == 'j':
            language = "Japanese"
        elif regionLetter == 'K' or regionLetter == 'k':
            language = "Korean"
        else:
            print("Unrecoverable error. Aborting\n")
            sys.exit()

        print(f"Copying {language} files.\n")
        shutil.copyfile(f"{curDir}/{language}/Race.bmg", f"{languageList[languageCycle]}.d/{bmgLocation}")

        if languageCycle == maxCycle:
            languageCycle = 0
            for entry in languageList:
                os.remove(f"{languageList[languageCycle]}.szs")
                languageCycle += 1
            break

        languageCycle += 1

    languageCycle = 0
    for entry in languageList:
        subprocess.run(["wszst", "create", f"{languageList[languageCycle]}.d"])
        shutil.rmtree(f"{languageList[languageCycle]}.d")
        languageCycle += 1

    print("Created all language files.\n")

def main():
    sysCheckPassed = "System check passed."

    if platform == "win32":
        if os.path.isfile("C:/Program Files (x86)/Wiimm/SZS/wszst.exe"):
            print (sysCheckPassed)
    elif os.path.isfile("/usr/local/bin/wszst"):
        print (sysCheckPassed)
    else:
        print ("Wiimm's SZS Tools could not be found. Please install Wiimm's SZS Tools from (https://szs.wiimm.de/download.html).")
        sys.exit()

    regionLetter = getRegionLetter()
    buildGlobalArchive(regionLetter)
    buildRegionalArchives(regionLetter)
    buildFont(regionLetter)
    print("Operation completed successfully.\n")

main()
