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
        ttk.Label(self, text="Categories").grid(row=1, column=1, sticky=(N,W))

        # Header for the elements of a shortcut entry
        ttk.Label(self, text="Non-Steam Game entry \nfrom shortcuts.vdf").grid(row=1, column=2, sticky=(N,W))

        # Show descriptive text
        ttk.Label(self, text="""How To Use:
Provide the filepath (including drive letter) to the Steam shortcuts.vdf via the File menu pulldown. 
Example: \"C:\\Program Files (x86)\\Steam\\userdata\\<user_id>\\config\\shortcuts.vdf\"
<user_id>: can be any set of numbers, check your Steam install setup.""").grid(row=1, column=3, columnspan=2, sticky=(N,E))

        # Add several label fields for each element of a shortcut entry
        ttk.Label(self, text="Index Number").grid(row=3, column=2, sticky=E)
        ttk.Label(self, text="AppName").grid(row=4, column=2, sticky=E)
        ttk.Label(self, text="Exe Path").grid(row=5, column=2, sticky=E)
        ttk.Label(self, text="Start Directory").grid(row=6, column=2, sticky=E)
        ttk.Label(self, text="Icon").grid(row=7, column=2, sticky=E)
        # =======================================================
        ttk.Label(self, text="Shortcut Path").grid(row=8, column=2, sticky=E)
        ttk.Label(self, text="Launch Options").grid(row=9, column=2, sticky=E)
        ttk.Label(self, text="IsHidden").grid(row=10, column=2, sticky=E)
        ttk.Label(self, text="Allow Desktop Config").grid(row=11, column=2, sticky=E)
        ttk.Label(self, text="Allow Overlay").grid(row=12, column=2, sticky=E)
        # =======================================================
        ttk.Label(self, text="OpenVR").grid(row=13, column=2, sticky=E)
        ttk.Label(self, text="Devkit").grid(row=14, column=2, sticky=E)
        ttk.Label(self, text="Devkit Game ID").grid(row=15, column=2, sticky=E)
        ttk.Label(self, text="Last Playtime").grid(row=16, column=2, sticky=E)
        ttk.Label(self, text="tags").grid(row=17, column=2, sticky=E)

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
        ttk.Button(self, text="Previous Entry", command=None).grid(row=18, column=1, sticky=(W,E)) # needs command

        # Add Next Entry Button
        ttk.Button(self, text="Next Entry", command=None).grid(row=18, column=2, sticky=(W,E)) # needs command

        # Add Remove Entry button
        ttk.Button(self, text="Remove Entry", command=None).grid(row=18, column=3, sticky=(W,E)) # needs command

        # Add Add/Update Entry button
        ttk.Button(self, text="Add/Update Entry", command=None).grid(row=18, column=4, sticky=(W,E)) # needs command

        # Add treeview
        # TODO

        # Adjust layout - give some room around children
        for child in self.winfo_children():
            child.grid_configure(padx=2, pady=5)
