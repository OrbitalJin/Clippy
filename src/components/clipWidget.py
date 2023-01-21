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

        self.clipContent = self._data["content"]
        self.LabelContent = self.clipContent.split("\n")[0].strip() if self.clipContent.count("\n") else self.clipContent

        self.textLabel = QLabel()
        self.textLabel.setStyleSheet("color: #8F8F8F;")
        self.textLabel.setText(self.LabelContent)

        self.textQVBoxLayout = QVBoxLayout()
        self.textQVBoxLayout.addWidget(self.textLabel)

        self.deleteSelfBtn = QPushButton("x")
        self.deleteSelfBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.deleteSelfBtn.setStyleSheet("color: #8F8F8F;")
        self.deleteSelfBtn.clicked.connect(self.deleteSelfCallback)

        self.allQHBoxLayout = QHBoxLayout()
        self.allQHBoxLayout.setContentsMargins(6, 4, 15, 4)
        self.allQHBoxLayout.addLayout(self.textQVBoxLayout, 1)
        self.allQHBoxLayout.addWidget(self.deleteSelfBtn, 0)
        self.setLayout(self.allQHBoxLayout)

    def getClipData(self):
        return self._data
    
    def getClipContent(self):
        return self.clipContent

    def getClipType(self):
        return self._data["type"]

    def getClipID(self):
        return self._data["id"]

    def getClipDate(self):
        return self._data["date"]

    def deleteSelfCallback(self):
        self._parent.ItemManager.deleteItemFromDataBase(self._data["id"])
        self._parent.removeClipWidgetItem(self._item)
        self.deleteLater()