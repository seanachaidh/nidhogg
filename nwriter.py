import xml.etree.ElementTree as ET
from copy import deepcopy

class NidhoggWriter:
	def __init__(self, filename, filetype, elements):
		self.filename = filename
		self.elements = elements
		self.filetype = filetype
	
	def _create_tree(self):
		tree = ET.Element('nidhoggfile', attrib={'type': self.filetype})
		for e in self.elements:
			attrib = deepcopy(e)
			
			attrib.pop('tag')
			attrib.pop('text')
			
			elem = ET.SubElement(tree, e['tag'], attrib)
			elem.text = e['text']
		return tree
	
	def serialize(self):
		t = self._create_tree()
		towrite = ET.ElementTree(t)
		towrite.write(self.filename, encoding='utf-8')
	
	def __repr__(self):
		retval = 'file to be written to: ' + self.filename + '\n'
		for x in range(len(self.elements)):
			current = self.elements[x]
			retval += 'Element ' + str(x) + '\n'
			for key, value in x.items():
				retval += '\tAttribute: ' + key + '; Value: ' + str(value) + '\n'
		return retval
