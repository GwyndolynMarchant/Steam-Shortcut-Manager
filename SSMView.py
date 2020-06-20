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
        
        # Add several entry fields

        # Set up Categories
        ttk.Label(self, text="Categories").grid(row=1, column=1, sticky=W)
        
        # Spacer
        ttk.Label(self, text="       ").grid(row=1, column=2)

        # Show descriptive text
        ttk.Label(self, text="Provide the filepath (including drive letter) to the Steam shortcuts.vdf. \nExample: \"C:\\Program Files (x86)\\Steam\\userdata\\<user_id>\\config\\shortcuts.vdf\"\n<user_id>: can be any set of numbers, check your Steam install setup.").grid(row=1, column=3, sticky=E)

        # Add Remove Entry button
        ttk.Button(self, text="Remove Entry", command=None).grid(row=3, column=3, sticky=E) # needs command

        # Add Add/Update Entry button
        ttk.Button(self, text="Add/Update Entry", command=None).grid(row=4, column=3, sticky=E) # needs command

        # Add treeview
