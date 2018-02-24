import nwriter, nfilters, nltk, re

class Perspective:
	
	def _dialog_filter(self, zinnen):
		retval = list()
		
		for z in zinnen:
			filtered = re.sub(r'(["\'])(?:(?=(\\?))\2.)*?\1', "", z)
			retval.append(filtered)
			
		return retval
	
	def _split_zinnen(self, text):
		zinnen = []
		
		tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
		zinnen = tokenizer.tokenize(text)
		
		return zinnen
				
					
	def _calculate_zinnen(self, zinnen):
		retval = []
		for z in zinnen:
			first = False
			
			tagged = nltk.pos_tag(nltk.word_tokenize(z))
			
			for t in z:
				if t[0] == 'I' or t[0].lower() == 'we' or t[0].lower() == 'my':
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
			fusetext = ''.join([x[0] for x in c[1]])
			elems.append(dict(soort = isi, text = fusetext, tag = 'zin'))
		
		filewriter = nwriter.NidhoggWriter('perspectivetest.xml', 'generesult', elems)
		#~ print(filewriter)
		filewriter.serialize()
	
	def __init__(self, myfile):
		self.myfile = myfile
		
	def get_score(self):
		
		nonew = nfilters.filter_spaces(self.myfile.data)
		
		diag = nfilters.filter_no_dialog(''.join(nonew))
		zinnen = self._split_zinnen(diag)
		czin = self._calculate_zinnen(zinnen)
		
		self._serialize_result(czin)
		
		
#End of class
