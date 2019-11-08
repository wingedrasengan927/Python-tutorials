import lxml.etree as etree

def format_tree(filename):
    x = etree.parse(filename)
    xmlstr = etree.tostring(x, pretty_print=True)

    with open(filename, 'wb') as f:
        f.write(xmlstr)

format_tree("test.xml")