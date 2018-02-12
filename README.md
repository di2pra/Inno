# Innovattic

## How to use?

In your script.py file import the LanguageXMLConverter python Class, below the exemple file :
```python
from classes.LanguageXMLConverter import LanguageXMLConverter
from models.plurals import plurals
from models.string import string


"""
 Example #1 generated Italian property language file
"""

italian = LanguageXMLConverter([string, plurals], ['example/input/values-it/ads.xml', 'example/input/values-it/extra.xml', 'example/input/values-it/strings.xml', 'example/input/values-it/strings2.xml']);

italian.generateOutputFile('example/output/Italian.txt') #generate property type language output file



"""
 Example #2 generated English property language file
"""


english = LanguageXMLConverter([string, plurals]) # init an instance of Language XML Converter with empty input file paths array

# add input file paths to the instance
english.addInputXMLFile('example/input/values/ads.xml')
english.addInputXMLFile('example/input/values/extra.xml')
english.addInputXMLFile('example/input/values/strings.xml')
english.addInputXMLFile('example/input/values/strings2.xml')

english.generateOutputFile('example/output/English.txt') #generate property type language output file

```

Open the command line tool in the main directory, and run the main python script. (Python 2.7)
