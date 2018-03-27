#!/usr/bin/env/python3

import os

class Application:
	
	
	def __init__(self, parameters):
		
		self.parameters = paramters
		self.books = list()

	def parse_parameters(self):
		for i in range(len(parameters)):
			current = self.parameters[i]
			
			if current == "--bookdir":
				self.bookdir = self.paramters[i+1]
				i++
			if current == '--algtype':
				self.algtype = self.parameters[i+1]
				i++
	
	def load_all_books(self):
		print('loading books from directory:' self.bookdir)
		allfiles = os.listdir(self.bookdir)
		
		for f in allfiles:
			fullfilename = os.path.join(self.bookdir, f)
			print('Loading book located in file:', fullfilename)
			
			nfile = Book(
			
			self.books
	
	def print_parameters(self):
		print('algtype:', self.algtype)
		print('bookdir:', self.bookdir)

def main():
    pass


if __name__== '__init__':
    main()
