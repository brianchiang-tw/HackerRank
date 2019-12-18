from html.parser import  HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)

        for attr in attrs:
            # tag name: attr[0]
            # tag value: attr[1]  
            print(f'-> {attr[0]} > {attr[1]}')



    def handle_endtag(self, tag):
        print( "End   :", tag)



    def handle_startendtag(self, tag, attrs):
        print( "Empty :", tag)

        for attr in attrs:
            # tag name: attr[0]
            # tag value: attr[1]            
            print(f'-> {attr[0]} > {attr[1]}')


if __name__ == '__main__':

    n = int( input() )
    # instantiate the parser and fed it some HTML
    parser = MyHTMLParser()

    for _ in range( n ):

        input_str = input()

        parser.feed( input_str )