class LanguageXMLConverter:
	"""A Simple Language Converter class: give an array of xml language files path, it will generate a single language property file"""

	""" Static parameters """
	xmlFileTagName = 'string' # XML file item tag name
	xmlTagAttributeName = 'name' # XML file item tag name
	regexPattern = '([%][0-9]+[$]\w)' # regex pattern to PHP printf directives 



	def __init__(self, inputFilesPath = None):
		""" LanguageXMLConvert Class Initiator
		=====================
		@param: inputFiles([string]): optional array of string of input XML file paths
		@return: nothing
		====================="""
		self.inputFiles = [] if inputFilesPath is None else inputFilesPath # if the inputFilesPath is not defined, then set the array of file paths as empty





	def addInputXMLFile(self, inputFilePath):
		""" Append a new XML file path to the existing filepath array
		=====================
		@param: inputFilePath(string): string of input XML file path to append
		@return: nothing
		====================="""
		self.inputFiles.append(inputFilePath) # append the given file path to the existing array of input file paths






	def generateOutputFile(self, outputFilePath):
		""" given the output file path, this method will generate the property language text file
		=====================
		@param: outputFilePath(string): string of input XML file path to append
		@return: nothing
		====================="""
		from xml.dom import minidom #import python minimal dom implementation

		try:

			outputFile = open(outputFilePath,'w') #generate empty output text file
		

			for inputFile in self.inputFiles: # iterate for each input file paths

				xmldoc = minidom.parse(inputFile) #parse the XML input file given the path
				itemlist = xmldoc.getElementsByTagName(LanguageXMLConverter.xmlFileTagName) # get the list of items give the tag name

				for item in itemlist: # iterate for each items in the XML file

					#write for each lines the property name with the property value
					outputFile.write(item.attributes[LanguageXMLConverter.xmlTagAttributeName].value.encode('utf-8') + ' = ' + LanguageXMLConverter.formatXmlCharacter(item.firstChild.data.encode('utf-8')) + '\n')
		
			outputFile.close() # close the generated file

			print("File `" + str(outputFilePath) + "` succesfully generated")
			
		except IOError as e: #catch file error
			print "Unable to generate the output file. Error info: I/O error({0}) - {1}".format(e.errno, e.strerror)
		except UnicodeDecodeError as e: #catch encoding error
			print "Unable to generate the output file. Error info: UnicodeDecodeError - {0}".format(e)
		return 0




	@staticmethod
	def formatXmlCharacter(value):
		""" given the input string, this STATIC method will convert the string according to the regex, the position of the match and replace by `{position}` and return the converted string.
		=====================
		@param: value(string): string to convert
		@return: string : converted string
		====================="""

		import re

		output = value
		matchs = re.findall(LanguageXMLConverter.regexPattern, value) # find all matches of the regex within the input string
		

		index=0 # init the position to 0

		for match in matchs: #iterate for matches of the input string
			output = output.replace(match, '{'+str(index)+'}') # replace the current match with `{position}`
			index += 1 # increase the position by 1

		return output # return the converted value
