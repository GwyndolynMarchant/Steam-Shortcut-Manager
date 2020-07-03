# Steam Shortcut Manager GUI

This Steam Shortcut Manager GUI project is intended to help work with a Steam install's shortcuts.vdf file - the list of data about non-Steam games added to Steam.

![](https://github.com/millerv/Steam-Shortcut-Manager/blob/master/SSMGUI_version_0.1.png)



# 1.0 Release Now available!
This is the first 'build' of the Steam Shortcut Manager GUI, hooray me. See "Releases."

Things beyond 1.0 release:
1. Working with the localconfig.vdf to let folks update their non-Steam game images in Steam.
2. Getting the Category sorter working in the main SSM gui.
3. Maybe remove shortcuts.py - not much of this DNA remains in the work I did at this point.
4. Maybe remove crc_algorithms.py - but I might need it for the localconfig image work...

# Getting Started

Note: Users need to be familiar with their Steam install and how to navigate through filepaths to get to the non-Steam game executable files.

1. Make sure Steam is closed so that changes made in the non-Steam games list will work correctly.
2. Provide the filepath (including drive letter on Windows) to the shortcuts.vdf file location. Example: "C:\Program Files (x86)\Steam\userdata\< user_id >\config\shortcuts.vdf"
3. Refer to the About menu and/or mouseover on entry fieldnames for more information and advice.
4. Log any issues to the issue tracker with as much info as possible, screenshots are ideal so I can see what you see.
5. Pull requests welcomed!

# License

SEE LICENSE.MD

# Acknowledgments

* CorporalQuesadilla for the prior work on a command line based Steam Shortcut Manager.
* Scott Rice for ICE,and his work finding how steam:// IDs are generated.
* PsychoTheHedgehog for also documenting how shortcuts.vdf is laid out.
* Fernanda Vergara (Roboxel) for use of the Kawaii Game Icon (available on itch.io!)
* Doc Buford for the original idea to visualize this in a friendlier format.
