from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from ui.interface import Ui_MainWindow
from components.scrollbar import CScrollBar

from utils.clipWorker import ClipListener
import pyperclip as clip
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
		
		self.connectSignalsAndSlots()
		
		self.x_shift = 0#-10
		self.y_shift = 0#-360
		self.center()

		QShortcut(QKeySequence('Ctrl+Q'), self).activated.connect(lambda: self.close())
		QShortcut(QKeySequence('Ctrl+ALT+P'), self).activated.connect(lambda: self.setVisible(not self.isVisible()))

	def adjustUi(self):
		self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
		self.setWindowTitle("ClipPy")
		self.setRoundEdges()
		self.setFocus()
		self.ui.searchBar.setFocus()
		self.ui.searchBar.setContextMenuPolicy(Qt.NoContextMenu)

		scrollBar = CScrollBar()
		self.ui.clipsListWidget.setVerticalScrollBar(scrollBar)

	def connectSignalsAndSlots(self):
		self.ClipListener.newClipSignalEvent.connect(lambda clip: self.newClipEventSlot(clip))
		self.ClipListener.unavailableClipEvent.connect(lambda status: print(f"ClipListener: {status}"))

		self.ui.clipsListWidget.itemDoubleClicked.connect(self.itemClipActivatedCallback)
		self.ui.searchBar.textChanged.connect(lambda text: self.filterClipboard(text))

		self.ui.settingsBtn.clicked.connect(lambda: self.ClipListener.setPaused(not self.ClipListener.isPaused))
		self.ui.closeAppBtn.clicked.connect(self.closeApp)

	@Slot()
	def newClipEventSlot(self, clip: str):
		size = QSize(15, 17)
		item = QListWidgetItem(clip)
		item.setSizeHint(size)
		self.ui.clipsListWidget.insertItem(0, item)

	def itemClipActivatedCallback(self, item: QListWidgetItem):
		def  sling_method():
			self.ui.statusLabel.setText("ClipPy v.0.1")
			self.ui.statusLabel.setStyleSheet("color: grey;")
		
		clip.copy(item.text())

		self.notify("ClipPy - Notifier", f"{item.text()} copied to the clipboard!", 3500)

		self.ui.statusLabel.setStyleSheet("color: #5E81AC;")
		self.ui.statusLabel.setText(f"{item.text()} copied to the clipboard!")
		QTimer.singleShot(3500, sling_method)

	def filterClipboard(self, text: str):
		# self.ui.clipsListWidget.item(index).setHidden(not text.lower() in self.ui.clipsListWidget.item(index).text().lower())
		for index in range(self.ui.clipsListWidget.count()):
			item = self.ui.clipsListWidget.item(index)
			item.setHidden(not text.lower() in item.text().lower())

	def notify(self, title: str, msg: str, timeout: int):
		n = notify2.Notification(summary = title, message = msg)
		n.set_timeout(timeout)	
		n.show()

	def center(self):
	    frameGm = self.frameGeometry()
	    screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
	    centerPoint = QApplication.desktop().screenGeometry(screen).center()
	    frameGm.moveCenter(centerPoint)
	    self.move(frameGm.topLeft().x()+self.x_shift, frameGm.topLeft().y()+self.y_shift)

	def setRoundEdges(self):
	    self.radius = 8.0
	    self.path = QPainterPath()
	    self.path.addRoundedRect(QRectF(self.rect()), self.radius, self.radius)
	    self.mask = QRegion(self.path.toFillPolygon().toPolygon())
	    self.setMask(self.mask)

	def closeApp(self):
		self.ClipListener.stop()
		self.ClipListener.wait()
		self.close()

if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = App()
	window.show()
	sys.exit(app.exec_())
