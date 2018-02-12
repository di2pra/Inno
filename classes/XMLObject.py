class XMLObject(object):

	def __init__(self, tagName = None, attribute = None, value = None):
		self.tagName = tagName
		self.attribute = attribute
		self.value = value

	def generateOutputFromXML(self, xml):

		node = xml.getElementsByTagName(self.tagName)[0]

		self.propertyName = node.attributes[self.attribute].value

		if self.value == None:

			self.propertyValue = node.firstChild.nodeValue
			print(self.propertyValue)

			return 

		else:

			self.value.generateOutputFromXML(node)

		print(self.propertyName)
		print(self.propertyValue)


				#self.value.generateOutputFromXML(node.firstChild.data)
