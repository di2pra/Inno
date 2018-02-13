from xml.dom import minidom
from models.domObject import domObject
from models.item import item

class plurals(domObject):

	childObjects = [item]
	propertyName = 'name'