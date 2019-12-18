from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):

        # tag name
        print(f'{tag}')


        for attr in attrs:
            # -> {attribute name} > {attribute value}
            print(f'-> {attr[0]} > {attr[1]}')

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