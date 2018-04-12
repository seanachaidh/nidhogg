from nfile import NidhoggFile

class Book:
	def __init__(self, title, author, publisher, genre, keywords, filename):
		self.title = title
		self.author = author
		self.publisher = publisher
		self.genre = genre
		self.keywords = keywords
		self.nfile = NidhoggFile(filename)
		
