from xml.dom import minidom
from models.domObject import domObject
from models.plurals import plurals
from models.string import string

class resources(domObject):

	childObjects = [string, plurals]