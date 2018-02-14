class LanguageXMLConverter:
	"""A Simple Language Converter class: give an array of xml language files path, it will generate a single language property file"""

	""" Static parameters """
	regexPattern = '([%][0-9]+[$]\w)|(%d)' # regex pattern to replace property value in the output file

	def __init__(self, schema, inputFilesPath = None):
		""" LanguageXMLConvert Class Initiator
		=====================
		@param:
			schema: required XML schema object (domObject)
			inputFiles([string]): optional array of string of input XML file paths
		@return: nothing
		====================="""
		self.schema = schema
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
		from models.string import string
		from models.plurals import plurals
		from xml.dom import minidom #import python minimal dom implementation

		try:

			outputFile = open(outputFilePath,'w') #generate empty output text file
		
			for inputFile in self.inputFiles: # iterate for each input file paths

				xmldoc = minidom.parse(inputFile) #parse the XML input file given the path

				values = self.schema(xmldoc).generateValues()

				for value in values:
					outputFile.write(LanguageXMLConverter.lineString(value[0], value[1]))
			
			outputFile.close() # close the generated file

			print("File `" + str(outputFilePath) + "` succesfully generated")
			
		except IOError as e: #catch file error
			print "Unable to generate the output file. Error info: I/O error({0}) - {1}".format(e.errno, e.strerror)
		except UnicodeDecodeError as e: #catch encoding error
			print "Unable to generate the output file. Error info: UnicodeDecodeError - {0}".format(e)
		except Exception as e:
			print "Unable to generate the output file. Error info: Undefined error - {0}".format(e)





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
			matches = re.findall(LanguageXMLConverter.regexPattern, value) # find all matches of the regex within the input string		

			index=0 # init the position to 0

			for match in matches: #iterate for matches of the input string
				for subMatch in match:
					if subMatch is not '':
						output = output.replace(subMatch, '{'+str(index)+'}')
						index += 1
				

			return output # return the converted value
			
		except Exception, e: #if we catch an exception during the formating method, return the initial string value

			return value





	@staticmethod
	def lineString(property, value):
		""" generate the property file line string given the property and value
		=====================
		@param:
			- property(string): string of the property name
			- value(string): string of the property value
		@return: (string) : return string format : `property = value`
		====================="""

		return property + ' = ' + LanguageXMLConverter.formatXmlCharacter(value) + '\n'



	@staticmethod
	def getFileNameFromPath(path):
		""" given the file path, this method will return the file name without the extension
		=====================
		@param:
			- path(string): full path of the file
		@return: (string) : filename
		====================="""
		import ntpath #file path module

		return ntpath.basename(path).split('.')[0] # getting the filename without the extension from the fullpath





