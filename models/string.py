from xml.dom import minidom
from models.domObject import domObject

class string(domObject):

	def __init__(self, xml):
		self.xml = xml
		self.tagName = self.__class__.__name__


	def generateLines(self):
		value = []

		dom = self.xml.getElementsByTagName(self.tagName) # get the list of items give the tag name

		for domItem in dom:
			value.append(domItem.attributes['name'].value.encode('utf-8') + ' = ' + string.formatXmlCharacter(domItem.firstChild.data.encode('utf-8')) + '\n')

		return value