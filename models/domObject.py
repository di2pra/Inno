from xml.dom import minidom

class domObject(object):

	""" Static parameters """
	regexPattern = '([%][0-9]+[$]\w)' # regex pattern to replace in the output file

	def __init__(self, xml):
		""" dom object class initiator
		=====================
		@param: xml(Node Element): XML node element
		@return: null
		====================="""
		self.xml = xml
		self.tagName = self.__class__.__name__


	def generateLines(self, prepend = None):
		""" generate the dom element property file line
		=====================
		@param: prepend(string): optional string to prepend the property name
		@return: [string] : return array of property file lines string
		====================="""

		value = []

		dom = self.xml.getElementsByTagName(self.tagName) # get the list of items give the tag name

		for domItem in dom: # for each dom item

			if self.childObject == None: # if the childObject is null then generate directly the string

				if prepend == None:
					value.append(domItem.attributes[self.propertyName].value.encode('utf-8') + ' = ' + self.formatXmlCharacter(domItem.firstChild.data.encode('utf-8')) + '\n')
				else:
					value.append(str(prepend) + '.' + domItem.attributes[self.propertyName].value.encode('utf-8') + ' = ' + self.formatXmlCharacter(domItem.firstChild.data.encode('utf-8')) + '\n')

			else: # else generate recursivly with the child domObject and prepend the parent property value
				parentName = domItem.attributes[self.propertyName].value.encode('utf-8')
				value.extend(self.childObject(domItem).generateLines(parentName))
			
		return value


	@staticmethod
	def formatXmlCharacter(value):
		""" given the input string, this STATIC method will convert the string according to the regex, the position of the match and replace by `{position}` and return the converted string.
		=====================
		@param: value(string): string to convert
		@return: string : converted string
		====================="""

		import re

		try:

			output = value
			matchs = re.findall(domObject.regexPattern, value) # find all matches of the regex within the input string
			

			index=0 # init the position to 0

			for match in matchs: #iterate for matches of the input string
				output = output.replace(match, '{'+str(index)+'}') # replace the current match with `{position}`
				index += 1 # increase the position by 1

			return output # return the converted value
			
		except Exception, e: #if we catch an exception during the formating method, return the initial string value

			return value