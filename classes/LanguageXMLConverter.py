class LanguageXMLConverter:
	"""A Simple Language Converter class: give an array of xml language files path, it will generate a single language property file"""


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

				lines = []

				lines.extend(self.schema(xmldoc).generateLines())

				for line in lines:
					outputFile.write(line)
			
			outputFile.close() # close the generated file

			print("File `" + str(outputFilePath) + "` succesfully generated")
			
		except IOError as e: #catch file error
			print "Unable to generate the output file. Error info: I/O error({0}) - {1}".format(e.errno, e.strerror)
		except UnicodeDecodeError as e: #catch encoding error
			print "Unable to generate the output file. Error info: UnicodeDecodeError - {0}".format(e)