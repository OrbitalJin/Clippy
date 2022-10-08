from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
import sys, os

from interface import Ui_MainWindow

class App(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
		self.setWindowTitle("ClipPy")
		self.setRoundEdges()
		self.x_shift = 0#-10
		self.y_shift = 0#-360
		self.center()
		self.setFocus()
		self.ui.searchBar.setFocus()
		QShortcut(QKeySequence("Ctrl+Q"), self, self.close)
X
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

if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = App()
	window.show()
	sys.exit(app.exec_())