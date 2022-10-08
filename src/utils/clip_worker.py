from PySide2.QtCore import QThread, Signal
import pyperclip as clip
import time


class ClipListener(QThread):
	newClipSignalEvent = Signal(str)
	unavailableClipEvent = Signal(bool)
	def __init__(self):
		QThread.__init__(self)
		self.ThreadActive = True
		print(f"ClipListener is_available: {self.ThreadActive}")

	def run(self):
		while True:
			if not self.ThreadActive: break
			clip.waitForNewPaste(timeout=None)
			self.newClipSignalEvent.emit(clip.paste())

	def stop(self):
		self.ThreadActive = False
		self.terminate()






# clip.copy('The text to be copied to the clipboard.')
# spam = clip.paste()
# print(spam)
# # if not clip.is_available():
# # 	print("Copy functionality unavailable!")

# while True:
# 	clip.waitForNewPaste(timeout=None)
# 	print(clip.paste())
