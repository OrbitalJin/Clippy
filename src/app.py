from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from utils.clip_worker import ClipListener
import pyperclip as clip
import sys, os

from interface import Ui_MainWindow

class App(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.adjustUi()
		self.ClipListener = ClipListener()
		self.connectSignalsAndSlots()
		self.ClipListener.start()
		
		self.x_shift = 0#-10
		self.y_shift = 0#-360
		self.center()

		QShortcut(QKeySequence('Ctrl+Q'), self).activated.connect(lambda: self.close())

	def adjustUi(self):
		self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
		self.setWindowTitle("ClipPy")
		self.setRoundEdges()
		self.setFocus()
		self.ui.searchBar.setFocus()

	def connectSignalsAndSlots(self):
		self.ClipListener.newClipSignalEvent.connect(lambda clip: self.newClipEventSlot(clip))
		self.ClipListener.unavailableClipEvent.connect(lambda status: print(f"ClipListener: {status}"))
		self.ui.settingsBtn.clicked.connect(lambda: print(self.ClipListener.ThreadActive))

		self.ui.clipsListWidget.itemDoubleClicked.connect(self.itemClipActivatedCallback)

	@Slot()
	def newClipEventSlot(self, clip: str):
		self.ui.clipsListWidget.addItem(clip)


	def itemClipActivatedCallback(self, item: QListWidgetItem):
		print(f"{item.text()} copied to the clipboard!")
		clip.copy(item.text())

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

	def leaveEvent(self, QEvent):
		if not self.isActiveWindow():
			print("yo")

	def close(self):
		self.ClipListener.stop()
		self.ClipListener.wait()

if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = App()
	window.show()
	sys.exit(app.exec_())