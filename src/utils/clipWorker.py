from PySide2.QtCore import QThread, Signal
import pyperclip as clip
import time


class ClipListener(QThread):
	newClipSignalEvent = Signal(str)
	unavailableClipEvent = Signal(bool)
	def __init__(self):
		QThread.__init__(self)
		self.__ThreadActive = True
		self.isPaused = False
		print(f"ClipListener is_available: {self.__ThreadActive}")

	def run(self):
		while True:
			if self.__ThreadActive:
				clip.waitForNewPaste(timeout=None)
				if not self.isPaused: self.newClipSignalEvent.emit(clip.paste())
			else: break

	def setPaused(self, switch: bool):
		self.isPaused = switch

	@property
	def isThreadActive(self):
		return self.___isThreadActive

	def stop(self):
		self.__ThreadActive = False
		self.terminate()
