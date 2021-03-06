import unittest, nwriter, nfile, perspective, nfilters, dbpedia, nidhogg

class TestFileWriter(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		testelem = list()
		testelem.append(dict(tag='zin', text='ik ben pieter', soort='bericht'))
		testelem.append(dict(tag='zin', text='Ik ben enorm cool', soort='de waarheid'))
		cls._mytree = nwriter.NidhoggWriter('test.xml', 'testzinnen', testelem)
		
	def test_serialization(self):
		self._mytree.serialize()
		

class TestPerspective(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls._testfile = nfile.NidhoggFile('corpus/alice_in_wonderland.txt.bz2')
		cls._scanner = perspective.Perspective(cls._testfile)
		cls._template = nwriter.NidhoggLoader('perspectivetest.xml')
		
	def test_perspective(self):
		self._scanner.get_score()

	def test_transformation(self):
		self._template.transform('transform/perspective.xslt')
		
		
class TestFilters(unittest.TestCase):
	
	def test_spacefilter(self):
		zin = 'Hello\n\ncruel\nworld'
		newzin = nfilters.filter_spaces(zin)
		self.assertEqual(newzin, 'Hello cruel world')


class TestRequests(unittest.TestCase):
	
	def test_librarything(self):
		# for tests we use the default configuration file location
		conffile = nidhogg.ConfigFile('settings.json')
		librarykey = conffile.search_key('librarything')['key']
		
		api = dbpedia.LibraryThing(librarykey, True)
		
		api.get_work(name = "Harry Potter and the Philosopher's Stone")
		

if __name__ == '__main__':
	unittest.main()
	

