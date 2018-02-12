class Perspective:
	
	def _dialog_filter(self, tokens):
		indial = False
		retval = []
		for tag in myfile.postag:
			if tag[1] == "''":
				indial = not indial
			elif not indial:
				retval.append(tag)
		return retval
	
	def _split_zinnen(tokens):
		zinnen = []
		current = []
		for tok in tokens:
			if tok[1] == '.': # Als we op het einde van een zin zitten
				zinnen.append(current)
				current = []
			else:
				current.append(tok)
	
	def _calculate_zinnen(self, zinnen):
		
		for z in zinnen:
			toparse = list.reverse([x for x in z]) # Kan ik dit ook doen zonder de lijst om te draaien?
			stack = list()
			
			for t in z:
				if not stack:
					
				
	
	def __init__(self, myfile):
		pass
		
	def get_socre(self):
		#Verkrijgt de score dewelke de kans is dat het verhaal in de eerste persoon is.
		eerste, tweede = 0
		zinnen = []
		
		#Hoeveel van de zinnen zijn in de eerste persoon
		# first we split it into scentences. Assuming that those end in a .
		
		
#End of class
