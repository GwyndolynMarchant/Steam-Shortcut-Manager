from tkinter import *
from tkinter import messagebox
import re
import SSMModel
import SSMView

class SSMController:
    '''
    The SSMController class manages communication between the view (SSMView)
    and the model (SSMModel)

    Args:
        tbd
    Attributes:
        tbd
    '''

    def __init__(self):
        self.root = Tk()

        self.model = SSMModel.SSMModel(self)
        self.view = SSMView.SSMView(self)

        self.listOfNonSteamGames = []
        self.nonSteamGameListPosition = 0
        self.updatedEntry = ""

        self.root.mainloop()

    def prevButtonPressed(self, event=None): # pylint: disable=unused-argument
        if self.nonSteamGameListPosition > 0:
            self.nonSteamGameListPosition -= 1
            self.setAllElementsInEntry()

    def nextButtonPressed(self, event=None): # pylint: disable=unused-argument
        if self.nonSteamGameListPosition < len(self.listOfNonSteamGames)-1:
            self.nonSteamGameListPosition += 1
            self.setAllElementsInEntry()

    def createNewButtonPressed(self, event=None): # pylint: disable=unused-argument
        self.view.scIndex.set(str(len(self.listOfNonSteamGames))) # index can be auto-filled
        self.view.scAppName.set("APPLICATION NAME (Example: Super Luigi Bros.)")
        self.view.scExePath.set('EXE FILEPATH - INCLUDE QUOTATION MARKS (Example: "C:/Program Files/SLBros/SuperLuigiBros.exe")')
        self.view.scStartDir.set('STARTING DIRECTORY - INCLUDE QUOTATION MARKS (Example: "C:/Program Files/SLBros")')
        self.view.scIcon.set("FILEPATH TO 256x256 PNG ICON (Example: C:/Program Files/SLBros/Luigi.png)")
        # =====================================================================
        self.view.scShortcutPath.set("(DEPRECATED?) STEAM SHORTCUT URL - CAN BE BLANK")
        self.view.scLaunchOptions.set("ADVANCED FLAGS TO USE WITH NON-STEAM GAME EXECUTABLE (Example: --nogui --fullscreen)")
        self.view.scIsHidden.set("0 FOR VISIBLE, 1 FOR HIDDEN")
        self.view.scAllowDesktopConfig.set("0 TO DISABLE DESKTOP CONTROLLER CONFIG, 1 TO ENABLE")
        self.view.scAllowOverlay.set("0 TO DISABLE STEAM OVERLAY, 1 TO ENABLE")
        # =====================================================================
        self.view.scOpenVR.set("0 TO DISABLE, 1 TO ADD TO VR LIBRARY CATEGORY")
        self.view.scDevkit.set("(UNKNOWN) OK TO BLANK OUT")
        self.view.scDevkitGameID.set("(UNKNOWN) OK TO BLANK OUT")
        self.view.scLastPlaytime.set("(DEPRECATED) OK TO BLANK OUT")
        self.view.scTags.set("A LIST WITH INDEX, A SPACE, THEN NAME FOR EACH CATEGORY (Example: 0 Platformers 1 Favorites 2 Souls-like)")
        # ---------------------------------------------------------------------
        self.model.showNewEntryWarning()

    def updateButtonPressed(self, event=None): # pylint: disable=unused-argument
        if self.view.scIndex.get() != str(len(self.listOfNonSteamGames)): # making sure we aren't on a new entry
            tagsEntry = self.view.scTags.get()
            tagsEntry = re.sub("[()']",'',tagsEntry)

            self.updatedEntry = self.view.scIndex.get() +","+ "appName" +","+ self.view.scAppName.get() +","+\
                                "exe"+","+ self.view.scExePath.get() +","+ "StartDir"+","+ self.view.scStartDir.get() +","+\
                                "icon"+","+ self.view.scIcon.get() +","+ "ShortcutPath"+","+ self.view.scShortcutPath.get() +","+\
                                "LaunchOptions"+","+self.view.scLaunchOptions.get() +","+ "IsHidden" + "," +self.view.scIsHidden.get() +","+\
                                "AllowDesktopConfig"+","+self.view.scAllowDesktopConfig.get() +","+ "AllowOverlay"+","+self.view.scAllowOverlay.get() +","+\
                                "openvr"+","+self.view.scOpenVR.get() +","+ "Devkit"+","+self.view.scDevkit.get() +","+ "DevkitGameID"+","+self.view.scDevkitGameID.get() +","+\
                                "LastPlayTime"+","+self.view.scLastPlaytime.get() +","+ "tags"+","+tagsEntry
            print(self.updatedEntry) #test
            elementsList = self.updatedEntry.split(",")

    def aboutMenuSelected(self, event=None): # pylint: disable=unused-argument
        self.model.showVersionAboutInfo()

    def openMenuSelected(self, event=None): # pylint: disable=unused-argument
        self.model.processShortcutFileData()
        messagebox.showinfo("Creating Backup","Creating shortcuts.vdf.bk - remove the .bk to restore your original shortcuts.vdf file.")
        self.listOfNonSteamGames = self.model.cleanedListOfEntries
        self.setAllElementsInEntry()

    def categoryExpanded(self, event=None): # pylint: disable=unused-argument
        result = 0 # TODO

    def setAllElementsInEntry(self):
        self.view.scIndex.set(self.listOfNonSteamGames[self.nonSteamGameListPosition][0])
        self.view.scAppName.set(self.listOfNonSteamGames[self.nonSteamGameListPosition][2])
        self.view.scExePath.set(self.listOfNonSteamGames[self.nonSteamGameListPosition][4])
        self.view.scStartDir.set(self.listOfNonSteamGames[self.nonSteamGameListPosition][6])
        self.view.scIcon.set(self.listOfNonSteamGames[self.nonSteamGameListPosition][8])
        # =====================================================================
        self.view.scShortcutPath.set(self.listOfNonSteamGames[self.nonSteamGameListPosition][10])
        self.view.scLaunchOptions.set(self.listOfNonSteamGames[self.nonSteamGameListPosition][12])
        self.view.scIsHidden.set(self.listOfNonSteamGames[self.nonSteamGameListPosition][14])
        self.view.scAllowDesktopConfig.set(self.listOfNonSteamGames[self.nonSteamGameListPosition][16])
        self.view.scAllowOverlay.set(self.listOfNonSteamGames[self.nonSteamGameListPosition][18])
        # =====================================================================
        self.view.scOpenVR.set(self.listOfNonSteamGames[self.nonSteamGameListPosition][20])
        self.view.scDevkit.set(self.listOfNonSteamGames[self.nonSteamGameListPosition][22])
        self.view.scDevkitGameID.set(self.listOfNonSteamGames[self.nonSteamGameListPosition][24])
        self.view.scLastPlaytime.set(self.listOfNonSteamGames[self.nonSteamGameListPosition][26])
        self.view.scTags.set(self.listOfNonSteamGames[self.nonSteamGameListPosition][28:])

if __name__ == "__main__":
    controller = SSMController()
