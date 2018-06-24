import os
from xml.etree import ElementTree as ET
from zipfile import ZipFile

from operator import attrgetter

class structTOC:
    def __init__(self, id, text, content, order):
        self.id = id
        self.text = text
        self.order = order
        self.content = content


class MetaData:
    def __init__(self, filename):
        pass

class TOC:
    def __init__(self, filename):
        elements = []

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
            elements.append(line)

            # Is hier het sorteren wel nodig?
            self.elements = sorted(elements, key = attrgetter('order'))


class EPUB:
    def __init__(self, author, title, chapters):
        pass
    
    @staticmethod
    def load_from_file(filename):
        foldername = filename.split('.')[0] + '_tmp'
        
        os.mkdir(foldername)
        zipf = ZipFile(filename)
        zipf.extractall(foldername)

        metainf = ET.parse(os.path.join(foldername, 'META-INF', 'container.xml')).getroot()
        locfolder =  metainf.find('.//rootfile').attrib.get('full-path')

        toc = TOC(os.path.join(foldername, locfolder, 'toc.ncx'))




