import nltk
from bz2 import BZ2File

def only_word(tokens):
	#Nog eens nakijken of ik moet specifiëren of het start of endigt met een onderliggend streepje
    no_underscore = [x.strip('_') for x in tokens]
    no_empty_words = [item for item in no_underscore if not len(item) == 0]
    
    return no_empty_words

def filter_dialog(tokens):
	#Assuming dialog is with double quotes
	pass
	

def check_tokens(tokens):
	for t in tokens:
		if len(t) == 0:
			raise RuntimeError("Something went wrong with the tokens")

class NidhoggFile:
	def __init__(self, filename):
		#First we read the file
		with BZ2File(filename, 'r') as myfile:
			self.data = myfile.read().decode('utf-8')
			print(self.data)
			
		#Then we create the tokens
		self.tokens = nltk.word_tokenize(self.data)
		self.stripped_tokens = only_word(self.tokens)
		
		check_tokens(self.stripped_tokens)
		
		self.postag = nltk.pos_tag(self.stripped_tokens)
