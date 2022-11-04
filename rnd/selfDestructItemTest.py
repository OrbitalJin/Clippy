from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Window(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.listWidget = QListWidget(self)
        self.layout.addWidget(self.listWidget)
        self.addListItems()

    def addListItems(self):           # creates the item widgets
        for i in range(5):
            item = QListWidgetItem(type=0)
            widget = ListItem(f"button {i}", self, item)
            self.listWidget.addItem(item)
            self.listWidget.setItemWidget(item, widget)

    def removeWidgetItem(self, item):  # removes the item widgets
        index = self.listWidget.indexFromItem(item).row()
        item = self.listWidget.takeItem(index)

class ListItem(QPushButton):

    def __init__(self, text, parent, item):
        super().__init__(text, parent)
        self.item = item                     # the ListWidgetItem
        self._parent = parent                # the Window
        self.clicked.connect(self.deleteSelf)

    def deleteSelf(self):                    # slot for button click
        self._parent.removeWidgetItem(self.item)
        self.deleteLater()

app = QApplication([])
window = Window()
window.show()
app.exec()