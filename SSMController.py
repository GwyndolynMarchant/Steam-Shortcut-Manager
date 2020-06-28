from tkinter import *
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

        self.root.mainloop()

    def prevButtonPressed(self, event=None): # pylint: disable=unused-argument
        if self.nonSteamGameListPosition > 0:
            self.nonSteamGameListPosition -= 1
            self.setAllElementsInEntry()

    def nextButtonPressed(self, event=None): # pylint: disable=unused-argument
        if self.nonSteamGameListPosition < len(self.listOfNonSteamGames)-1:
            self.nonSteamGameListPosition += 1
            self.setAllElementsInEntry()

    def removeButtonPressed(self, event=None): # pylint: disable=unused-argument
        result = 0 # TODO

    def addUpdateButtonPressed(self, event=None): # pylint: disable=unused-argument
        result = 0 # TODO

    def aboutMenuSelected(self, event=None): # pylint: disable=unused-argument
        self.model.showVersionAboutInfo()

    def openMenuSelected(self, event=None): # pylint: disable=unused-argument
        self.model.processShortcutFileData()
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
        self.view.scShortcutPath.set(self.listOfNonSteamGames[self.nonSteamGameListPosition][10])
        self.view.scLaunchOptions.set(self.listOfNonSteamGames[self.nonSteamGameListPosition][12])
        self.view.scIsHidden.set(self.listOfNonSteamGames[self.nonSteamGameListPosition][14])
        self.view.scAllowDesktopConfig.set(self.listOfNonSteamGames[self.nonSteamGameListPosition][16])
        self.view.scAllowOverlay.set(self.listOfNonSteamGames[self.nonSteamGameListPosition][18])
        self.view.scOpenVR.set(self.listOfNonSteamGames[self.nonSteamGameListPosition][20])
        self.view.scDevkit.set(self.listOfNonSteamGames[self.nonSteamGameListPosition][22])
        self.view.scDevkitGameID.set(self.listOfNonSteamGames[self.nonSteamGameListPosition][24])
        self.view.scLastPlaytime.set(self.listOfNonSteamGames[self.nonSteamGameListPosition][26])
        self.view.scTags.set(self.listOfNonSteamGames[self.nonSteamGameListPosition][28:])

if __name__ == "__main__":
    controller = SSMController()
