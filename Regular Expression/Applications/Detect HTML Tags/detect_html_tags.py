# Enter your code here. Read input from STDIN. Print output to STDOUT

from html.parser import HTMLParser

tag_set = set()

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):


        if tag not in tag_set:
            tag_set.add( tag)
            
        # tag name
        #print(f'{tag}')


        
    def handle_endtag(self, tag):
        #print("End tag  :", tag)
        pass

    def handle_data(self, data):
        #print("Data     :", data)
        pass

    def handle_comment(self, data):
        #print("Comment  :", data)
        pass



if __name__ == '__main__':

    html = ""       

    for i in range(int(input())):
        html += input().rstrip()
        html += '\n'
    
    parser = MyHTMLParser()
    parser.feed(html)
    parser.close()


    list_of_tag = list( tag_set )
    list_of_tag.sort()

    output_str = ';'.join( list_of_tag )

    print( output_str )