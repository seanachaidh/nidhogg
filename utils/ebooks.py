import os
from xml.etree import ElementTree as ET
from zipfile import ZipFile


class structTOC:
    def __init__(self, id, text, content, order):
        self.id = id
        self.text = text
        self.order = order
        self.content = content

class TOC:
    def __init__(self, filename):
        self.elements = []

        tree = ET.parse(filename)
        root = tree.getroot()

        navpoints = root.findall('.//NavPoint') # Ik kan dit beter neerschrijven
        
        for point in navpoints:
            # Hier zou eigenlijk geen enkele waarde none mogen zijn

            id = point.attrib.get('id', 'None')
            order = point.attrib.get('playOrder', 0)
            text = point.find('./text').text
            content = point.find('./content').attrib.get('src', 'None')

            line = structTOC(id, text, content, order)
            self.elements.append(line)

class EPUB:
    def __init__(self, author, title):
        pass
    
    @staticmethod
    def load_from_file(filename):
        foldername = filename.split('.')[0] + '_tmp'
        
        os.mkdir(foldername)
        zipf = ZipFile(filename)
        zipf.extractall(foldername)


    
