#Deze bron is bedoeld voo rhet besturen van dbpedia

from SPARQLWrapper import SPARQLWrapper, JSON
import http.client


def print_request_info(path, result):
	print('sent request to:', path)
	print('result:', result.status, ',', result.reason)

def dict_to_paramstr(diction):
	retval = ''
	vals = diction.items()
	maxi = len(vals) - 1
	i = 0
	
	for key, value in vals:
		if not i == maxi:
			retval += str(key) + '=' + str(value) + '&'
		else:
			retval += str(key) + '=' + str(value)
		i = i + 1
	return retval

class LibraryThing:
	def __init__(self, devkey, debugmode = False):
		self.conn = http.client.HTTPConnection("librarything.com", 80)
		self.devkey = devkey
		self.debugmode = debugmode
		
	def get_work(self, id = None, isbn = None, iccn = None, oclc = None, name = None):
		params = dict()
		
		if not id is None:
			params['id'] = id
		if not isbn is None:
			params['isbn'] = isbn
		if not iccn is None:
			params['iccn'] = iccn
		if not oclc is None:
			params['oclc'] = oclc
		if not name is None:
			params['name'] = name
		params['method'] = 'librarything.ck.getwork'
		params['key'] = self.devkey
		
		
	
		paramstr = dict_to_paramstr(params)
		fullpath = '/services/rest/1.1/?' + paramstr
		
		self.conn.request('GET', fullpath)
		retval = self.conn.getresponse()
		
		if self.debugmode:
			print_request_info(fullpath, retval)
		
		data = str(retval.read()) # Typecast bytstring to regular string
		if self.debugmode:
			print(data)
		
		

class DBPedia:
	def __init__(self):
		pass
	
	def get_related_genres(self, genre):
		pass
	
	def get_country(self, book):
		pass
