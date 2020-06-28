from tkinter import *
from tkinter import ttk

class SSMView(ttk.Frame):
    """The SSMView class holds all of the user interface layout.

    Attributes:
        arg(controller): Storage for the SSMController object.
    """
    def __init__(self, controller):
        """Setting up the GUI in a grid layout. """
        ttk.Frame.__init__(self, padding = "4 4 12 12")
        self.grid(column=0, row=0, sticky=(N,W,E,S))
        self.controller = controller
        self.controller.root.title("Steam Shortcut Manager GUI")
        self.controller.root.columnconfigure(0, weight=1)
        self.controller.root.rowconfigure(0, weight=1)

        # Setup the pulldown menubar
        self.menubar = Menu(self.controller.root)

        # Create file menu, attach to the menubar
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Open shortcuts.vdf...", command=self.controller.openMenuSelected)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.quit)
        self.menubar.add_cascade(label="File", menu=self.filemenu)

        # Create about menu, attach to the menubar
        self.aboutmenu = Menu(self.menubar, tearoff=0)
        self.aboutmenu.add_command(label="Info/Version", command=self.controller.aboutMenuSelected)
        self.menubar.add_cascade(label="About", menu=self.aboutmenu)

        # show menubar
        self.controller.root.config(menu = self.menubar)

        # Set up Categories
        self.categoryHeader = ttk.Label(self, text="Categories\n(Under Construction)")
        self.categoryHeader.grid(row=1, column=1, sticky=(N,W))

        # Header for the elements of a shortcut entry
        self.entryElementsHeader = ttk.Label(self, text="Non-Steam Game entry fields \nfrom shortcuts.vdf.\n\nMouseover for info.")
        self.entryElementsHeader.grid(row=1, column=2, sticky=(N,W))

        # Show descriptive text
        self.mainDescriptionHeader = Label(self, text="""How To Use:
Provide the filepath (including drive letter) to the Steam shortcuts.vdf via the File menu pulldown. 
Example: \"C:\\Program Files (x86)\\Steam\\userdata\\<user_id>\\config\\shortcuts.vdf\"
<user_id>: can be any set of numbers, check your Steam install setup.""", width=105, height=4, justify=LEFT, anchor=W)
        self.mainDescriptionHeader.grid(row=1, column=3, columnspan=2)

        # Add several label fields for each element of a shortcut entry
        # Note: Tkinter will return a NoneType if you do a .grid all on one line 
        # with the original Label creation, make sure to do the .grid separately
        self.indexLabel = ttk.Label(self, text="Index Number")
        self.indexLabel.bind("<Enter>", self.updateIndexLabelEntered)
        self.indexLabel.bind("<Leave>", self.updateLabelExited)
        self.indexLabel.grid(row=3, column=2, sticky=E)

        self.appNameLabel = ttk.Label(self, text="AppName")
        self.appNameLabel.bind("<Enter>", self.updateAppNameLabelEntered)
        self.appNameLabel.bind("<Leave>", self.updateLabelExited)
        self.appNameLabel.grid(row=4, column=2, sticky=E)

        self.exePathLabel = ttk.Label(self, text="Exe Path")
        self.exePathLabel.bind("<Enter>", self.updateExePathLabelEntered)
        self.exePathLabel.bind("<Leave>", self.updateLabelExited)
        self.exePathLabel.grid(row=5, column=2, sticky=E)

        self.startDirLabel = ttk.Label(self, text="Start Directory")
        self.startDirLabel.bind("<Enter>", self.updateStartDirLabelEntered)
        self.startDirLabel.bind("<Leave>", self.updateLabelExited)
        self.startDirLabel.grid(row=6, column=2, sticky=E)

        self.iconLabel = ttk.Label(self, text="Icon")
        self.iconLabel.bind("<Enter>", self.updateIconLabelEntered)
        self.iconLabel.bind("<Leave>", self.updateLabelExited)
        self.iconLabel.grid(row=7, column=2, sticky=E)
        # =======================================================
        self.shortcutPathLabel = ttk.Label(self, text="Shortcut Path")
        self.shortcutPathLabel.bind("<Enter>", self.updateShortcutPathLabelEntered)
        self.shortcutPathLabel.bind("<Leave>", self.updateLabelExited)
        self.shortcutPathLabel.grid(row=8, column=2, sticky=E)

        self.launchOptsLabel = ttk.Label(self, text="Launch Options")
        self.launchOptsLabel.bind("<Enter>", self.updateLaunchOptsLabelEntered)
        self.launchOptsLabel.bind("<Leave>", self.updateLabelExited)
        self.launchOptsLabel.grid(row=9, column=2, sticky=E)

        self.isHiddenLabel = ttk.Label(self, text="IsHidden")
        self.isHiddenLabel.bind("<Enter>", self.updateIsHiddenLabelEntered)
        self.isHiddenLabel.bind("<Leave>", self.updateLabelExited)
        self.isHiddenLabel.grid(row=10, column=2, sticky=E)

        self.allowDesktopCfgLabel = ttk.Label(self, text="Allow Desktop Config")
        self.allowDesktopCfgLabel.bind("<Enter>", self.updateAllowDesktopCfgLabelEntered)
        self.allowDesktopCfgLabel.bind("<Leave>", self.updateLabelExited)
        self.allowDesktopCfgLabel.grid(row=11, column=2, sticky=E)

        self.allowOverlayLabel = ttk.Label(self, text="Allow Overlay")
        self.allowOverlayLabel.bind("<Enter>", self.updateAllowOverlayLabelEntered)
        self.allowOverlayLabel.bind("<Leave>", self.updateLabelExited)
        self.allowOverlayLabel.grid(row=12, column=2, sticky=E)
        # =======================================================
        self.openVRLabel = ttk.Label(self, text="OpenVR")
        self.openVRLabel.bind("<Enter>", self.updateOpenVRLabelEntered)
        self.openVRLabel.bind("<Leave>", self.updateLabelExited)
        self.openVRLabel.grid(row=13, column=2, sticky=E)

        self.devkitLabel = ttk.Label(self, text="Devkit")
        self.devkitLabel.bind("<Enter>", self.updateDevkitLabelEntered)
        self.devkitLabel.bind("<Leave>", self.updateLabelExited)
        self.devkitLabel.grid(row=14, column=2, sticky=E)

        self.devkitGameIDLabel = ttk.Label(self, text="Devkit Game ID")
        self.devkitGameIDLabel.bind("<Enter>", self.updateDevkitGameIDLabelEntered)
        self.devkitGameIDLabel.bind("<Leave>", self.updateLabelExited)
        self.devkitGameIDLabel.grid(row=15, column=2, sticky=E)

        self.lastPlaytimeLabel = ttk.Label(self, text="Last Playtime")
        self.lastPlaytimeLabel.bind("<Enter>", self.updateLastPlaytimeLabelEntered)
        self.lastPlaytimeLabel.bind("<Leave>", self.updateLabelExited)
        self.lastPlaytimeLabel.grid(row=16, column=2, sticky=E)

        self.tagsLabel = ttk.Label(self, text="Tags")
        self.tagsLabel.bind("<Enter>", self.updateTagsLabelEntered)
        self.tagsLabel.bind("<Leave>", self.updateLabelExited)
        self.tagsLabel.grid(row=17, column=2, sticky=E)

        # Adding the entry fields for the corresponding elements
        self.scIndex = StringVar()
        self.scIndex.set("---")
        self.displayIndex = ttk.Entry(self, textvariable=self.scIndex).grid(row=3, column=3, columnspan=2, sticky=(W,E))

        self.scAppName = StringVar()
        self.scAppName.set("---")
        self.displayAppName = ttk.Entry(self, textvariable=self.scAppName).grid(row=4, column=3, columnspan=2, sticky=(W,E))

        self.scExePath = StringVar()
        self.scExePath.set("---")
        self.displayExePath = ttk.Entry(self, textvariable=self.scExePath).grid(row=5, column=3, columnspan=2, sticky=(W,E))

        self.scStartDir = StringVar()
        self.scStartDir.set("---")
        self.displayStartDir = ttk.Entry(self, textvariable=self.scStartDir).grid(row=6, column=3, columnspan=2, sticky=(W,E))

        self.scIcon = StringVar()
        self.scIcon.set("---")
        self.displayIcon = ttk.Entry(self, textvariable=self.scIcon).grid(row=7, column=3, columnspan=2, sticky=(W,E))
        # =======================================================
        self.scShortcutPath = StringVar()
        self.scShortcutPath.set("---")
        self.displayShortcutPath = ttk.Entry(self, textvariable=self.scShortcutPath).grid(row=8, column=3, columnspan=2, sticky=(W,E))

        self.scLaunchOptions = StringVar()
        self.scLaunchOptions.set("---")
        self.displayLaunchOptions = ttk.Entry(self, textvariable=self.scLaunchOptions).grid(row=9, column=3, columnspan=2, sticky=(W,E))

        self.scIsHidden = StringVar()
        self.scIsHidden.set("---")
        self.displayIsHidden = ttk.Entry(self, textvariable=self.scIsHidden).grid(row=10, column=3, columnspan=2, sticky=(W,E))

        self.scAllowDesktopConfig = StringVar()
        self.scAllowDesktopConfig.set("---")
        self.displayAllowDesktopConfig = ttk.Entry(self, textvariable=self.scAllowDesktopConfig).grid(row=11, column=3, columnspan=2, sticky=(W,E))

        self.scAllowOverlay = StringVar()
        self.scAllowOverlay.set("---")
        self.displayAllowOverlay = ttk.Entry(self, textvariable=self.scAllowOverlay).grid(row=12, column=3, columnspan=2, sticky=(W,E))
        # =======================================================
        self.scOpenVR = StringVar()
        self.scOpenVR.set("---")
        self.displayOpenVR = ttk.Entry(self, textvariable=self.scOpenVR).grid(row=13, column=3, columnspan=2, sticky=(W,E))

        self.scDevkit = StringVar()
        self.scDevkit.set("---")
        self.displayDevkit = ttk.Entry(self, textvariable=self.scDevkit).grid(row=14, column=3, columnspan=2, sticky=(W,E))

        self.scDevkitGameID = StringVar()
        self.scDevkitGameID.set("---")
        self.displayDevkitGameID = ttk.Entry(self, textvariable=self.scDevkitGameID).grid(row=15, column=3, columnspan=2, sticky=(W,E))

        self.scLastPlaytime = StringVar()
        self.scLastPlaytime.set("---")
        self.displayLastPlaytime = ttk.Entry(self, textvariable=self.scLastPlaytime).grid(row=16, column=3, columnspan=2, sticky=(W,E))

        self.scTags = StringVar()
        self.scTags.set("---")
        self.displayTags = ttk.Entry(self, textvariable=self.scTags).grid(row=17, column=3, columnspan=2, sticky=(W,E))
        # =======================================================
        # Add Previous Entry button
        ttk.Button(self, text="<<< Previous Entry", command=None).grid(row=18, column=1, sticky=(W,E)) # needs command

        # Add Next Entry Button
        ttk.Button(self, text="Next Entry >>>", command=None).grid(row=18, column=2, sticky=(W,E)) # needs command

        # Add Remove Entry button
        ttk.Button(self, text="Remove Entry", command=None).grid(row=18, column=3, sticky=(W,E)) # needs command

        # Add Add/Update Entry button
        ttk.Button(self, text="Add/Update Entry", command=None).grid(row=18, column=4, sticky=(W,E)) # needs command

        # Add treeview
        # TODO

        # Adjust layout - give some room around children
        for child in self.winfo_children():
            child.grid_configure(padx=2, pady=5)

    # Need functions for when a mouse enters each particular label to update and 
    # display the explaination text
    def updateIndexLabelEntered(self, event=None):
        self.mainDescriptionHeader.configure(text="Index number of entry, starting with 0.")

    def updateAppNameLabelEntered(self, event=None):
        self.mainDescriptionHeader.configure(text="Name of the non-Steam game.")

    def updateExePathLabelEntered(self, event=None):
        self.mainDescriptionHeader.configure(text="Full filepath to the actual .exe file.")

    def updateStartDirLabelEntered(self, event=None):
        self.mainDescriptionHeader.configure(text="Folder filepath containing .exe file.")

    def updateIconLabelEntered(self, event=None):
        self.mainDescriptionHeader.configure(text="256x256 .png file location.")

    # =========================================================================

    def updateShortcutPathLabelEntered(self, event=None):
        self.mainDescriptionHeader.configure(text="(deprecated?) Steam shortcut URL.")
    
    def updateLaunchOptsLabelEntered(self, event=None):
        self.mainDescriptionHeader.configure(text="Advanced flags to add to executable.")

    def updateIsHiddenLabelEntered(self, event=None):
        self.mainDescriptionHeader.configure(text="Set to 0 for visible, 1 for hidden.")

    def updateAllowDesktopCfgLabelEntered(self, event=None):
        self.mainDescriptionHeader.configure(text="Set to 0 to disable, 1 to enable controller desktop config.")

    def updateAllowOverlayLabelEntered(self, event=None):
        self.mainDescriptionHeader.configure(text="Set to 0 to disable, 1 to enable Steam Overlay.")

    # =========================================================================

    def updateOpenVRLabelEntered(self, event=None):
        self.mainDescriptionHeader.configure(text="Set to 0 to disable, 1 to add VR Library category.")

    def updateDevkitLabelEntered(self, event=None):
        self.mainDescriptionHeader.configure(text="(unknown) Ok to leave blank.")

    def updateDevkitGameIDLabelEntered(self, event=None):
        self.mainDescriptionHeader.configure(text="(unknown) Ok to leave blank.")

    def updateLastPlaytimeLabelEntered(self, event=None):
        self.mainDescriptionHeader.configure(text="(deprecated) Ok to blank this out - may contain gibberish.")

    def updateTagsLabelEntered(self, event=None):
        self.mainDescriptionHeader.configure(text="List of categories/tags used by user on this entry.")

    def updateLabelExited(self, event=None):
        self.mainDescriptionHeader.configure(text="""How To Use:
Provide the filepath (including drive letter) to the Steam shortcuts.vdf via the File menu pulldown. 
Example: \"C:\\Program Files (x86)\\Steam\\userdata\\<user_id>\\config\\shortcuts.vdf\"
<user_id>: can be any set of numbers, check your Steam install setup.""")