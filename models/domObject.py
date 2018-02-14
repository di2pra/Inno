from xml.dom import minidom

class domObject(object):
	"""Main Dom Object Mapper"""

	
	""" Static parameters """
	childObjects = None # define if the current object as child dom object by default None
	propertyName = None # define the property name of the dom object to get the property value, by default None

	def __init__(self, xml):
		""" dom object class initiator
		=====================
		@param: xml(Node Element): XML node element
		@return: null
		====================="""
		self.xml = xml
		self.tagName = self.__class__.__name__






	def generateValues(self, prepend = None):
		""" generate the dom element property file line
		=====================
		@param: prepend(string): optional string to prepend the property name
		@return: [(name, value)] : return an array of tuplet composed by (name, value)
		====================="""

		value = []

		dom = self.xml.getElementsByTagName(self.tagName) # get the list of items give the tag name

		for domItem in dom: # for each dom item

			if self.childObjects == None: # if the childObject is null then generate directly the string

				prependStr = '' if (prepend == None) else (str(prepend) + '.')
				value.append((str(prependStr) + domItem.attributes[self.propertyName].value.encode('utf-8'), domItem.firstChild.data.encode('utf-8')))

			else: # otherwise generate recursivly with the child domObject and prepend the parent property value

				parentName = None if (self.propertyName == None) else domItem.attributes[self.propertyName].value.encode('utf-8')

				if parentName == None: # if parentName is None then prependStr is equel to prepend value

					prependStr = None if (prepend == None) else prepend

				else: # else append the parentName to the prepend Value

					prependStr = parentName if (prepend == None) else (str(prepend) + '.' + parentName)

				for childObject in self.childObjects:
					value.extend(childObject(domItem).generateValues(prependStr)) # recursively call the method to process sub nodes
			
		return value