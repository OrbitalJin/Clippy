


# def method(lst: list) -> dict:
# 	l = []
# 	for entry in lst:
# 		hotkey = ""
# 		entry = entry.lower()
# 		for key in entry.split("+"):
# 			hotkey += key if len(key) == 1 else f"<{key}>+" 
# 		l.append(hotkey)

# 	return {
# 		entry:lambda: print(entry[-1]) for entry in l
# 	}
# test = ["Ctrl+ALT+I", "Ctrl+ALT+H"]

def method(lst: list) -> dict:
	lst = ["Ctrl+ALT+I", "Ctrl+ALT+H"]
	combinations = [combination.lower() for combination in lst]
	combinations = ["+".join([key if not len(key)-1 else f"<{key}>" for key in combination.split("+")]) for combination in combinations]
	return{
		combination: (lambda: print(combination[-1])) for combination in combinations
	}

combinations = ["Ctrl+ALT+I", "Ctrl+ALT+H"]
print(method(combinations))

