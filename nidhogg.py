#!/usr/bin/env/python3

import os, json

class Key:
	def __init__(self, name, type, key):
		self.name = name
		self.type = type
		self.key = key


#is deze klasse wel nodig?
class ConfigFile:
	
	def search_key(self, keyname):
		for k in self.keys:
			if k['keyname'] == keyname:
				return k
		return None
		
	
	def __init__(self, filename):
		with open(filename, 'r') as f:
			self.conf = json.load(f)
		
		self.profile_name = self.conf['profile_name']
		self.keys = self.conf['keys']
		
class Application:
	
	def __init__(self, parameters):
		
		self.parameters = paramters
		self.books = list()

	def parse_parameters(self):
		for i in range(len(parameters)):
			current = self.parameters[i]
			
			if current == "--bookdir":
				self.bookdir = self.paramters[i+1]
				i = i + 1
			if current == '--algtype':
				self.algtype = self.parameters[i+1]
				i = i + 1
			if current == '--configfile':
				self.configfile = self.parameters[i+1]
				i = i + 1
			
	
	def load_all_books(self):
		print('loading books from directory:', self.bookdir)
		allfiles = os.listdir(self.bookdir)
		
		for f in allfiles:
			fullfilename = os.path.join(self.bookdir, f)
			print('Loading book located in file:', fullfilename)
			
			#~ nfile = Book(
			
			#~ self.books
	
	def print_parameters(self):
		print('algtype:', self.algtype)
		print('bookdir:', self.bookdir)

def main():
    pass


if __name__== '__init__':
    main()
