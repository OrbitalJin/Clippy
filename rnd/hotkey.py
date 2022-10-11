from pynput import keyboard
from functools import partial

print("test")
def method(lst: list) -> dict:
    combinations = [combination.lower() for combination in lst]
    combinations = ["+".join([key if not len(key)-1 else f"<{key}>" for key in combination.split("+")]) for combination in combinations]
    return{
        hotkey: partial(print, hotkey[-1]) for hotkey in combinations # Replaced lambda by partial bc whereas lambda requires a var, partial binds a parameter upfront https://stackoverflow.com/questions/72956217/how-to-pass-arguments-to-functions-called-by-hot-keys-in-pynput
    }, ((hotkey, hotkey[-1]) for hotkey in combinations)

combinations = ["Ctrl+ALT+A", "Ctrl+ALT+B"]


binds, strs = method(combinations)

print(list(strs))
with keyboard.GlobalHotKeys(binds) as h:
    h.join()


