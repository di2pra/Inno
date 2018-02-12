from classes.LanguageXMLConverter import LanguageXMLConverter



"""
 Example #1 generated Italian property language file
"""

italian = LanguageXMLConverter(['example/input/values-it/ads.xml', 'example/input/values-it/extra.xml', 'example/input/values-it/strings.xml', 'example/input/values-it/strings2.xml']);

italian.generateOutputFile('example/output/Italian.txt') #generate property type language output file



"""
 Example #2 generated English property language file
"""


english = LanguageXMLConverter() # init an instance of Language XML Converter with empty input file paths array

# add input file paths to the instance
english.addInputXMLFile('example/input/values/ads.xml')
english.addInputXMLFile('example/input/values/extra.xml')
english.addInputXMLFile('example/input/values/strings.xml')
english.addInputXMLFile('example/input/values/strings2.xml')

english.generateOutputFile('example/output/English.txt') #generate property type language output file
