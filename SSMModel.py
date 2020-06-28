# Meant purely for functions that do work
#
# Get path to Steam folder and the shortcuts.vdf from user
# If not found, ask user to create one via Steam (ideally create new one for them, maybe feature for later)
# Read the .vdf list of entries
# Display the categories - make them selectable/expandable
# Select the first category's entry by default and auto-display those elements
# Make each entry's element editable, but display the current info by default
# Have a add/update button for each entry that the user can edit
# Have a remove button for the current entry
#
# App ID # - compare to crc result - there's a (appid)_hero.png, (appid)_logo.png, and (appid)p.png that
#   all live in \userdata\(userID)\config\grid
# Offer buttons to convert vdf to csv and csv to vdf (extra feature)

# E:/SteamLibrary/userdata/35696109/config/shortcuts.vdf
# C:\Users\uwmil\Downloads\shortcuts.vdf
# C:/Users/uwmil/Downloads/shortcuts.vdf

import re
import os
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

    def processShortcutFileData(self):
        try:
            fileBlob = filedialog.askopenfile(initialdir = "/",
                                              title = "Select your Steam shortcuts.vdf file...",
                                              filetypes = (("vdf files", "*.vdf"),("all files", "*.*")))
            # To make this more manageable, we take the non-printable characters in the .vdf and swap them out with 
            # characters that are easier to process down into something that can be formed into a list of non-Steam
            # game entries
            readyBlob = fileBlob.read().replace('\x08', '@').replace('\x00',',').replace('\x01','').replace('\x02','').replace("\\", "/")
            readyBlob = re.sub(r"(,,,,,,|,,,,,|,,,,)", ',,', readyBlob)
            readyBlob = readyBlob[12:].replace('@@@@','@@')
            readyBlob = readyBlob[:-3] # removing the trailing ',@@'
            readyEntryList = readyBlob.split(",@@,") # Breaks up the individual entries
            for entry in readyEntryList:
                newEntryList = entry.split(",")
                self.cleanedListOfEntries.append(newEntryList)
            # print(self.cleanedListOfEntries) # temp test
            # Need to slice off the tags/category information and work with it
            # self.cleanedListOfEntries[0][27:] - includes 'tags' and then each entry after this title to the end of the entry

        except FileNotFoundError:
            print("File not found, please add a non-Steam game while in Steam to generate a shortcuts.vdf")
