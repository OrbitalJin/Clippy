from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from components.clipWidget import ClipWidget

from tinydb import TinyDB, Query
from datetime import datetime
from pprint import pprint
from uuid import uuid4

class ItemManager:
	"""Manages the items"""
	def __init__(self, dataBase, parent):
		super(ItemManager, self).__init__()
		self._dataBase = TinyDB(dataBase)
		self._parent = parent

	def newItem(self, clip: str):
		if clip == " " or clip == "\n": return
		now = datetime.now()
		clipData = {
			"id": str(uuid4()),
			"type": "text",
			"content": clip,
			"date": now.strftime("%d/%m/%Y, %H:%M:%S"),
		}
		self.appendItem(data)
		self._dataBase.insert(data)

	def appendItem(self, data: dict):
		item = QListWidgetItem()
		item.setSizeHint(QSize(15, 28))
		widget = ClipWidget(data, item, self._parent)
		self._parent.ui.clipsListWidget.insertItem(0, item)
		self._parent.ui.clipsListWidget.setItemWidget(item, widget)

	def populateList(self):
		for itemData in self._dataBase:
			self.appendItem(itemData)

	def deleteItemFromDataBase(self, ID: str):
		itemQuery = Query()
		self._dataBase.remove(itemQuery.id == ID)

	def purgeDataBase(self): pass
	def saveDataBase(self):  pass
		