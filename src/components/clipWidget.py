from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

class ClipWidget(QWidget):
    # https://stackoverflow.com/questions/73302473/pyqt5-delete-a-qlistwidgetitem-when-button-in-widget-is-pressed
    def __init__ (self, data, item, parent):
        super(ClipWidget, self).__init__(parent)
        self._data = data
        self._parent = parent
        self._item = item
        self._id = self._data["id"]

        self.clipContent = self._data["content"]
        self.LabelContent = self.clipContent.split("\n")[0].strip() if self.clipContent.count("\n") else self.clipContent

        self.textQVBoxLayout = QVBoxLayout()
        self.textLabel = QLabel()

        self.allQHBoxLayout = QHBoxLayout()
        self.allQHBoxLayout.setContentsMargins(6, 4, 6, 4)

        self.deleteSelfBtn = QPushButton("x")
        self.deleteSelfBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.deleteSelfBtn.setStyleSheet("color: grey;")
        self.deleteSelfBtn.clicked.connect(self.deleteSelfCallback)

        self.textQVBoxLayout.addWidget(self.textLabel)
        self.allQHBoxLayout.addLayout(self.textQVBoxLayout, 1)
        self.allQHBoxLayout.addWidget(self.deleteSelfBtn, 0)
        self.setLayout(self.allQHBoxLayout)
        self.setClipLabel(self.LabelContent)

    def setClipLabel (self, text):
        self.textLabel.setText(text)
    
    def getClipContent(self):
        return self.clipContent

    def deleteSelfCallback(self):
        self._parent.ItemManager.deleteItemFromDataBase(self._id)
        self._parent.removeClipWidgetItem(self._item)
        self.deleteLater()