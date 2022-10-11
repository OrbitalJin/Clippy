from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *

from ui.interface import Ui_MainWindow
from components.scrollbar import CScrollBar

from utils.hotkeyWorker import HotKeyWorker
from utils.clipWorker import ClipListener

import pyperclip as cliplib
import sys, os, notify2

class App(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.adjustUi()
		self.ClipListener = ClipListener()
		self.ClipListener.start()
		notify2.init("ClipPy - Notifier")
		
		self.HotKeys = ['Ctrl+ALT+H', 'Ctrl+ALT+Z', 'Ctrl+ALT+C']
		self.HotKeyListener = HotKeyWorker(self.HotKeys)
		self.HotKeyListener.start()

		self.connectSignalsAndSlots()
		self.setupShortcuts()
		self.center()

# Setup:
	def adjustUi(self):
		self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Popup)
		self.setWindowTitle("ClipPy")
		self.setRoundEdges()
		self.setFocus()
		self.ui.searchBar.setFocus()
		self.ui.searchBar.setContextMenuPolicy(Qt.NoContextMenu)
		self.ui.clipsListWidget.setVerticalScrollBar(CScrollBar())
		self.setMouseTracking(True)

	def setupShortcuts(self):
		QShortcut(QKeySequence('Ctrl+Q'), self).activated.connect(self.closeApp)

	def connectSignalsAndSlots(self):
		self.ClipListener.newClipSignalEvent.connect(lambda clip: self.newClipEventSlot(clip))
		self.ClipListener.unavailableClipEvent.connect(lambda status: print(f"ClipListener: {status}"))
		self.HotKeyListener.combinationDetected.connect(lambda cmd: self.hotkeySlot(cmd))

		self.ui.clipsListWidget.itemDoubleClicked.connect(self.itemClipActivatedCallback)
		self.ui.searchBar.textChanged.connect(lambda text: self.filterClipboard(text))

		self.ui.settingsBtn.clicked.connect(lambda: self.HotKeyListener.doWork())
		self.ui.closeAppBtn.clicked.connect(self.closeApp)

# Slots:
	@Slot()
	def newClipEventSlot(self, clip: str):
		size = QSize(15, 17)
		item = QListWidgetItem(clip)
		item.setSizeHint(size)
		self.ui.clipsListWidget.insertItem(0, item)

	@Slot()
	def hotkeySlot(self, cmd: str):
		if cmd == "h": self.ui.clipsListWidget.clear()
		if cmd == "z": self.itemClipActivatedCallback(self.ui.clipsListWidget.item(1)) if self.ui.clipsListWidget.count() > 1 else None
		if cmd == "c": self.setVisible(not self.isVisible()); self.center()

# Callbacks:
	def itemClipActivatedCallback(self, item: QListWidgetItem):
		def  sling_method():
			self.ui.statusLabel.setText("ClipPy v.0.1")
			self.ui.statusLabel.setStyleSheet("color: grey;")
		
		cliplib.copy(item.text())
		self.pushClipToDataBase(item.text())
		self.notify("ClipPy - Notifier", f"{item.text()} copied to the clipboard!", 3500)

		self.ui.statusLabel.setStyleSheet("color: #5E81AC;")
		self.ui.statusLabel.setText(f"{item.text()} copied to the clipboard!")
		QTimer.singleShot(3500, sling_method)

# Methods:
	def pushClipToDataBase(self, clip: str):
		pass

	def filterClipboard(self, text: str):
		for index in range(self.ui.clipsListWidget.count()):
			item = self.ui.clipsListWidget.item(index)
			item.setHidden(not text.lower() in item.text().lower())

	def notify(self, title: str, msg: str, timeout: int):
		notification = notify2.Notification(summary = title, message = msg)
		notification.set_timeout(timeout)	
		notification.show()

# Private:
	def setRoundEdges(self):
	    self.radius = 8.0
	    self.path = QPainterPath()
	    self.path.addRoundedRect(QRectF(self.rect()), self.radius, self.radius)
	    self.mask = QRegion(self.path.toFillPolygon().toPolygon())
	    self.setMask(self.mask)

	def center(self):
		print(QApplication.desktop().cursor().pos())
		self.x_shift = 0 #-10
		self.y_shift = 0 #-360
		frameGm = self.frameGeometry()
		screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
		centerPoint = QApplication.desktop().screenGeometry(screen).center()
		frameGm.moveCenter(centerPoint)
		self.move(frameGm.topLeft().x()+self.x_shift, frameGm.topLeft().y()+self.y_shift)

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
		sys.exit()											# To fully close the application flagged as a popup

# Entry Point
if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = App()
	window.show()
	sys.exit(app.exec_())
