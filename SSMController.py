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

        self.root.mainloop()

    def prevButtonPressed(self, event=None): # pylint: disable=unused-argument
        result = 0 # TODO

    def nextButtonPressed(self, event=None): # pylint: disable=unused-argument
        result = 0 # TODO

    def removeButtonPressed(self, event=None): # pylint: disable=unused-argument
        result = 0 # TODO

    def addUpdateButtonPressed(self, event=None): # pylint: disable=unused-argument
        result = 0 # TODO

    def aboutMenuSelected(self, event=None): # pylint: disable=unused-argument
        self.model.showVersionAboutInfo()

    def openMenuSelected(self, event=None): # pylint: disable=unused-argument
        self.model.processShortcutFileData()

    def categoryExpanded(self, event=None): # pylint: disable=unused-argument
        result = 0 # TODO

if __name__ == "__main__":
    controller = SSMController()
