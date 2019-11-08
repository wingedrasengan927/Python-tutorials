'''
credits: https://www.youtube.com/watch?v=OAfeQuNhcps
'''

from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element
import xml.etree.ElementTree as etree
from xml.dom import minidom

# create root tag
root = Element('person')

# build the tree
tree = ElementTree(root)

# create a child element and append it to the root
name = Element('name')
root.append(name)

# give a value to the element
name.text = "julie"

# print the root
print(etree.tostring(root))

# write everything to a file
with open("test.xml", 'wb') as f:
    tree.write(f)