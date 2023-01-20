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
		self.appendItem(clipData)
		self._dataBase.insert(clipData)

	def appendItem(self, data: dict):
		item = QListWidgetItem()
		item.setSizeHint(QSize(15, 28))
		widget = ClipWidget(data, item, self._parent)
		self._parent.ui.clipsListWidget.insertItem(0, item)
		self._parent.ui.clipsListWidget.setItemWidget(item, widget)

	def populateList(self):
		for itemData in self._dataBase:
			self.appendItem(itemData)

	def getItemContent(self, item: QListWidgetItem):
		widget = self._parent.ui.clipsListWidget.itemWidget(item)
		content = widget.getClipContent()
		return content

	def getVisibleItems(self):
		items = []
		for i in range(self._parent.ui.clipsListWidget.count()):
			item = self._parent.ui.clipsListWidget.item(i)
			if not item.isHidden():
				items.append(item)
		return items

	def gotToFirstVisibleItem(self):
		self._parent.ui.clipsListWidget.setFocus()
		items = self.getVisibleItems()
		if not items: return
		self._parent.ui.clipsListWidget.setCurrentItem(items[0])

	def gotToNextVisibleItem(self):
		self._parent.ui.clipsListWidget.setFocus()
		items = self.getVisibleItems()
		currentItem = self._parent.ui.clipsListWidget.currentItem()
		if currentItem: index = (items.index(currentItem) + 1) % len(items)
		else: self.ItemManager.gotToFirstVisibleItem(); return
		self._parent.ui.clipsListWidget.setCurrentItem(items[index])

	def gotToPrevVisibleItem(self):
		self._parent.ui.clipsListWidget.setFocus()
		items = self.getVisibleItems()
		currentItem = self._parent.ui.clipsListWidget.currentItem()
		if currentItem: index = (items.index(currentItem) - 1) % len(items)
		else: self.ItemManager.gotToFirstVisibleItem(); return
		self._parent.ui.clipsListWidget.setCurrentItem(items[index])

	def deleteItemFromDataBase(self, ID: str):
		itemQuery = Query()
		self._dataBase.remove(itemQuery.id == ID)

	def purgeDataBase(self): pass
		