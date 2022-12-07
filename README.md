# Goal
ClipPy aims to solve a commonly encountered ergonomic issue when copying content into the clipboard, by tracing back it's history, filtering it accordingly and giving it's users the ability to track, save, store and reuse the current and paste content at will.


# TODO - Priority Pool
- [ ] TODO: ReImplement the Clipboard logic using `QApplication.clipboard()`, it supports images too.
- [ ] TODO: Save history locally on the machine. Considering tinyDB as a DB backend: https://tinydb.readthedocs.io/en/latest/index.html

# Checked TODOs
- [X] DONE: Added a self destruct button to each ClipWidget by passing a referecence to the item and parent (app), and calling the `removeClipWidget` method.
- [X] DONE: Mess around with the Qt.Popup flag/type to make the window dissapear and fallback to tray upon losing focus.
- [x] DONE: Make the app globally summonable.
- [x] DONE: Listen to clipboard events and add new entries to the stack.
- [x] DONE: Move selection to the top of the stack upon double click if it's different from the current top of the stack.
- [x] DONE: Notify when operation has been performed on the clipboard.
- [x] DONE: Implemented Shortcuts (not globally) Clear, Last, Grab, Quit.
- [x] DONE: Search bar to filter through the entries.

# Dropped TODOs
- [ ] Clip transform/filter method in the ClipListener worker to strip and such.

# Features
+ Ergonomy:
    * [X] Shortcut summoning.
    * [ ] Support hyper links urls and open in browser tab.
+ Navigation:
    * [x] Browsing plain-text clipboard history and automatically pasting any selected entry to the clipboard.
    * [ ] Organize by date or filter parameters.
+ Images:
    * [ ] Image support.
    * [ ] Imgur upload support. @ https://github.com/Imgur/imgurpython
+ Miscellaneous:
    * [ ] Export clipboard history as a plain-text file.

# Known Issues / Bug Report
- [X] Text overflows of custom item instead of truncating to a normalized size. *(Sort of fixed)*.
> ~~None so far, strange huh?~~

# Fixed Bugs
- [X] Fixed: Getting the text from a QListWidget's Widget instead of the item itself.
- [X] Fixed: Notification backend conflicting between different operating systems.
- [x] Fixed: QDesktop deprecation warning by replacing `QApplication.desktop().screenNumber` with `QGuiApplication.screenAt(QApplication.desktop())`.

# Support
+ On Windows, no additional modules are needed.

+ On Mac, the pyobjc module is used, falling back to the pbcopy and pbpaste cli
    commands. (These commands should come with OS X.).

+ On Linux, install xclip, xsel, or wl-clipboard (for "wayland" sessions) via package manager.
- For example, in Debian:
    - sudo apt-get install xclip
    - sudo apt-get install xsel
    - sudo apt-get install wl-clipboard

- Or in Arch:
    - (sudo pacman | yay) -S install xclip
    - (sudo pacman | yay) -S install xsel
    - (sudo pacman | yay) -S install wl-clipboard

Otherwise on Linux, you will need the gtk or PyQt5+/PySide2+ modules installed.

Gtk and PyQt4 modules are not available for Python 3, and this module does not work with PyGObject, and support isn't planned.
Cygwin is currently not supported.

Note: There seems to be a way to get gtk on Python 3, according to:
    https://askubuntu.com/questions/697397/python3-is-not-supporting-gtk-module
