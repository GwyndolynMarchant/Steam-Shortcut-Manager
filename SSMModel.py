# Display the categories - make them selectable/expandable
# Select the first category's entry by default and auto-display those elements
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

    Args:
        arg(controller): Storage for the SSMController object.
    
    Attributes:
        controller (SSMController): The model sets some attributes on the controller.
        cleanedListOfEntries (list): The list of non-Steam games from shortcuts.vdf.

    """

    def __init__(self, controller):
        self.controller = controller
        self.cleanedListOfEntries = []
        self.sourceFilePath = ""

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
            self.sourceFilePath = fileBlob.name
            destFilePath = self.sourceFilePath.replace(".vdf",".vdf.bk")
            copy2(self.sourceFilePath, destFilePath)

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
            # Create warning message visible to users. TODO
            print("File not found, please add a non-Steam game while in Steam to generate a shortcuts.vdf")

    def createNewShortcutFile(self):
        # print(self.sourceFilePath) # test
        shortcutsIntroText = '\x00'+'shortcuts'+'\x00'
        shortcutsText = ''
        shortcutsEndingText = '\x08\x08'

        length = len(self.cleanedListOfEntries)
        position = 0

        while position < length:
            shortcutsText += '\x00'+self.cleanedListOfEntries[position][0]+'\x00'+\
                             '\x01'+'appName'+'\x00'+self.cleanedListOfEntries[position][2]+'\x00'+\
                             '\x01'+'exe'+'\x00'+self.cleanedListOfEntries[position][4]+'\x00'+\
                             '\x01'+'StartDir'+'\x00'+self.cleanedListOfEntries[position][6]+'\x00'+\
                             '\x01'+'icon'+'\x00'+self.cleanedListOfEntries[position][8]+'\x00'+\
                             '\x01'+'ShortcutPath'+'\x00'+self.cleanedListOfEntries[position][10]+'\x00'+\
                             '\x01'+'LaunchOptions'+'\x00'+self.cleanedListOfEntries[position][12]+'\x00'+\
                             '\x02'+'IsHidden'+'\x00\x00\x00\x00\x00'+\
                             '\x02'+'AllowDesktopConfig'+'\x00\x01\x00\x00\x00'+\
                             '\x02'+'AllowOverlay'+'\x00\x01\x00\x00\x00'+\
                             '\x02'+'openvr'+'\x00\x00\x00\x00\x00'+\
                             '\x02'+'Devkit'+'\x00\x00\x00\x00\x00'+\
                             '\x01'+'DevkitGameID'+'\x00\x00'+\
                             '\x02'+'LastPlayTime'+'\x00'+self.cleanedListOfEntries[position][26]+'\x00'+\
                             'tags'+'\x00'+self.setupTags(position)+'\x08\x08'
            position += 1
        # print(shortcutsIntroText+shortcutsText+shortcutsEndingText) # temp test
        try:
            dataFile = filedialog.asksaveasfile(mode='w',
                                                defaultextension=".vdf",
                                                initialdir="/",
                                                title="Save shortcuts.vdf file...",
                                                filetypes=(("vdf files", "*.vdf"),("all files", "*.*")))
            dataFile.write(shortcutsIntroText+shortcutsText+shortcutsEndingText) # TODO FIX SLASH ORIENTATION
            dataFile.close()
        except IOError:
            # Create warning message visible to users. TODO
            print("Unable to save file to previous shortcuts.vdf location, please check and try again later.")
    
    def setupTags(self, pos):
        finalString=''
        remainingTags = self.cleanedListOfEntries[pos][28:] # the tags can show multiple categories
        counter = 0
        while counter < len(remainingTags):
            finalString += '\x01'+remainingTags[counter]+'\x00'+remainingTags[counter+1]+'\x00'
            counter += 2
        # print(finalString) # temp test
        return finalString        
                             