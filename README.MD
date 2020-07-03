# Steam Shortcut Manager GUI

This Steam Shortcut Manager GUI project is intended to help work with a Steam install's shortcuts.vdf file - the list of data about non-Steam games added to Steam.

![](https://github.com/millerv/Steam-Shortcut-Manager/blob/master/SSMGUI_version_0.1.png)



# FYI: IN PRE-RELEASE, INCOMPLETE AT THIS TIME

Things I have to do to get to a 1.0 release:
1. Since this was made in Python 3.7.7, I should? be able to create an easy installer to make nice packages for this.

Things beyond 1.0 release:
1. Working with the localconfig.vdf to let folks update their non-Steam game images in Steam.
2. Getting the Category sorter working in the main SSM gui.
3. Maybe remove shortcuts.py - not much of this DNA remains in the work I did at this point.
4. Maybe remove crc_algorithms.py - but I might need it for the localconfig image work...

# Getting Started (when I actually get here)

1. Make sure Steam is closed so that changes made in the non-Steam games list will work correctly.
2. Provide the filepath (including drive letter on Windows) to the shortcuts.vdf file location. Example: "C:\Program Files (x86)\Steam\userdata\< user_id >\config\shortcuts.vdf"

# License

SEE LICENSE.MD

# Acknowledgments

* CorporalQuesadilla for the prior work on a command line based Steam Shortcut Manager.
* Scott Rice for ICE,and his work finding how steam:// IDs are generated.
* PsychoTheHedgehog for also documenting how shortcuts.vdf is laid out.
* Fernanda Vergara (Roboxel) for use of the Kawaii Game Icon (available on itch.io!)
* Doc Buford for the original idea to visualize this in a friendlier format.
