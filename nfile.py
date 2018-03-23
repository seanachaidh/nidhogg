import re, nltk
from bz2 import BZ2File

class NidhoggFile:
	def __init__(self, filename, fileinfo = ''):
		
		self.fileinfo = fileinfo
		self.filename = filename
		
		#First we read the file
		with BZ2File(filename, 'r') as myfile:
			tmpdat = myfile.read().decode('utf-8')
			tmpdat = tmpdat.replace('\r\n', '\n')
			#~ self.data = re.sub('[“”]', '"', tmpdat)
			self.data = tmpdat
			print(self.data)
			
		#Then we create the tokens
		self.tokens = nltk.word_tokenize(self.data)
		self.stripped_tokens = only_word(self.tokens)
		
		self.postag = nltk.pos_tag(self.stripped_tokens)
