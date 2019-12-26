import sys
import xml.etree.ElementTree as etree



def get_attr_number(node):
    # your code goes here

    if node is None:
        return 0
    else:
        attr_cur = len(node.attrib)
        attr_child = sum([ get_attr_number(child) for child in node ]) 
        return attr_cur + attr_child



if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))