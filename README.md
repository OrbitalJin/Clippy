# [Objectives]
ClipPy aims to solve a commonly encountered ergonomic issue when copying content into the clipboard, by tracing back it's history, filtering it accoringly and giving it's users the ability to track, save, store and reuse the current and past content at will.

# [Future Features]
+ Browsing plain-text clipboard history and automatically pasting any selected entry to the clipboard.
+ Shortcut summoning
+ Image support
+ Organize by date or filter parameters.
+ Imgur upload support. @ https://github.com/Imgur/imgurpython
+ Export clipboard history as a plain-text file.
+ Support hyper links urls and open in browser tab.

# [Support]
+ On Windows, no additional modules are needed.

+ On Mac, the pyobjc module is used, falling back to the pbcopy and pbpaste cli
    commands. (These commands should come with OS X.).

+ On Linux, install xclip, xsel, or wl-clipboard (for "wayland" sessions) via package manager.
For example, in Debian:
    sudo apt-get install xclip
    sudo apt-get install xsel
    sudo apt-get install wl-clipboard

Or in Arch:
    (sudo pacman | yay) -S install xclip
    (sudo pacman | yay) -S install xsel
    (sudo pacman | yay) -S install wl-clipboard

Otherwise on Linux, you will need the gtk or PyQt5/PyQt4 modules installed.

gtk and PyQt4 modules are not available for Python 3,
and this module does not work with PyGObject yet.

Note: There seems to be a way to get gtk on Python 3, according to:
    https://askubuntu.com/questions/697397/python3-is-not-supporting-gtk-module
Cygwin is currently not supported.