from html.parser import HTMLParser
from sys import stdin
from collections import defaultdict

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        #print( "{}:".format( tag), end ='')

        #for a in attrs:
        #    print( a[0] , end=',')
        if tag not in tag_attr_dict:
            tag_attr_dict[tag] = []

        for attr in attrs:
            if attr[0] not in tag_attr_dict[tag]:
                tag_attr_dict[tag].append( attr[0] )

    def handle_endtag(self, tag):
        #print("Encountered an end tag :", tag)
        pass

    def handle_data(self, data):
        #print("Encountered some data  :", data)
        pass


if __name__ == '__main__':

    tag_attr_dict = defaultdict( list )

    parser = MyHTMLParser()

    # get raw input from stdin
    parser.feed( stdin.read() )


    # extract keys from tag_attr_dict
    key_in_order = [ *tag_attr_dict ]

    # sort keys in lecical order
    key_in_order.sort()



    for tag in key_in_order:

        # get values from dictionary with key = tag
        attrs_in_order = tag_attr_dict[tag]

        # sort values in lexical order
        attrs_in_order.sort()

        print( f'{tag}', end = ':')
        print( ','.join(attrs_in_order) )