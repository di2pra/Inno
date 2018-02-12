from xml.dom import minidom
from models.domObject import domObject

class plurals(domObject):

	def __init__(self, xml):
		self.xml = xml
		self.tagName = self.__class__.__name__


	def generateLines(self):
		value = []

		dom = self.xml.getElementsByTagName(self.tagName) # get the list of items give the tag name

		for domItem in dom:
			childs = domItem.getElementsByTagName('item')
			parentName = domItem.attributes['name'].value.encode('utf-8')

			for child in childs:
				value.append(parentName + '.' + child.attributes['quantity'].value.encode('utf-8') + ' = ' + self.formatXmlCharacter(child.firstChild.data.encode('utf-8')) + '\n')

		return value
