import nwriter

class Perspective:
	
	def _dialog_filter(self):
		indial = False
		retval = []
		for tag in self.myfile.postag:
			if tag[1] == "''":
				indial = not indial
			elif not indial:
				retval.append(tag)
		return retval
	
	def _split_zinnen(self, tokens):
		zinnen = []
		current = []
		for tok in tokens:
			if tok[1] == '.': # Als we op het einde van een zin zitten
				zinnen.append(current)
				current = []
			else:
				current.append(tok)
		return zinnen
				
					
	def _calculate_zinnen(self, zinnen):
		retval = []
		
		for z in zinnen:
			first = False
			for t in z:
				if t[0] == 'I' or t[0].lower() == 'we':
					first = True
			retval.append((first, z)) #Geeft tuples terug
		return retval
			
	def _serialize_result(self, calczinnen):
		elems = list()
		
		for c in calczinnen:
			if c[0]:
				isi = 'ik'
			else:
				isi = 'hij'
			elems.append(dict(soort = isi, text = c[1], tag = 'zin'))
		
		filewriter = nwriter.NidhoggWriter('perspectivetest.xml', 'generesult', elems)
		filewriter.serialize()
	
	def __init__(self, myfile):
		self.myfile = myfile
		
	def get_score(self):
		# Eerst de dialogen
		diag = self._dialog_filter()
		zinnen = self._split_zinnen(diag)
		czin = self._calculate_zinnen(zinnen)
		
		self._serialize_result(czin)
		
		
#End of class
