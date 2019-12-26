import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    global maxdepth
    
    if elem is None:
        return -1
    else:
        next_level = [ depth(child, level) for child in elem]
        if len(next_level) == 0:
            return 0
        else:
            maxdepth =  max( next_level ) + 1
        
        return maxdepth

if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)