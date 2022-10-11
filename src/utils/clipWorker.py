from PySide2.QtCore import QThread, Signal
import pyperclip as clip

class ClipListener(QThread):
	newClipSignalEvent = Signal(str)
	unavailableClipEvent = Signal(bool)
	def __init__(self):
		QThread.__init__(self)
		self.__ThreadActive = True
		print(f"ClipListener is_available: {self.__ThreadActive}")

	def run(self):
		while self.__ThreadActive:
			try:
				if self.__ThreadActive:
					clip.waitForNewPaste(timeout=1) 			# Timeout is set to 1 because this was preventing the QThread from safely quitting
					self.newClipSignalEvent.emit(clip.paste())
				else: break
			except: pass										# Passing here because the waitForNewPaste will raise a tiemout expection
				
	@property
	def isThreadActive(self):
		return self.___isThreadActive

	def stop(self):
		self.__ThreadActive = False
		self.quit()
