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
	def __init__(self, dataBase, caller):
		super(ItemManager, self).__init__()
		self._dataBase = TinyDB(dataBase)
		self._caller = caller

	def newItem(self, clip: dict):
		if self.itemOnTop(clip["content"]): return
		now = datetime.now()
		clipData = {
			"id": str(uuid4()),
			"type": clip["type"],
			"content": clip["content"],
			"date": now.strftime("%d/%m/%Y, %H:%M:%S")
		}
		self.appendItem(clipData)
		self._dataBase.insert(clipData)

	def appendItem(self, data: dict):
		item = QListWidgetItem()
		item.setSizeHint(QSize(15, 28))
		widget = ClipWidget(data, item, self._caller)
		self._caller.ui.clipsListWidget.insertItem(0, item)
		self._caller.ui.clipsListWidget.setItemWidget(item, widget)
		self._caller.filterClipboard(self._caller.ui.searchBar.text())

	def populateList(self):
		for itemData in self._dataBase:
			self.appendItem(itemData)

	def gotToFirstVisibleItem(self):
		self._caller.ui.clipsListWidget.setFocus()
		items = self.getVisibleItems()
		if not items: return
		self._caller.ui.clipsListWidget.setCurrentItem(items[0])

	def gotToNextVisibleItem(self):
		if self._caller.ui.clipsListWidget.currentRow() == -1 or not self.visibleItemSelected():
			self.gotToFirstVisibleItem(); return

		self._caller.ui.clipsListWidget.setFocus()
		items = self.getVisibleItems()
		currentItem = self._caller.ui.clipsListWidget.currentItem()
		if currentItem: index = (items.index(currentItem) + 1) % len(items)
		else: self.ItemManager.gotToFirstVisibleItem(); return
		self._caller.ui.clipsListWidget.setCurrentItem(items[index])

	def gotToPrevVisibleItem(self):
		if not self.visibleItemSelected(): self.gotToFirstVisibleItem()
		self._caller.ui.clipsListWidget.setFocus()
		items = self.getVisibleItems()
		currentItem = self._caller.ui.clipsListWidget.currentItem()
		if currentItem: index = (items.index(currentItem) - 1) % len(items)
		else: self.ItemManager.gotToFirstVisibleItem(); return
		self._caller.ui.clipsListWidget.setCurrentItem(items[index])

	def getItemContent(self, item: QListWidgetItem):
		widget = self._caller.ui.clipsListWidget.itemWidget(item)
		content = widget.getClipContent()
		return content

	def getItemData(self, item: QListWidgetItem):
		widget = self._caller.ui.clipsListWidget.itemWidget(item)
		data = widget.getClipData()
		return data

	def getVisibleItems(self):
		items = []
		for i in range(self._caller.ui.clipsListWidget.count()):
			item = self._caller.ui.clipsListWidget.item(i)
			if not item.isHidden():
				items.append(item)
		return items

	def itemOnTop(self, content):
		topItem = self._caller.ui.clipsListWidget.item(0)
		topItemContent = self.getItemContent(topItem)
		return content == topItemContent

	def visibleItemSelected(self):
		return any([item.isSelected() for item in self.getVisibleItems()])

	def deleteItemFromDataBase(self, ID: str):
		itemQuery = Query()
		self._dataBase.remove(itemQuery.id == ID)

	def purgeDataBase(self): pass
		