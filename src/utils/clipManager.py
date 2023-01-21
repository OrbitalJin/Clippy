from PySide2.QtCore import QObject, QThread, Signal
from PySide2.QtGui import QPixmap, QImage
import pyperclip as clip

class ClipManager(QObject):
	processedClip = Signal(dict)
	def __init__(self, clipboard, caller):
		QObject.__init__(self)
		self.Clipboard = clipboard
		self._caller = caller
		self.connectSignalsAndSlots()

	def connectSignalsAndSlots(self):
		self.Clipboard.dataChanged.connect(self.processClip)

	def processClip(self):
		if self.Clipboard.text():      self.processText()
		elif self.Clipboard.pixmap():  self.processPixmap() 
		elif self.Clipboard.image():   self.processImage()
		else: return self.raiseUnsupportedFormatException()
		return None

	def processText(self):
		text = self.Clipboard.text()
		if text == " " or text == "\n": return 
		data = {
			"type": "text",
			"content": text
		}
		self.log("Copied Text")
		self.processedClip.emit(data)

	def processPixmap(self):
		pixmap = self.Clipboard.pixmap()
		data = {
			"type": "pixmap",
			"content": pixmap
		}
		self.log("Copied Pixmap")
		# self.processedClip.emit(data)

	def processImage(self):
		image = self.Clipboard.image()
		data = {
			"type": "image",
			"content": image
		}
		self.log("Copied Image")
		# self.processedClip.emit(data)

	def pasteContentFromData(self, data: dict):
 		if data["type"] == "text":   self.pasteText(data["content"])
 		if data["type"] == "pixmap": self.pastePixmap(data["content"])
 		if data["type"] == "image":  self.pasteImage(data["content"])

	def pasteText(self, text: str):
 		self.Clipboard.setText(text)

	def pastePixmap(self, pixmap: QPixmap):
		self.Clipboard.setPixmap(pixmap)
	
	def pasteImage(self, Image: QImage):
		self.Clipboard.setImage(image)

	def log(self, msg: str):
		print(f"[{self.__class__}] {msg}")
	
	def raiseUnsupportedFormatException(self): pass