# The shortcuts.vdf file consists of a list of entries with uniform
# data.

class SSMShortCutEntry:
    '''
    The SSMShortCutEntry class encompasses handling individual non-Steam
    game entries that derive from shortcuts.vdf

    Attributes:
        dataTypeNull: NUL in plain text ANSI
        dataTypeString: SOH in plain text ANSI
        dataTypeBool: STX in plain text ANSI
        dataTypeBackSp: BS in plain text ANSI
        dataTypeNullFour: Repeats the NUL char x4
        dataTypeStrNullGroup: SOH then NUL char x3
        dataTypeBackSpPair: BS char x2
    '''
    # When viewing shortcuts.vdf in a plaintext editor like Notepad++,
    # it looks like ANSI encoding, with all entries on a single line.
    #
    # -------------------------------------------------------------------------
    # Special characters section - used to denote data type and/or
    # used as delimiters - x00 indicates a list, x01 a String, and x02 a Bool
    dataTypeNull        =       '\x00'
    dataTypeString      =       '\x01'
    dataTypeBool        =       '\x02'
    dataTypeBackSp      =       '\x08'

    dataTypeNullFour        =       '\x00\x00\x00\x00'
    dataTypeStrNullGroup    =       '\x01\x00\x00\x00'
    dataTypeBackSpPair      =       '\x08\x08'

    def __init__(self, var_entryID, var_appName, var_unquotedPath, var_startDir, var_iconPath,
                 var_shortcutPath, var_launchOptions, var_isHidden, var_allowDeskConf, var_allowOverlay,
                 var_openVR, var_devkit, var_devkitGameID, var_lastPlayTime, var_tags):
    '''
    Creates an entry for a non-steam game.
    
    Args:
        arg (var_entryID): index for the entry in a list
        arg (var_appName): name of the non-Steam game
        arg (var_unquotedPath): full path to the exe
        arg (var_startDir): full path to containing folder above exe
        arg (var_iconPath): full path to 256x256 (ideally) png image
        arg (var_shortcutPath): (deprecated) a Steam URL that exists as a desktop shortcut to the Steam entry
        arg (var_launchOptions): flags used on starting the title
        arg (var_isHidden): use 1 to hide, 0 to show
        arg (var_allowDeskConf): controller desktop config in game, 1 to enable, 0 to disable(?)
        arg (var_allowOverlay): 1 to enable, 0 to disable Steam Overlay
        arg (var_openVR): 1 to enable, 0 to disable in VR Library category
        arg (var_devkit): unknown
        arg (var_devkitGameID): unknown
        arg (var_lastPlayTime): (deprecated) - use 0
        arg (var_tags): a list of categories, can be multiple tags
    '''    
        var_shortcutPath = ""
        var_devkit = ""
        var_devkitGameID = ""
        var_lastPlayTime = ""
        # Steam doesn't appear to care about camel case or all lower case,
        # but we're going to use camel case since most parts of the entry
        # already do and we'll keep it consistent with that
        # ---------------------------------------------------------------------
        # Table of elements that make up a single non-Steam game shortcut
        #
        # Element                    # DataType          # PlainTextName         # Delimiter     # InputElement      # Delimiter
        self.full_entryID        =                                               dataTypeNull +  var_entryID       + dataTypeNull
        self.full_appName        =   dataTypeString +    'AppName'             + dataTypeNull +  var_appName       + dataTypeNull
        self.full_quotedPath     =   dataTypeString +    'Exe'                 + dataTypeNull +  var_unquotedPath  + dataTypeNull
        self.full_startDir       =   dataTypeString +    'StartDir'            + dataTypeNull +  var_startDir      + dataTypeNull
        self.full_iconPath       =   dataTypeString +    'icon'                + dataTypeNull +  var_iconPath      + dataTypeNull
        #
        self.full_shortchutPath  =   dataTypeString +    'ShortcutPath'        + dataTypeNull +  var_shortcutPath  + dataTypeNull
        self.full_launchOptions  =   dataTypeString +    'LaunchOptions'       + dataTypeNull +  var_launchOptions + dataTypeNull
        self.full_isHidden       =   dataTypeBool   +    'IsHidden'            + dataTypeNull +  var_isHidden      + dataTypeNullFour
        self.full_allowDeskConf  =   dataTypeBool   +    'AllowDesktopConfig'  + dataTypeNull +  var_allowDeskConf + dataTypeStrNullGroup
        self.full_allowOverlay   =   dataTypeBool   +    'AllowOverlay'        + dataTypeNull +  var_allowOverlay  + dataTypeStrNullGroup
        #
        self.full_openVR         =   dataTypeBool   +    'OpenVR'              + dataTypeNull +  var_openVR        + dataTypeNullFour
        self.full_devkit         =   dataTypeBool   +    'Devkit'              + dataTypeNull +  var_devkit        + dataTypeNullFour
        self.full_devkitGameID   =   dataTypeString +    'DevkitGameID'        + dataTypeNull +  var_devkitGameID  + dataTypeNull
        self.full_lastPlayTime   =   dataTypeBool   +    'LastPlayTime'        + dataTypeNull +  var_lastPlayTime  + dataTypeNullFour
        self.full_tags           =   dataTypeNull   +    'tags'                + dataTypeNull +  var_tags          + dataTypeBackSpPair

    def createTagsList(self, var_tags):
        # There's actually a list of tags that need to be processed

        self.full_tags = dataTypeNull + 'tags' + dataTypeNull + var_tags + dataTypeBackSpPair
