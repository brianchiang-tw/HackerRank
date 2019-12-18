from html.parser import HTMLParser
import re

class MyHTMLParser(HTMLParser):
  
    def handle_data(self, data):

        data_list = list( map( str, re.split( '\n|\t|\r', data ) ) )


        for d in data_list:
            if d != '':
                print(">>> Data")
                print( d )
                

    def handle_comment(self, data):
        comments = list( map( str, re.split( '\n|\t|\r', data ) ) )
        
        if len( comments ) > 1:
            print(">>> Multi-line Comment")
        else:
            print(">>> Single-line Comment")

        for c in comments:
            print( c )
  
  
  
  
  
  
  
  
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()

