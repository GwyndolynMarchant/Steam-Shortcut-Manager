# Display the categories - make them selectable/expandable
# Select the first category's entry by default and auto-display those elements
# Make each entry's element editable, but display the current info by default
# App ID # - compare to crc result - there's a (appid)_hero.png, (appid)_logo.png, and (appid)p.png that
#   all live in \userdata\(userID)\config\grid
# Offer buttons to convert vdf to csv and csv to vdf (extra feature)

# E:/SteamLibrary/userdata/35696109/config/shortcuts.vdf
# C:/Users/uwmil/Downloads/shortcuts.vdf

import re
import os
from shutil import copy2
from tkinter import filedialog
from tkinter import messagebox

class SSMModel:
    """The SSMModel contains the functions used by the Steam Shortcut Manager.

    Attributes:
        tbd
    """

    def __init__(self, controller):
        self.controller = controller
        self.cleanedListOfEntries = []

    def showVersionAboutInfo(self):
        messagebox.showinfo("About SSM GUI", """Version 0.1
The Steam Shortcut Manager GUI displays the non-Steam game shortcuts that appear in your userdata's shortcuts.vdf file in a friendlier format.
Update and then save each entry in your non-Steam game list as needed, then save the changes.

Author: Val Miller
Made possible by supportive spouse and cats <3""")

    def showNewEntryWarning(self):
        messagebox.showwarning("New Entry Warning","""Leave the Index Number as-is, but replace all other entries with your new entry's information.

If you're unsure about this, use Steam's UI to add a new entry's information instead.

After making changes, go to the File menu and select 'Save As' to create/update your shortcuts.vdf - it must be in the correct Steam userdata folder for Steam to see your changes when restarting that application.""")

    def processShortcutFileData(self):
        try:
            fileBlob = filedialog.askopenfile(initialdir = "/",
                                              title = "Select your Steam shortcuts.vdf file...",
                                              filetypes = (("vdf files", "*.vdf"),("all files", "*.*")))
            # make a backup copy
            sourceFilePath = fileBlob.name
            destFilePath = sourceFilePath.replace(".vdf",".vdf.bk")
            copy2(sourceFilePath, destFilePath)

            # To make this more manageable, we take the non-printable characters in the .vdf and swap them out with 
            # characters that are easier to process down into something that can be formed into a list of non-Steam
            # game entries
            readyBlob = fileBlob.read().replace('\x08', '@').replace('\x00',',').replace('\x01','').replace('\x02','').replace("\\", "/")
            fileBlob.close()
            readyBlob = re.sub(r"(,,,,,,|,,,,,|,,,,)", ',,', readyBlob)
            readyBlob = readyBlob[12:].replace('@@@@','@@')
            readyBlob = readyBlob[:-3] # removing the trailing ',@@'
            readyEntryList = readyBlob.split(",@@,") # Breaks up the individual entries
            for entry in readyEntryList:
                newEntryList = entry.split(",")
                self.cleanedListOfEntries.append(newEntryList)
            # print(self.cleanedListOfEntries) # temp test
        except FileNotFoundError:
            print("File not found, please add a non-Steam game while in Steam to generate a shortcuts.vdf")
