import nltk
from bz2 import BZ2File

def only_word(tokens):
	#Nog eens nakijken of ik moet specifiëren of het start of endigt met een onderliggend streepje
    return [x.trim('_') for x in tokens]


class NidhoggFile:
	def __init__(self, filename):
		#First we read the file
		with BZ2File(filename, 'r') as myfile:
			self.data = myfile.read().decode('utf-8')
			print(self.data)
			
		#Then we create the tokens
		self.tokens = nltk.word_tokenize(self.data)
		self.striped_tokens = only_word(self.tokens)
		self.postag = nltk.pos_tag(self.stripped_tokens
		
