def filter_no_dialog(text):
	in_dialog = False
	textlist = list(text)
	retval = list()
	
	for char in textlist:
		if char == '"':
			in_dialog = not in_dialog
		else:
			if not in_dialog:
				retval.append(char)
	return ''.join(retval)


def remove_between_char(text, char1, char2):
	in_char = False
	retval = []
	
	for t in text:
		if t == char1:
			in_char = True
		elif t == char2:
			in_char = False
		elif not in_char:
			retval.append(t)
	return ''.join(retval)
			


def filter_spaces(text):
	retval = list()
	for i in range(len(text)):
		if text[i] == '\n':
			if not i == (len(text) - 1) and not text[i+1] == '\n':
				retval.append(' ')
		else:
			retval.append(text[i])
	return ''.join(retval)
				
			
	
