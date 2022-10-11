from PySide2.QtCore import QThread, Signal
from functools import partial
from pynput import keyboard

# Replaced lambda by partial bc whereas lambda requires a var, partial binds a parameter upfront https://stackoverflow.com/questions/72956217/how-to-pass-arguments-to-functions-called-by-hot-keys-in-pynput
class HotKeyWorker(QThread):
	combinationDetected = Signal(str)
	def __init__(self, HotKeys: list):
		QThread.__init__(self)
		self.__isThreadActive = True
		self.HotKeys = HotKeys

	def run(self):
		if self.__isThreadActive:
			self.Bindings, self.Logs = self.generateBindingsMap(self.HotKeys)
			self.KeyListener = keyboard.GlobalHotKeys(self.Bindings)
			self.KeyListener.start()

	def generateBindingsMap(self, lst: list) -> dict:
	    combinations = [combination.lower() for combination in lst]
	    combinations = ["+".join([key if not len(key)-1 else f"<{key}>" for key in combination.split("+")]) for combination in combinations]
	    return{
	        hotkey: partial(self.combinationDetected.emit, hotkey[-1]) for hotkey in combinations # <--
	    }, ((hotkey, hotkey[-1]) for hotkey in combinations)
   	
	@property
	def isThreadActive(self):
		return self.___isThreadActive

	def stop(self):
		self.__isThreadActive = False
		self.KeyListener.stop()
		self.quit()