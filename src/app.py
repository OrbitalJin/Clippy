from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *

from ui.interface import Ui_MainWindow

from components.scrollbar import CScrollBar
from components.clipWidget import ClipWidget

from utils.hotkeyManager import HotKeyManager
from utils.clipManager import ClipManager
from utils.itemManager import ItemManager

import pyperclip as cliplib
from pprint import pprint
import notify2, sys, os

HOST 		 = sys.platform
PATH_TO_DB   = "./data/db.json"
PATH_TO_ICON = "../res/icons/icon_clipboard.svg"

class App(QMainWindow):
	notify2.init("ClipPy - Notifier")
	def __init__(self):
		QMainWindow.__init__(self)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.setupSystemTray()
		self.adjustUi()

		self.HotKeys = ['Ctrl+ALT+C']
		self.HotKeyListener = HotKeyManager(self.HotKeys)
		self.HotKeyListener.start()

		self.ClipboardManager = ClipManager(clipboard, self)

		self.ItemManager = ItemManager(PATH_TO_DB, self)
		self.ItemManager.populateList()

		self.connectSignalsAndSlots()
		self.setupShortcuts()
		self.center()

# Setup:
	def adjustUi(self):
		self.setWindowTitle("Clippy")
		self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Popup)
		self.setAttribute(Qt.WA_TranslucentBackground)
		self.setWindowOpacity(.70)
		self.setFocus()
		self.ui.searchBar.setFocus()
		self.ui.searchBar.setContextMenuPolicy(Qt.NoContextMenu)
		self.ui.clipsListWidget.setVerticalScrollBar(CScrollBar())
		self.ui.clipsListWidget.setCurrentRow(-1)

	def setupShortcuts(self):
		QShortcut(QKeySequence(Qt.Key_Delete), self).activated.connect(self.popItemFromTop)
		QShortcut(QKeySequence(Qt.CTRL | Qt.Key_Q), self).activated.connect(self.closeApp)
		QShortcut(QKeySequence(Qt.Key_Up), self).activated.connect(self.ItemManager.gotToPrevVisibleItem)
		QShortcut(QKeySequence(Qt.Key_Down), self).activated.connect(self.ItemManager.gotToNextVisibleItem)

	def connectSignalsAndSlots(self):
		self.ClipboardManager.processedClip.connect(lambda payload: self.newClipEventSlot(payload))
		self.HotKeyListener.combinationDetected.connect(lambda cmd: self.hotkeySlot(cmd))

		self.ui.clipsListWidget.itemActivated.connect(self.itemClipActivatedCallback)
		self.ui.searchBar.textChanged.connect(lambda text: self.filterClipboard(text))
		self.ui.searchBar.returnPressed.connect(lambda: self.ui.clipsListWidget.setFocus())
		self.ui.searchBar.returnPressed.connect(self.ItemManager.gotToFirstVisibleItem)

# Slots:
	@Slot()
	def newClipEventSlot(self, clip: str):
		self.ItemManager.newItem(clip)

	@Slot()
	def hotkeySlot(self, cmd: str):
		if cmd == "h": self.ui.clipsListWidget.clear()
		if cmd == "z": self.itemClipActivatedCallback(self.ui.clipsListWidget.item(1)) if self.ui.clipsListWidget.count() > 1 else None
		if cmd == "c": self.summon()

# Callbacks:
	def itemClipActivatedCallback(self, item: QListWidgetItem):
		itemData = self.ItemManager.getItemData(item)
		self.ClipboardManager.pasteContentFromData(itemData)
		self.notify(f"{item.text()} copied to the clipboard!", 500)
		QTimer.singleShot(200, self.hide)

# Methods:
	def removeClipWidgetItem(self, item: QListWidgetItem):
		index = self.ui.clipsListWidget.indexFromItem(item).row()
		item = self.ui.clipsListWidget.takeItem(index)

	def popItemFromTop(self):
		item = self.ui.clipsListWidget.currentItem()
		self.removeClipWidgetItem(item)

	def filterClipboard(self, text: str):
		for index in range(self.ui.clipsListWidget.count()):
			item = self.ui.clipsListWidget.item(index)
			content = self.ItemManager.getItemContent(item)
			item.setHidden(not text.lower() in content.lower())

	def notify(self, msg: str, timeout: int):
		title = "ClipPy - Notifier"
		notification = notify2.Notification(summary = title, message = msg)
		notification.set_timeout(timeout)
		notification.show()

	def summon(self):
		if not self.isVisible(): self.center()
		self.setVisible(not self.isVisible())

# Internal Events:
	def hideEvent(self, event: QEvent):
		self.TrayIcon.show()
		# self.ui.clipsListWidget.setCurrentRow(0)

	def showEvent(self, event: QEvent):
		self.TrayIcon.hide()
		self.ui.searchBar.setFocus()

# Private:
	def setupSystemTray(self):
		self.TrayIcon = QSystemTrayIcon(QIcon(PATH_TO_ICON))
		self.TrayIcon.setToolTip("ClipPy")
		self.TrayMenu = QMenu(self)
		exitAction = self.TrayMenu.addAction("Exit")
		exitAction.triggered.connect(self.closeApp)
		showAction = self.TrayMenu.addAction("Show")
		showAction.triggered.connect(self.show)
		showAction.triggered.connect(self.ui.searchBar.setFocus)
		settingsAction = self.TrayMenu.addAction("Settings")
		self.TrayIcon.setContextMenu(self.TrayMenu)
		self.TrayIcon.show()

	def setRoundEdges(self):
		self.radius = 8.0
		self.path = QPainterPath()
		self.path.addRoundedRect(QRectF(self.rect()), self.radius, self.radius)
		self.mask = QRegion(self.path.toFillPolygon().toPolygon())
		self.setMask(self.mask)
	
	def center(self):
		self.x_shift = 0 #-10
		self.y_shift = 0 #-360
		self.frame = self.frameGeometry()
		screen = QGuiApplication.screenAt(QApplication.desktop().cursor().pos())
		centerPoint = screen.availableGeometry().center()
		self.frame.moveCenter(centerPoint)
		self.move(self.frame.topLeft().x()+self.x_shift, self.frame.topLeft().y()+self.y_shift)

	def stopRunningThreads(self):
		self.HotKeyListener.stop()
		self.HotKeyListener.quit()
		self.HotKeyListener.wait()
		print("HotKeyListener Thread: ", self.HotKeyListener.isRunning())

	def closeApp(self):
		self.setWindowFlags(self.windowFlags() & ~Qt.Popup) # Removing the popup flag because it prevents the app from fulling closing
		self.stopRunningThreads()
		self.close()
		sys.exit(0)											# To fully close the application flagged as a popup

# Entry Point:
def fontCheck(app):
    font = QFont("Segoe UI")
    font.setPointSize(11)
    if HOST == "win32": app.setFont(font)
    elif HOST in "linux darwin": pass
    return app

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app = fontCheck(app)
    clipboard = QApplication.clipboard()
    window = App()
    window.show()
    sys.exit(app.exec_())
