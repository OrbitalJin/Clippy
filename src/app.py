from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *

from ui.interface import Ui_MainWindow
from components.scrollbar import CScrollBar
from components.clipWidget import ClipWidget

from utils.hotkeyWorker import HotKeyWorker
from utils.clipWorker import ClipListener

from tinydb import TinyDB, Query
import pyperclip as cliplib
import sys, os

if sys.platform in "linux darwin": host = "*unix"; import notify2
else: host = "win32"; from win10toast_click import ToastNotifier
if host == "win32": winNotify = ToastNotifier()
else: notify2.init("ClipPy - Notifier")

PATH_TO_DB = "./data/db.json"

class App(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.setupSystemTray()
		self.adjustUi()

		self.ClipListener = ClipListener()
		self.ClipListener.start()	
		
		self.HotKeys = ['Ctrl+ALT+H', 'Ctrl+ALT+Z', 'Ctrl+ALT+C']
		self.HotKeyListener = HotKeyWorker(self.HotKeys)
		self.HotKeyListener.start()

		self.connectSignalsAndSlots()
		self.setupShortcuts()
		self.center()

		self.loadClips()

# Setup:
	def adjustUi(self):
		self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Popup)
		self.setWindowTitle("ClipPy")
		self.setRoundEdges()
		self.setFocus()
		self.ui.searchBar.setFocus()
		self.ui.searchBar.setContextMenuPolicy(Qt.NoContextMenu)
		self.ui.clipsListWidget.setVerticalScrollBar(CScrollBar())

	def setupShortcuts(self):
		QShortcut(QKeySequence('Ctrl+Q'), self).activated.connect(self.closeApp)

	def setupSystemTray(self):
		self.TrayIcon = QSystemTrayIcon(QIcon("../res/icons/icon_clipboard.svg"))
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

	def connectSignalsAndSlots(self):
		self.ClipListener.newClipSignalEvent.connect(lambda clip: self.newClipEventSlot(clip))
		self.ClipListener.unavailableClipEvent.connect(lambda status: print(f"ClipListener: {status}"))
		self.HotKeyListener.combinationDetected.connect(lambda cmd: self.hotkeySlot(cmd))

		self.ui.clipsListWidget.itemActivated.connect(self.itemClipActivatedCallback)
		self.ui.searchBar.textChanged.connect(lambda text: self.filterClipboard(text))

		self.ui.settingsBtn.clicked.connect(lambda: self.HotKeyListener.doWork())
		self.ui.closeAppBtn.clicked.connect(self.closeApp)

# Slots:
	@Slot()
	def newClipEventSlot(self, clip: str):
		item = QListWidgetItem()
		widget = ClipWidget(clip, item, self)
		item.setSizeHint(QSize(15, 28))
		self.ui.clipsListWidget.insertItem(0, item)
		self.ui.clipsListWidget.setItemWidget(item, widget)
		# item.setSizeHint(widget.sizeHint())



	@Slot()
	def hotkeySlot(self, cmd: str):
		def c():
			if not self.isVisible():self.center()
			self.setVisible(not self.isVisible())

		if cmd == "h": self.ui.clipsListWidget.clear()
		if cmd == "z": self.itemClipActivatedCallback(self.ui.clipsListWidget.item(1)) if self.ui.clipsListWidget.count() > 1 else None
		if cmd == "c": c()

# Callbacks:
	def itemClipActivatedCallback(self, item: QListWidgetItem):
		def  sling_method():
			self.ui.statusLabel.setText("ClipPy v.0.1")
			self.ui.statusLabel.setStyleSheet("color: grey;")

		txt = self.ui.clipsListWidget.itemWidget(item).getClipContent()
		cliplib.copy(txt)
		self.pushClipToDataBase(item.text())
		self.notify("ClipPy - Notifier", f"{item.text()} copied to the clipboard!", 1000)

		self.ui.statusLabel.setStyleSheet("color: #5E81AC;")
		self.ui.statusLabel.setText(f"Entry copied to the clipboard!")
		QTimer.singleShot(3500, sling_method)
		QTimer.singleShot(400, self.hide)

# Methods:
	def removeClipWidgetItem(self, item: QListWidgetItem):
		index = self.ui.clipsListWidget.indexFromItem(item).row()
		item = self.ui.clipsListWidget.takeItem(index)

	def loadClips(self):
		self.db = TinyDB(PATH_TO_DB)
		for clip in self.db: self.newClipEventSlot(clip["content"])

	def pushClipToDataBase(self, clip: str):
		pass

	def filterClipboard(self, text: str):
		for index in range(self.ui.clipsListWidget.count()):
			item = self.ui.clipsListWidget.item(index)
			item.setHidden(not text.lower() in item.text().lower())

	def notify(self, title: str, msg: str, timeout: int):
		if host == "*unix":
			notification = notify2.Notification(summary = title, message = msg)
			notification.set_timeout(timeout)	
			notification.show()
		else: winNotify.show_toast(title, msg, duration = int(timeout/1000), threaded = True)

# Internal Events:
	def hideEvent(self, event: QEvent):
		self.TrayIcon.show()
		print("Hidden")

	def showEvent(self, event: QEvent):
		self.TrayIcon.hide()
		print("Shown")

# Private:
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
		self.ClipListener.stop()
		self.ClipListener.quit()
		self.ClipListener.wait()
		self.HotKeyListener.stop()
		self.HotKeyListener.quit()
		self.HotKeyListener.wait()
		print("ClipListener Thread: ", self.ClipListener.isRunning())
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
    if host == "win32": app.setFont(font)
    elif host in "linux darwin": pass
    return app

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app = fontCheck(app)
    window = App()
    window.show()
    sys.exit(app.exec_())
