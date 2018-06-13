from nfile import NidhoggFile
from bz2 import BZ2File

class Book:
    
    def _load_file(self):
        with BZ2File(filename, 'r') as myfile:
            tmpdat = myfile.read().decode('utf-8')
            tmpdat = tmpdat.replace('\r\n', '\n')
            #~ self.data = re.sub('[“”]', '"', tmpdat)
            self.data = tmpdat
#            print(self.data)        
    
	def __init__(self, title, author, publisher, genre, keywords, filename):
		self.title = title
		self.author = author
		self.publisher = publisher
		self.genre = genre
		self.keywords = keywords
		self.nfile = filename
        
        self._load_file()
        