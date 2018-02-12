from xml.dom import minidom

class domObject(object):

	regexPattern = '([%][0-9]+[$]\w)'


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